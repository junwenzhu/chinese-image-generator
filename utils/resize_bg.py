import os
import cv2
import cfg

if not os.path.exists(cfg.path_bg2):
    os.makedirs(cfg.path_bg2)

def get_bigger_bg():
    min_height = 800
    min_width = 1200
    count = 0
    for home, dirs, files in os.walk(cfg.path_bg):
        for filename in files:
            if count % 500 == 0:
                print(count)
            count += 1
            fullname = os.path.join(home, filename)
            img = cv2.imread(fullname)
            if img is None:
                print(filename, "无法识别")
                continue
            height, width = img.shape[0], img.shape[1]
            scale = max(min_height / height, min_width / width)
            img = cv2.resize(img, (int(width * scale), int(height * scale)))
            img = img[100:img.shape[0] - 100, :]
            cv2.imwrite(cfg.path_bg2 + filename, img)


if __name__ == '__main__':
    get_bigger_bg()
