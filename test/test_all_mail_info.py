import re, collections
import unittest
from main.all_mail_info import *

class TestAllMailInfo(unittest.TestCase):

    def test_init(self):
        test = AllMailInfo('index2')
        self.assertEqual('index2', test.get_file_path())

        test = AllMailInfo('../data/trec06p/full/index2')
        self.assertEqual('../data/trec06p/full/index2', test.get_file_path())

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
        model = collections.defaultdict(lambda : [])
        test = AllMailInfo('../data/trec06p/full/index3')
        self.assertEqual(model, test.get_index_info())

        test = AllMailInfo('../data/trec06p/full/index2')
        model['ham'].append('../data/trec06p/full/../data/000/000')
        model['ham'].append('../data/trec06p/full/../data/000/003')
        model['spam'].append('../data/trec06p/full/../data/000/001')
        model['spam'].append('../data/trec06p/full/../data/000/002')
        model['spam'].append('../data/trec06p/full/../data/000/004')
        self.assertEqual(model, AllMailInfo.parse_index_file('../data/trec06p/full/index2'))
        self.assertEqual(model, test.get_index_info())