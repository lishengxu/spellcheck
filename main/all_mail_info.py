import re, collections
import os.path


class AllMailInfo(object):
    class MailInfo(object):
        def __init__(self, path_name):
            self.__path_name = os.path.relpath(path_name)
            self.__mail_dict = AllMailInfo.parse_mail_file(path_name)

        def get_path_name(self):
            return self.__path_name

        def get_mail_dict(self):
            return self.__mail_dict

    class WordFrequency(object):
        def __init__(self, word, frequency):
            self.__word = word
            self.__frequency = frequency

        def get_word(self):
            return self.__word

        def get_frequency(self):
            return self.__frequency

    def __init__(self, path_name):
        self.__path_name = os.path.relpath(path_name)
        self.__mail_index_dict = None
        self.__all_word_dict = None
        self.__all_word_frequency = None

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
    def split_index_info(word, split=' '):
        word_splits = word.split(split)
        words_not_null = []
        for each in word_splits:
            if each != '':
                words_not_null.append(each.strip())
        return words_not_null

    @staticmethod
    def parse_index_file(path_name):
        model = collections.defaultdict(lambda: [])
        lines = AllMailInfo.read_file_line(path_name)
        dir_name = os.path.dirname(path_name)
        for line in lines:
            words = AllMailInfo.split_index_info(line)
            model[words[0]].append(dir_name + os.path.sep + words[1])
        return model

    @staticmethod
    def parse_mail_file(path_name):
        model = collections.defaultdict(lambda: 0)
        lines = AllMailInfo.read_file_line(path_name)
        all_word = []
        for line in lines:
            all_word.extend(AllMailInfo.words(line))
        for word in all_word:
            model[word] += 1
        return model

    def parse(self):
        self.__mail_index_dict = AllMailInfo.static_parse(self.__path_name)

    @staticmethod
    def static_parse(path_name):
        result = collections.defaultdict(lambda: [])
        model = AllMailInfo.parse_index_file(path_name)
        for each in model.keys():
            for line in model.get(each):
                result[each].append(AllMailInfo.MailInfo(line))
        return result

    def get_file_path(self):
        return self.__path_name

    def get_mail_index_dict(self):
        return self.__mail_index_dict

    def collect_all_word(self):
        all_word_info = collections.defaultdict(lambda: 0)
        for key in self.__mail_index_dict.keys():
            for mail_info in self.__mail_index_dict.get(key):
                mail_dict = mail_info.get_mail_dict()
                for word in mail_dict.keys():
                    all_word_info[word] += mail_dict.get(word)
        return all_word_info

    def fit(self):
        self.__all_word_dict = self.collect_all_word()
        all_word_frequency = collections.defaultdict(lambda: [])
        for key in self.__all_word_dict.keys():
            for mail_index in self.__mail_index_dict.keys():
                total = len(self.__mail_index_dict.get(mail_index))
                count = 0
                for mail_info in self.__mail_index_dict.get(mail_index):
                    if mail_info.get_mail_dict().get(key) is not None:
                        count += 1
                all_word_frequency[mail_index].append(AllMailInfo.WordFrequency(key, count / total))
        self.__all_word_frequency = all_word_frequency
        # 获取所有的词
        # 计算每个词在mail中每个each中的的概率,存储在collection['word'] = 12中
        #
        return self.__all_word_frequency

    def predict(self):
        pass
