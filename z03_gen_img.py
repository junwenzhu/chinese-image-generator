import cv2
import numpy as np
import pygame

import cfg
import glob
from multiprocessing import Process, Manager, Lock
import os
import math
from utils.gen_bg import get_bg_url, get_bg_crop
from utils.check_font import get_dic2d_charset
from utils.gen_pygame_img import get_pygame_img

import re
import random


class SampleGen:
    def __init__(self):
        self.total_num = 0  # 一共多少个句子

        self.__font_name = []  # 字体名，用于索引self.fonts
        self.__input_txt = cfg.txt_sentences  # 加载语料

        # 输出路径
        self.output_dir = cfg.path_img_output
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        file_path = os.path.join(self.output_dir, cfg.txt_gt_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        self.output = open(file_path, 'a', encoding='utf-8')

        # 加载字体文件
        self.__load_fonts()

        # 加载每个字体支持的字
        self.dic2d_charset = get_dic2d_charset()

        self.lst_bg_url = get_bg_url()

        self.lst_cache_bg = []

        self.__change_lst_bg()

    def get_lines(self):
        # 将每一行加工成一张图片
        lines = []
        for line in open(self.__input_txt, encoding='utf-8'):
            lines.append(line[:-1])
        return lines

    def process_lines(self, lock, mydict, sentences):
        for sentence in sentences:
            lock.acquire()
            line_num = mydict["line_num"]
            mydict["line_num"] += 1
            if line_num % cfg.num_change_bg == 0:
                self.__change_lst_bg()
            lock.release()

            if line_num % 1000 == 0:
                print("已经生成{}个，一共{}个".format(line_num, self.total_num))

            self.__process_line(line_num, sentence)

    def __load_fonts(self):
        font_path = os.path.join(cfg.path_font, "*.*")
        fonts = list(glob.glob(font_path))
        for font in fonts:
            self.__font_name.append(font)

    def __process_line(self, line_num, sentence):
        success, font_name, char = self.__save_pic(line_num, sentence)

        # 写图像文件名和类别序列的对照表
        if success:
            self.__save_gt(line_num, sentence)
        else:
            print(font_name, "【无法生成】", sentence, "【原因是存在不识别的字符】：", char)

    def __save_gt(self, line_num, sentence):
        # 写图像文件名和类别序列的对照表
        self.output.write("{:0>8d}.png\t{}\n".format(line_num, sentence))
        self.output.flush()  # 重点,在多进程中写文件需要尽快刷新,否则可能会导致数据丢失

    def __save_pic(self, line_num, sentence):
        # 根据字体名字获取字体包含哪些字符
        font_name = random.choice(self.__font_name)
        charset = self.dic2d_charset[font_name]

        for char in sentence:  # 如果字符 在 该字体下不存在， 返回False
            if char not in charset:
                return False, font_name, char

        save_path = os.path.join(self.output_dir, '{:0>8d}.png'.format(line_num))  # 类别序列即文件名

        background = get_pygame_img(self.lst_cache_bg, sentence, font_name)
        pygame.image.save(background, save_path)
        return True, font_name, ""

    def __change_lst_bg(self):
        print("正在重新缓存一批背景图...")
        self.lst_cache_bg = [cv2.imread(url_bg) for url_bg in random.choices(self.lst_bg_url, k=cfg.num_cache_bg)]


def main():
    sample_gen = SampleGen()
    sample_gen.__font_name = 1
    lines = sample_gen.get_lines()
    sample_gen.total_num = len(lines)

    manager = Manager()
    lock = Lock()
    mydict = manager.dict({"line_num": 0})
    core_num = cfg.core_num
    core_data_len = math.ceil(len(lines) / core_num)

    lst_p = []
    for i in range(core_num):
        # 对每个句子进行处理
        p = Process(target=sample_gen.process_lines,
                    args=(lock, mydict, lines[i * core_data_len:i * core_data_len + core_data_len]))
        p.start()
        lst_p.append(p)
    [p.join() for p in lst_p]
    sample_gen.output.close()


if __name__ == '__main__':
    main()
