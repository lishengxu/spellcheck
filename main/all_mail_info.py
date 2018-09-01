import re, collections
import os.path

class AllMailInfo(object):
    def __init__(self, path_name):
        self.__path_name = path_name
        self.__index_info = AllMailInfo.parse_index_file(path_name)

    @staticmethod
    def read_file_line(path_name):
        lines = []
        if not os.path.exists(path_name):
            return lines

        with open(path_name, 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        return lines

    @staticmethod
    def split_index_info(word, split = ' '):
        word_splits = word.split(split)
        words_not_null = []
        for each in word_splits:
            if each != '':
                words_not_null.append(each.strip())
        return words_not_null

    @staticmethod
    def parse_index_file(path_name):
        model = collections.defaultdict(lambda : [])
        lines = AllMailInfo.read_file_line(path_name)
        dir_name = os.path.dirname(path_name)
        for line in lines:
            words = AllMailInfo.split_index_info(line)
            model[words[0]].append(dir_name + os.path.sep + words[1])
        return model

    def get_file_path(self):
        return self.__path_name

    def get_index_info(self):
        return self.__index_info