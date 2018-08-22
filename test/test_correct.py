import unittest
from main.correct import *


class Testcorrect(unittest.TestCase):

    def testwords(self):
        text = ''
        self.assertEqual([], words(text))
        text = 'abd'
        self.assertEqual(['abd'], words(text))
        text = 'a b'
        self.assertEqual(['a', 'b'], words(text))
        text = 'ab     '
        self.assertEqual(['ab'], words(text))
        text = 'ab cd ef g'
        self.assertEqual(['ab', 'cd', 'ef', 'g'], words(text))

    def testtrain(self):
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

    def testedits1(self):
        text = ''
        alphabetset = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z'}
        self.assertEqual(alphabetset, edits1(text))
        alphabetset.clear()
        text = 'word'
        alphabetset = {'eword', 'aord', 'uword', 'woid', 'wsord', 'woryd', 'wordd', 'worvd', 'vord', 'wobrd', 'uord',
                       'bord', 'bword', 'wordq', 'wored', 'worod', 'wrrd', 'wtrd', 'wortd', 'kord', 'wordp', 'wopd',
                       'wford', 'wlord', 'wogrd', 'xord', 'wozd', 'work', 'wodd', 'wori', 'nword', 'oord', 'wurd',
                       'wwrd', 'woard', 'wourd', 'tord', 'world', 'worad', 'worl', 'oword', 'wold', 'werd', 'wcord',
                       'fword', 'worzd', 'ward', 'wordm', 'wgrd', 'whrd', 'wordh', 'worxd', 'wyord', 'worpd', 'dword',
                       'pord', 'wodrd', 'wdord', 'dord', 'wmord', 'wdrd', 'worcd', 'aword', 'wocrd', 'wofrd', 'wordr',
                       'iword', 'worz', 'weord', 'yord', 'workd', 'wordj', 'wordo', 'wcrd', 'worsd', 'wotrd', 'wordc',
                       'wodr', 'worwd', 'wzrd', 'wore', 'worx', 'wormd', 'wordl', 'wordy', 'wprd', 'qord', 'sword',
                       'wxord', 'wolrd', 'wowrd', 'worde', 'xword', 'worud', 'wjrd', 'mord', 'woqrd', 'wojrd', 'woro',
                       'woxd', 'woqd', 'worn', 'nord', 'woru', 'lword', 'tword', 'wordx', 'worv', 'woad', 'qword',
                       'wkord', 'wvrd', 'mword', 'worf', 'vword', 'ord', 'wort', 'hord', 'gord', 'worj', 'wordk',
                       'word', 'wmrd', 'worc', 'eord', 'worda', 'wordv', 'worg', 'wuord', 'sord', 'woxrd', 'wor',
                       'wordt', 'woed', 'woerd', 'cword', 'woud', 'wordf', 'wrd', 'woird', 'ford', 'worfd', 'woprd',
                       'worrd', 'wzord', 'wohd', 'wod', 'jword', 'wnrd', 'wosrd', 'wosd', 'jord', 'worgd', 'kword',
                       'hword', 'wqord', 'wxrd', 'wbord', 'woord', 'wvord', 'worjd', 'wors', 'wordw', 'yword', 'womd',
                       'gword', 'wohrd', 'worqd', 'worw', 'wrod', 'whord', 'wfrd', 'owrd', 'wond', 'zord', 'wogd',
                       'words', 'worh', 'wowd', 'rword', 'wnord', 'cord', 'wtord', 'wiord', 'wpord', 'wonrd', 'woyrd',
                       'wordg', 'worm', 'wocd', 'wqrd', 'wokd', 'wrord', 'wjord', 'worp', 'pword', 'wordb', 'wordz',
                       'worb', 'wozrd', 'wordn', 'woyd', 'wyrd', 'wword', 'wgord', 'womrd', 'wovrd', 'wbrd', 'zword',
                       'worr', 'wordi', 'wornd', 'wordu', 'rord', 'wlrd', 'wofd', 'worbd', 'lord', 'wsrd', 'wory',
                       'worhd', 'wird', 'wotd', 'worid', 'wood', 'waord', 'wora', 'wobd', 'wokrd', 'wojd', 'worq',
                       'wovd', 'wkrd', 'iord', }
        self.assertEqual(alphabetset, edits1(text))

    def testKnown(self):
        text = 'word'
        alphabetknownset = {'cord', 'ford', 'lord', 'sword', 'ward', 'wood', 'word', 'words', 'wordy', 'wore', 'work',
                            'world', 'worm', 'worn'}
        self.assertEqual(alphabetknownset, known(edits1(text)))

    def testknown_edits2(self):
        text = 'word'
        alphabetknown_edits2 = {'award', 'bird', 'board', 'bold', 'bond', 'bore', 'bored', 'born', 'bory', 'card',
                                'chord', 'cod', 'cold', 'cord', 'cords', 'core', 'cork', 'corn', 'dodd', 'dorr', 'fold',
                                'fond', 'food', 'for', 'ford', 'fords', 'fork', 'form', 'fort', 'gird', 'god', 'gold',
                                'good', 'gory', 'hard', 'herd', 'hoard', 'hold', 'hood', 'horde', 'horn', 'hors',
                                'load', 'lord', 'lords', 'loud', 'mold', 'mood', 'more', 'mort', 'nod', 'nor', 'odd',
                                'old', 'or', 'orb', 'ore', 'org', 'owed', 'pond', 'pork', 'port', 'rd', 'road', 'rod',
                                'sird', 'sold', 'sore', 'sort', 'sword', 'swords', 'swore', 'sworn', 'told', 'tore',
                                'torn', 'tory', 'trod', 'void', 'wad', 'war', 'ward', 'wards', 'ware', 'warm', 'warn',
                                'warp', 'wars', 'wart', 'wary', 'weed', 'weird', 'weld', 'were', 'wild', 'wind', 'wire',
                                'wired', 'wirt', 'wiry', 'wo', 'woes', 'woke', 'wolf', 'won', 'wont', 'wood', 'woods',
                                'woof', 'wool', 'woot', 'word', 'worded', 'words', 'wordy', 'wore', 'work', 'worked',
                                'works', 'world', 'worlds', 'worm', 'worms', 'worn', 'worry', 'worse', 'worst', 'worth',
                                'would', 'wound', 'wove', 'wry', 'yard', 'york'}
        self.assertEqual(alphabetknown_edits2, known_edits2(text))

    def testcorrect(self):
        text = 'word'
        self.assertEqual('word', correct(text))
        text = 'wor'
        self.assertEqual('for', correct(text))
        text = 'percfeact'
        self.assertEqual('perfect', correct(text))
        text = 'abcdefghijklmn'
        self.assertEqual('abcdefghijklmn', correct(text))