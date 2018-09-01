import re, collections
import unittest
from main.all_mail_info import *


class TestAllMailInfo(unittest.TestCase):

    def test_init(self):
        test = AllMailInfo('index2')
        self.assertEqual('index2', test.get_file_path())

        test = AllMailInfo('../data/trec06p/full/index2')
        self.assertEqual('../data/trec06p/full/index2', test.get_file_path())

        test = AllMailInfo('../data/trec06p/full/../full/index2')
        self.assertEqual('../data/trec06p/full/index2', test.get_file_path())

    def test_words(self):
        text = ''
        self.assertEqual([], AllMailInfo.words(text))
        text = 'abd'
        self.assertEqual(['abd'], AllMailInfo.words(text))
        text = 'a.txt bef'
        self.assertEqual(['a', 'txt', 'bef'], AllMailInfo.words(text))
        text = 'ab     bef'
        self.assertEqual(['ab', 'bef'], AllMailInfo.words(text))
        text = 'ab+@test cd!test ef g'
        self.assertEqual(['ab', 'test', 'cd', 'test', 'ef', 'g'], AllMailInfo.words(text))

    def test_read_file_line(self):
        file = 'testspam_filter_readfileline.txt'
        line = AllMailInfo.read_file_line(file)
        self.assertEqual('ab', line[0])
        self.assertEqual('cd', line[1])
        self.assertEqual('ef', line[2])

    def test_split_index_info(self):
        self.assertEqual([], AllMailInfo.split_index_info(''))
        self.assertEqual(['a'], AllMailInfo.split_index_info('a'))
        self.assertEqual(['a'], AllMailInfo.split_index_info(' a '))
        self.assertEqual(['ab'], AllMailInfo.split_index_info('ab'))
        splits = ['a', 'b']
        self.assertEqual(splits, AllMailInfo.split_index_info('a  b'))
        self.assertEqual(splits, AllMailInfo.split_index_info(' a b'))
        self.assertEqual(splits, AllMailInfo.split_index_info(' a b '))
        self.assertEqual(['a', 'b', 'c'], AllMailInfo.split_index_info('a b c'))

    def test_parse_index_file(self):
        model = collections.defaultdict(lambda: [])

        model['ham'].append('../data/trec06p/full/../data/000/000')
        model['ham'].append('../data/trec06p/full/../data/000/003')
        model['spam'].append('../data/trec06p/full/../data/000/001')
        model['spam'].append('../data/trec06p/full/../data/000/002')
        model['spam'].append('../data/trec06p/full/../data/000/004')
        self.assertEqual(model, AllMailInfo.parse_index_file('../data/trec06p/full/index2'))

    def test_parse_mail_file(self):
        lines = []
        with open('test_all_mail_info_parse_mail_file.txt', 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        model = collections.defaultdict(lambda: 0)
        for line in lines:
            word_split = AllMailInfo.split_index_info(line, ':')
            model[word_split[0]] += int(word_split[1])
        model2 = AllMailInfo.parse_mail_file('../data/trec06p/data/000/000')
        self.assertEqual(model, model2)

    def test_MainInfo(self):
        lines = []
        with open('test_all_mail_info_parse_mail_file.txt', 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        model = collections.defaultdict(lambda: 0)
        for line in lines:
            word_split = AllMailInfo.split_index_info(line, ':')
            model[word_split[0]] += int(word_split[1])
        test = AllMailInfo.MainInfo('../data/trec06p/data/000/000')
        self.assertEqual(model, test.get_mail_info())

    def test_static_parse(self):
        model = collections.defaultdict(lambda: [])
        model['ham'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/000'))
        model['ham'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/003'))
        model['spam'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/001'))
        model['spam'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/002'))
        model['spam'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/004'))

        model2 = AllMailInfo.static_parse('../data/trec06p/full/index3')
        for each in model.keys():
            lines_expected = model.get(each)
            lines_actual = model2.get(each)
            for index in range(len(lines_expected)):
                expected = lines_expected[index]
                actual = lines_actual[index]
                self.assertEqual(expected.get_path_name(), actual.get_path_name())
                self.assertEqual(expected.get_mail_info(), actual.get_mail_info())

    def test_parse(self):
        model = collections.defaultdict(lambda: [])
        model['ham'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/000'))
        model['ham'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/003'))
        model['spam'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/001'))
        model['spam'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/002'))
        model['spam'].append(AllMailInfo.MainInfo('../data/trec06p/data/000/004'))

        test = AllMailInfo('../data/trec06p/full/index3')
        test.parse()
        model2 = test.get_mail_info()
        for each in model.keys():
            lines_expected = model.get(each)
            lines_actual = model2.get(each)
            for index in range(len(lines_expected)):
                expected = lines_expected[index]
                actual = lines_actual[index]
                self.assertEqual(expected.get_path_name(), actual.get_path_name())
                self.assertEqual(expected.get_mail_info(), actual.get_mail_info())