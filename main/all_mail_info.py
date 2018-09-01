import re, collections
import os.path

class AllMailInfo(object):
    class MainInfo(object):
        def __init__(self, path_name):
            self.__path_name = os.path.relpath(path_name)
            self.__main_info = AllMailInfo.parse_mail_file(path_name)

        def get_path_name(self):
            return self.__path_name

        def get_mail_info(self):
            return self.__main_info

    def __init__(self, path_name):
        self.__path_name = os.path.relpath(path_name)
        self.__mail_info = None

    @staticmethod
    def words(text):
        return re.findall('[a-z]+', text.lower())

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

    @staticmethod
    def parse_mail_file(path_name):
        model = collections.defaultdict(lambda : 0)
        lines = AllMailInfo.read_file_line(path_name)
        all_word = []
        for line in lines:
            all_word.extend(AllMailInfo.words(line))
        for word in all_word:
            model[word] += 1
        return model

    def parse(self):
        self.__mail_info = AllMailInfo.static_parse(self.__path_name)

    @staticmethod
    def static_parse(path_name):
        result = collections.defaultdict(lambda: [])
        model = AllMailInfo.parse_index_file(path_name)
        for each in model.keys():
            for line in model.get(each):
                result[each].append(AllMailInfo.MainInfo(line))
        return result

    def get_file_path(self):
        return self.__path_name

    def get_mail_info(self):
        return self.__mail_info