import unittest
from main.spam_filter import *

class Testspam_filter(unittest.TestCase):

    def test_words(self):
        text = ''
        self.assertEqual([], words(text))
        text = 'abd'
        self.assertEqual(['abd'], words(text))
        text = 'a.txt bef'
        self.assertEqual(['a', 'txt', 'bef'], words(text))
        text = 'ab     bef'
        self.assertEqual(['ab', 'bef'], words(text))
        text = 'ab+@test cd!test ef g'
        self.assertEqual(['ab', 'test', 'cd', 'test', 'ef', 'g'], words(text))

    def test_read_file_line(self):
        file = 'testspam_filter_readfileline.txt'
        line = read_file_line(file)
        self.assertEqual('ab', line[0])
        self.assertEqual('cd', line[1])
        self.assertEqual('ef', line[2])

    def test_split_index_info(self):
        self.assertEqual([], split_index_info(''))
        self.assertEqual(['a'], split_index_info('a'))
        self.assertEqual(['a'], split_index_info(' a '))
        self.assertEqual(['ab'], split_index_info('ab'))
        splits = ['a', 'b']
        self.assertEqual(splits, split_index_info('a  b'))
        self.assertEqual(splits, split_index_info(' a b'))
        self.assertEqual(splits, split_index_info(' a b '))
        self.assertEqual(['a', 'b', 'c'], split_index_info('a b c'))

    def test_chinese_split_content_info(self):
        self.assertEqual([], split_chinese_content_info(''))
        self.assertEqual(['a'], split_chinese_content_info('a'))
        self.assertEqual(['a'], split_chinese_content_info(' a '))
        self.assertEqual(['ab'], split_chinese_content_info('ab'))
        splits = ['a', 'b']
        self.assertEqual(splits, split_chinese_content_info('a b'))
        self.assertEqual(splits, split_chinese_content_info(' a b'))
        self.assertEqual(splits, split_chinese_content_info(' a b '))
        self.assertEqual(['a', 'b', 'c'], split_chinese_content_info('a b c'))
        self.assertEqual(['we', 'love', 'beijing', 'and', 'tianjin'],
                         split_chinese_content_info('we love beijing and tianjin'))
        self.assertEqual(['I', 'm', 'from', 'fuyang', 'at', 'pm', 'address2', 'xiaolitai'],
                         split_chinese_content_info('I\'m from fuyang, at 19890602, pm 05:00, address2:xiaolitai'))

    def test_train(self):
        text = ['']
        model = collections.defaultdict(lambda: 1)
        model[''] += 1
        self.assertEqual(model, train(text))
        model.clear()
        text = ['a']
        model['a'] += 1
        self.assertEqual(model, train(text))
        model.clear()
        text = ['a', 'a', 'aaaa']
        model['a'] += 2
        model['aaaa'] += 1
        self.assertEqual(model, train(text))
        model2 = model.copy()
        model2['a'] += 2
        model２['aaaa'] += 1
        self.assertEqual(model2, train(text, model))


    def test_get_all_info(self):
        lines = read_file_line('testspam_filter_get_all_info.txt')
        self.assertEqual(['ab cd', 'test', 'ef gh', 'tech', 'gh ef', 'ghtes efl adte'], lines)
        self.assertEqual([['ab', 'cd'], ['ef', 'gh'], ['gh', 'ef']], get_all_index(lines))
        self.assertEqual([], get_all_index([]))

    def test_train_each_index(self):
        model = collections.defaultdict(lambda: 1)
        model['ab'] += 1
        model['adte'] += 1
        model['cd'] += 1
        model['ef'] += 2
        model['efl'] += 1
        model['gh'] += 2
        model['ghtes'] += 1
        model['tech'] += 1
        model['test'] += 1
        self.assertEqual(model, train_each_index('testspam_filter_get_all_info.txt', split_chinese_content_info))
        model2 = model.copy()
        model2['ab'] += 1
        model2['adte'] += 1
        model2['cd'] += 1
        model2['ef'] += 2
        model2['efl'] += 1
        model2['gh'] += 2
        model2['ghtes'] += 1
        model2['tech'] += 1
        model2['test'] += 1
        self.assertEqual(model2, train_each_index('testspam_filter_get_all_info.txt', split_chinese_content_info, model))

    def test_chinese_get_all_spam_info(self):
        lines = []
        with open('testspam_filter_get_all_chinese_spam_info.txt', 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        model = collections.defaultdict(lambda: 0)
        for line in lines:
            words = split_index_info(line, ':')
            model[words[0]] += int(words[1])
        # model2 = get_chinese_all_spam_info()
        # print('---------------being--------')
        # for each in model2.keys():
        #     print(each, ':', model2.get(each))
        # print('-----------------------')
        # for each in model.keys():
        #     print(each, ':', model.get(each))
        # print('---------------end--------')
        # self.assertEqual(model, model2)

    def test_get_all_spam_info(self):
        lines = []
        with open('testspam_filter_get_all_spam_info.txt', 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        model = collections.defaultdict(lambda: 0)
        for line in lines:
            words = split_index_info(line, ':')
            model[words[0]] += int(words[1])
        model2 = get_all_spam_info()
        # print('---------------being--------')
        # for each in model2.keys():
        #     print(each, ':', model2.get(each))
        # print('-----------------------')
        # for each in model.keys():
        #     print(each, ':', model.get(each))
        # print('---------------end--------')
        self.assertEqual(model, model2)