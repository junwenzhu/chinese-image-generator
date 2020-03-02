import cfg


def main():
    lst = []
    for i in open(cfg.txt_charset_raw, encoding='utf-8'):
        lst.append(i[:-1])
    print("初始字符数", len(lst))

    set_char = list(set(lst))
    set_char.sort()
    print("去重后字符数", len(set_char))

    f = open(cfg.txt_charset_unique, "w", encoding='utf-8')
    for i in set_char:
        f.write(i + "\n")


if __name__ == '__main__':
    main()
