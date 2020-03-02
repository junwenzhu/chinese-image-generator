import pygame
import cv2
import cfg
import random
from utils.gen_bg import get_bg_url, get_bg_crop
import numpy as np

pygame.init()


def get_pygame_img(lst_cache_bg, text, font_name):
    font = pygame.font.Font(font_name, cfg.font_size - random.randint(0, cfg.font_size_range))
    if random.random() < cfg.prob_bold:
        font.set_bold(True)
    if random.random() < cfg.prob_italic:
        font.set_italic(True)
    if random.random() < cfg.prob_underline:
        font.set_underline(True)

    # 创建文字颜色
    char_b = random.randint(0, 255)
    char_g = random.randint(0, 255)
    char_r = random.randint(0, 255)

    img_text = font.render(text, True, (char_b, char_g, char_r))
    img_w, img_h = img_text.get_size()

    w_add = random.randint(0, cfg.w_range)
    h_add = random.randint(0, cfg.h_range)
    if random.random() < cfg.prob_use_bg:  # 使用背景图
        img = get_bg_crop(lst_cache_bg, img_w + w_add, img_h + h_add, text)
        img = img.transpose((1, 0, 2))
    else:  # 使用纯色背景
        img = np.ones(shape=(img_w + w_add, img_h + h_add, 3), dtype=int)
        img[:, :, 0] *= random.randint(0, 255)
        img[:, :, 1] *= random.randint(0, 255)
        img[:, :, 2] *= random.randint(0, 255)

    background = pygame.surfarray.make_surface(img)
    # print(background.get_size())
    # 获取中心的坐标
    center = ((background.get_width() + random.randint(0, w_add)) / 2,
              (background.get_height() + random.randint(0, h_add)) / 2)
    # center = (500, 500)
    # 获取设置后新的坐标区域
    textpos = img_text.get_rect(center=center)

    background.blit(img_text, textpos)

    return background


if __name__ == '__main__':
    img = cv2.imread("1.png", 1).transpose((1, 0, 2))
    # background = pygame.image.load("1.png")
    background = pygame.surfarray.make_surface(img)
    # font = pygame.font.Font(None, 56)
    font = pygame.font.Font("fonts/书体坊颜体.ttf", 100)
    font.set_bold(True)
    # font.set_italic(True)
    font.set_underline(True)
    # 文本与颜色
    text = font.render("sad发大水大发送到", 0, (255, 10, 10))
    print(background.get_size())
    # 获取中心的坐标
    center = (background.get_width() / 2, background.get_height() / 2)
    # center = (500, 500)
    # 获取设置后新的坐标区域
    textpos = text.get_rect(center=center)

    background.blit(text, textpos)

    background = pygame.surfarray.array3d(background)
    cv2.imwrite("2.png", background.transpose((1, 0, 2)))

    # pygame.image.save(background, "tt.png")
