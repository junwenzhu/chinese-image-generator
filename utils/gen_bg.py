import cv2
import os
import random
import cfg

def get_bg_url():
    lst_bg_url = []
    for dirpath, dirnames, filenames in os.walk(cfg.path_bg2):
        for name in filenames:
            _, ext = os.path.splitext(name)
            ext = ext.lower()
            if ext == '.jpg' or ext == '.jpeg' or ext == '.png':
                fullname = os.path.join(dirpath, name)
                lst_bg_url.append(fullname)
    return lst_bg_url


def get_bg_crop(lst_cache_bg,width_crop=20, height_crop=20,sentence=""):
    img = random.choice(lst_cache_bg)
    height,width = img.shape[0],img.shape[1]
    if height < height_crop:
        print("height < height_crop",height , height_crop,sentence)
        height = height_crop
        img = cv2.resize(img, (width, height_crop))
    if width < width_crop:
        print("width < width_crop",width , width_crop,sentence)
        width = width_crop
        img = cv2.resize(img, (width_crop, height))

    width_range = random.randint(0, width - width_crop)
    height_range = random.randint(0, height - height_crop)

    left, upper, right, lower = 0 + width_range, 0 + height_range, \
                                width_crop + width_range, height_crop + height_range

    img2 = img[upper:lower, left:right]

    return img2


if __name__ == '__main__':
    lst_bg_url = get_bg_url()
    img = get_bg_crop(lst_bg_url, width_crop=200, height_crop=200,sentence="")
    cv2.imwrite('crop_img.jpg', img)
