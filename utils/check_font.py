import glob

from libs_font.font_utils import check_font_chars, load_font
import cfg

font_paths = glob.glob(cfg.path_font + '*.*')

DIC2D = {}


def get_dic2d_charset():
    fonts = {}
    for p in font_paths:
        ttf = load_font(p)
        fonts[p] = ttf

    for fontname, ttf in fonts.items():
        chars = check_font_chars(ttf)
        DIC2D[fontname] = chars
    return DIC2D


if __name__ == '__main__':

    fonts = {}
    for p in font_paths:
        ttf = load_font(p)
        fonts[p] = ttf

    useful_fonts = []
    for k, ttf in fonts.items():
        print(k)
        chars = check_font_chars(ttf)
        print(len(chars))

# if ord(c) not in chars_int:
