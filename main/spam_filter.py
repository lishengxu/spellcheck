import re, collections
import jieba

def words(text):
    return re.findall('[a-z]+', text.lower())

def read_file_line(file_name):
    lines = []
    with open(file_name, 'r', encoding='gbk', errors = 'ignore') as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines

def split_index_info(word, split = ' '):
    word_splits = word.split(split)
    words_not_null = []
    for each in word_splits:
        if each != '':
            words_not_null.append(each.strip())
    return words_not_null

def split_chinese_content_info(word):
    word_cut = jieba.cut(word, cut_all=True)
    words_split = ' '.join(word_cut)
    words_splits = words_split.split(' ')
    words_not_null = []
    for each in words_splits:
        if each != '' and (not each.isdigit()):
            words_not_null.append(each)
    return words_not_null

def get_all_index(lines):
    all_info = []
    for line in lines:
        word_splits = split_index_info(line)
        if len(word_splits) == 2:
            all_info.append(word_splits)
    return all_info

def train(features, model = None):
    if model is None:
        model = collections.defaultdict(lambda: 1)
    for each in features:
        model[each] += 1
    return model

def train_each_index(file_name, split_func, model = None):
    all_word = []
    lines = read_file_line(file_name)
    for line in lines:
        all_word.extend(split_func(line))
    return train(all_word, model)

def get_chinese_all_spam_info():
    model = collections.defaultdict(lambda: 0)
    file_path = '../data/trec06c/full'
    lines = read_file_line(file_path + '/index')
    all_info = get_all_index(lines)
    for info in all_info:
        if info[0] == 'spam':
            train_each_index(file_path + '/' + info[1], split_chinese_content_info, model)
    return model

def get_all_spam_info():
    model = collections.defaultdict(lambda: 0)
    file_path = '../data/trec06p/full'
    lines = read_file_line(file_path + '/index1')
    all_info = get_all_index(lines)
    for info in all_info:
        if info[0] == 'spam':
            train_each_index(file_path + '/' + info[1], words, model)
    return model