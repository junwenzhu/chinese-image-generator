import random
import cfg

"""
定制化功能：
在文本开头可以按照权重加入自己设计的符号
"""
sign = []
sign_prob = []
for line in open(cfg.txt_sign, encoding="utf8"):
    res = line.strip().split("\t")
    sign.append(res[0])
    sign_prob.append(int(res[1]))


def get_sign():
    return random.choices(sign, weights=sign_prob)[0]


if __name__ == '__main__':
    print(random.choices(sign, weights=sign_prob))
