import unittest
import re, collections
from main.spam_filter import *


class Testspam_filter(unittest.TestCase):

    def test_read_file_line(self):
        file = 'testspam_filter_readfileline.txt'
        line = read_file_line(file)
        self.assertEqual('ab', line[0])
        self.assertEqual('cd', line[1])
        self.assertEqual('ef', line[2])

    def test_split_word(self):
        self.assertEqual([], split_word(''))
        self.assertEqual(['a'], split_word('a'))
        self.assertEqual(['a'], split_word(' a '))
        self.assertEqual(['ab'], split_word('ab'))
        splits = ['a', 'b']
        self.assertEqual(splits, split_word('a b'))
        self.assertEqual(splits, split_word(' a b'))
        self.assertEqual(splits, split_word(' a b '))
        self.assertEqual(['a', 'b', 'c'], split_word('a b c'))

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
        self.assertEqual(model, train_each_index('testspam_filter_get_all_info.txt'))
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
        self.assertEqual(model2, train_each_index('testspam_filter_get_all_info.txt', model))

    def test_get_all_spam_info(self):
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
        #self.assertEqual(model, get_all_spam_info())