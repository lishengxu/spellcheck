import re, collections

def read_file_line(file_name):
    lines = []
    with open(file_name, 'r', errors = 'ignore') as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines

def split_word(word):
    words = word.split(' ')
    words_not_null = []
    for word in words:
        if word != '':
            words_not_null.append(word)
    return words_not_null

def get_all_index(lines):
    all_info = []
    for line in lines:
        words = split_word(line)
        if len(words) == 2:
            all_info.append(words)
    return all_info

def train(features, model = None):
    if model == None:
        model = collections.defaultdict(lambda: 1)
    for each in features:
        model[each] += 1
    return model

def train_each_index(file_name, model = None):
    all_word = []
    lines = read_file_line(file_name)
    for line in lines:
        all_word.extend(split_word(line))
    return train(all_word, model)

def get_all_spam_info():
    model = collections.defaultdict(lambda: 0)
    file_path = '../data/trec06c/full'
    lines = read_file_line(file_path + '/index')
    all_info = get_all_index(lines)
    for info in all_info:
        if info[0] == 'spam':
            train_each_index(file_path + '/' + info[1], model)
    return model