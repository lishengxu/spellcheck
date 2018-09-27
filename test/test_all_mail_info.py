import re, collections
import unittest
from main.all_mail_info import *


class TestAllMailInfo(unittest.TestCase):

    @unittest.skip
    def test_init(self):
        test = AllMailInfo('index2')
        self.assertEqual('index2', test.get_file_path())

        test = AllMailInfo('../data/trec06p/full/index2')
        self.assertEqual('../data/trec06p/full/index2', test.get_file_path())

        test = AllMailInfo('../data/trec06p/full/../full/index2')
        self.assertEqual('../data/trec06p/full/index2', test.get_file_path())

    @unittest.skip
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

    @unittest.skip
    def test_read_file_line(self):
        file = 'test_all_mail_info_readfileline.txt'
        line = AllMailInfo.read_file_line(file)
        self.assertEqual('ab', line[0])
        self.assertEqual('cd', line[1])
        self.assertEqual('ef', line[2])

    @unittest.skip
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

    @unittest.skip
    def test_parse_index_file(self):
        model = collections.defaultdict(lambda: [])

        model['ham'].append('../data/trec06p/full/../data/000/000')
        model['ham'].append('../data/trec06p/full/../data/000/003')
        model['spam'].append('../data/trec06p/full/../data/000/001')
        model['spam'].append('../data/trec06p/full/../data/000/002')
        model['spam'].append('../data/trec06p/full/../data/000/004')
        self.assertEqual(model, AllMailInfo.parse_index_file('../data/trec06p/full/index2'))

    @unittest.skip
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

    @unittest.skip
    def test_MainInfo(self):
        lines = []
        with open('test_all_mail_info_parse_mail_file.txt', 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        model = collections.defaultdict(lambda: 0)
        for line in lines:
            word_split = AllMailInfo.split_index_info(line, ':')
            model[word_split[0]] += int(word_split[1])
        test = AllMailInfo.MailInfo('../data/trec06p/data/000/000')
        self.assertEqual(model, test.get_mail_dict())

    @unittest.skip
    def test_static_parse(self):
        model = collections.defaultdict(lambda: [])
        model['ham'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/000'))
        model['ham'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/003'))
        model['spam'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/001'))
        model['spam'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/002'))
        model['spam'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/004'))

        model2 = AllMailInfo.static_parse('../data/trec06p/full/index3')
        for each in model.keys():
            lines_expected = model.get(each)
            lines_actual = model2.get(each)
            for index in range(len(lines_expected)):
                expected = lines_expected[index]
                actual = lines_actual[index]
                self.assertEqual(expected.get_path_name(), actual.get_path_name())
                self.assertEqual(expected.get_mail_dict(), actual.get_mail_dict())

    @unittest.skip
    def test_parse(self):
        model = collections.defaultdict(lambda: [])
        model['ham'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/000'))
        model['ham'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/003'))
        model['spam'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/001'))
        model['spam'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/002'))
        model['spam'].append(AllMailInfo.MailInfo('../data/trec06p/data/000/004'))

        test = AllMailInfo('../data/trec06p/full/index3')
        test.parse()
        model2 = test.get_mail_index_dict()
        for each in model.keys():
            lines_expected = model.get(each)
            lines_actual = model2.get(each)
            for index in range(len(lines_expected)):
                expected = lines_expected[index]
                actual = lines_actual[index]
                self.assertEqual(expected.get_path_name(), actual.get_path_name())
                self.assertEqual(expected.get_mail_dict(), actual.get_mail_dict())

    @unittest.skip
    def test_collect_all_word(self):
        lines = []
        with open('test_all_mail_info_collection_all_word.txt', 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        model = collections.defaultdict(lambda: 0)
        for line in lines:
            word_split = AllMailInfo.split_index_info(line, ':')
            model[word_split[0]] += int(word_split[1])

        test = AllMailInfo('../data/trec06p/full/index4')
        test.parse()
        self.assertEqual(model, test.collect_all_word())

    @unittest.skip
    def test_fit(self):
        lines = []
        with open('test_all_mail_info_fit.txt', 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        model = collections.defaultdict(lambda: 0)
        for line in lines:
            word_split = AllMailInfo.split_index_info(line, ':')
            model[word_split[0]] += float(word_split[1])

        test = AllMailInfo('../data/trec06p/full/index4')
        test.parse()
        word_frequency = test.fit()

        model2 = collections.defaultdict(lambda: 0)
        for key in word_frequency.keys():
            lines = word_frequency.get(key)
            for line in lines:
                model2[line.get_word()] += float(line.get_frequency())
        for key in model2.keys():
            self.assertAlmostEqual(model.get(key), model2.get(key), 6)
        for key in model.keys():
            self.assertAlmostEqual(model.get(key), model2.get(key), 6)

    def test_predict(self):
        lines = []
        path_name = '../data/trec06p/full/index_test'
        with open(path_name, 'r', errors='ignore') as f:
            for line in f.readlines():
                lines.append(line.strip())
        model = collections.defaultdict(lambda: [])
        for line in lines:
            word_split = AllMailInfo.split_index_info(line, ' ')
            model[word_split[0]].append(AllMailInfo.MailInfo(
                os.path.dirname(path_name) + os.path.sep + word_split[1]))

        test = AllMailInfo('../data/trec06p/full/index_fit')
        test.parse()
        test.fit()
        print('3333')
        for key in model.keys():
            for mail_info in model.get(key):
                temp_list = []
                for work in mail_info.get_mail_dict().keys():
                    temp_list.append(work)
                self.assertTrue(test.predict_spam(temp_list))
