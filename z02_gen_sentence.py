import os
import random
from utils.sign import get_sign
import cfg


def get_charset():
    dic = {}
    for char in open(cfg.txt_charset_unique,encoding="utf8"):
        dic[char[0]] = None
    return dic


def add_sentence(dir, len_min_sentence, len_max_sentence, sentences_count):
    str_sentence_all = ""
    for home, dirs, files in os.walk(dir):  # 将语料串成一句话
        for filename in files:
            fullname = os.path.join(home, filename)
            for line in open(fullname, encoding='utf8'):
                str_sentence_all += line[:-1]
    for i in range(sentences_count):  # 抽取一个片段
        char_start = random.randint(0, len(str_sentence_all) - len_max_sentence)
        len_sentence = random.randint(len_min_sentence, len_max_sentence)
        sentence = str_sentence_all[char_start:char_start + len_sentence]
        has_unknown_char = False
        for char in sentence:
            if char not in DIC_CHARSET:
                has_unknown_char = True
                break
        if has_unknown_char == False:
            LST_SENTENCE.append(sentence.strip())


DIC_CHARSET = get_charset()
LST_SENTENCE = []


def main():
    print("产生句子中...")
    f = open(cfg.txt_sentences, "w", encoding="utf8")
    # 中文字符最小/大长度，如果宽度为32像素，35个字符的长度约为750像素
    add_sentence(dir=cfg.path_corpus_cn, len_min_sentence=cfg.len_min_sentence_cn,
                 len_max_sentence=cfg.len_max_sentence_cn, sentences_count=cfg.sentences_count_cn)
    # 英文字符最小/大长度，如果宽度为32像素，47个字符的长度约为750像素
    add_sentence(dir=cfg.path_corpus_en, len_min_sentence=cfg.len_min_sentence_en,
                 len_max_sentence=cfg.len_max_sentence_en, sentences_count=cfg.sentences_count_en)

    random.shuffle(LST_SENTENCE)

    final_len = len(LST_SENTENCE)
    for sentence in LST_SENTENCE:
        if sentence in ["", ",", ".", "?", ";", ":", "\"", "\'", "[", "]", "`", "“", "”", "。", ".", "—", "-", "_"]:
            final_len -= 1
            continue
        if random.random() < cfg.prob_add_sign:  # 10%的开头有符号
            sign = get_sign()
            sentence = sign + sentence
            sentence = sentence[:len(sentence) - len(sign)]

        f.write(sentence + "\n")
    print("生成的句子数：",final_len)


if __name__ == '__main__':
    main()
