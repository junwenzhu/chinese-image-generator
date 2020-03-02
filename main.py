import os
import sys
import cfg

import z01_charset_unique
import z02_gen_sentence
import z03_gen_img
import z03_gen_img_win32

from utils.resize_bg import get_bigger_bg

if __name__ == '__main__':
    # 该方法只需运行一次，可以将背景图片提前放大，加速最终img的生成，不然每次都要对图像进行拉伸十分耗时
    get_bigger_bg()

    # 将字符集命名为charset_raw.txt放在根目录
    # 对字符集去重排序输出新的字符集
    z01_charset_unique.main()

    # 将语料放入corpus,中英分开
    z02_gen_sentence.main()

    # 生成图像
    if sys.platform == "win32":
        # window下多进程有点问题，每次生成数据请手动删掉res文件夹
        z03_gen_img_win32.main()
    else:
        z03_gen_img.main()
