# 用户添加的背景图
path_bg = "bg/"

# 程序将其拉伸，输出的路径
path_bg2 = "bg2/"

# 缓存背景的张数，每次从path_bg2抽取一批数据缓冲到内存，以加快生成图像的速度
num_cache_bg = 2

# 每隔多少轮换一批内存中的背景
num_change_bg = 50

# 用户的字典，有可能由于疏忽出现两个相同的字符
txt_charset_raw = "charset_raw.txt"

# 去重后的字典，对用户的字典进行去重，排序
txt_charset_unique = "charset_unique.txt"

# 存放语料的文件夹，因为网络中有Bilstm，所以需要用有语义的句子训练ocr识别模型，语料不比做成一个文件，都放在文件夹下即可
path_corpus_cn = "corpus/CN/"
path_corpus_en = "corpus/EN/"

# 生成的一行一行的语料文件
txt_sentences = "sentence.txt"

# 10%的开头有符号  #这是一个定制化功能，比如你要识别的内容以经常以特定字符开头，可以有针对性的生成特定的图片
prob_add_sign = 0.1

# 在文本开头可以按照权重加入自己设计的符号
txt_sign = "configs/sign.txt"

# 每一行语料的配置信息
# 中文字符最小/大长度，如果宽度为32像素，35个字符的长度约为750像素
len_min_sentence_cn = 10
len_max_sentence_cn = 35
# 要生产多少张，总数可能少于设置的值，因为有的字符不在特定的字体中
sentences_count_cn = 300

# 英文字符最小/大长度，如果宽度为32像素，47个字符的长度约为750像素
len_min_sentence_en = 10
len_max_sentence_en = 47
# 要生产多少张，总数可能少于设置的值，因为有的字符不在特定的字体中
sentences_count_en = 100

# 字体文件路径
path_font = 'fonts/'

# 图片输出路径
path_img_output = 'res/'

# 图像和label的映射表
txt_gt_name = "gt.txt"

# 图像高度
# img_h = 32 这个不好设置，因为不同的字体size不一致

# 文字像素
font_size = 32  # 有可能生成的图像大于文字的像素

# 像素向下浮动范围
font_size_range = 4  # 最终文字像素在【char_pix-char_pix_range,char_pix】之间

prob_bold = 0.5  # 加粗的概率
prob_italic = 0.5  # 斜体的概率
prob_underline = 0.5  # 下划线的概率

# 图像宽高的浮动，字会在其中游离
w_range = 100
h_range = 20

# 使用背景图片的概率，否则会随机生成rgb纯色背景
prob_use_bg = 0.5

# 多少个进程
core_num = 8  #根据自己机器，选择启动多少个进程；实测：阿里云16核服务器 可以设置160个进程，生成速度：每秒1500张
