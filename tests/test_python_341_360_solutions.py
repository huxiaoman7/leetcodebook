import importlib.util
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_module(relative_path, name):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NestedInteger(object):

    def __init__(self, value):
        self.value = value

    def isInteger(self):
        return isinstance(self.value, int)

    def getInteger(self):
        return self.value if self.isInteger() else None

    def getList(self):
        return self.value if not self.isInteger() else None


class Python341To360SolutionTest(unittest.TestCase):

    def test_flatten_nested_list_iterator(self):
        module = load_module('python/341_FlattenNestedListIterator.py', 'nested_iterator')
        nested = [NestedInteger([NestedInteger(1), NestedInteger(1)]), NestedInteger(2), NestedInteger([NestedInteger(1), NestedInteger(1)])]
        iterator = module.NestedIterator(nested)
        result = []
        while iterator.hasNext():
            result.append(iterator.next())
        self.assertEqual(result, [1, 1, 2, 1, 1])

    def test_power_of_four(self):
        module = load_module('python/342_PowerofFour.py', 'power_four')
        self.assertTrue(module.Solution().isPowerOfFour(16))
        self.assertFalse(module.Solution().isPowerOfFour(8))

    def test_integer_break(self):
        module = load_module('python/343_IntegerBreak.py', 'integer_break')
        self.assertEqual(module.Solution().integerBreak(10), 36)

    def test_reverse_string(self):
        module = load_module('python/344_ReverseString.py', 'reverse_string')
        chars = ['h', 'e', 'l', 'l', 'o']
        module.Solution().reverseString(chars)
        self.assertEqual(chars, ['o', 'l', 'l', 'e', 'h'])

    def test_reverse_vowels(self):
        module = load_module('python/345_ReverseVowelsofaString.py', 'reverse_vowels')
        self.assertEqual(module.Solution().reverseVowels('hello'), 'holle')
        self.assertEqual(module.Solution().reverseVowels('leetcode'), 'leotcede')

    def test_moving_average(self):
        module = load_module('python/346_MovingAveragefromDataStream.py', 'moving_average')
        obj = module.MovingAverage(3)
        self.assertEqual(obj.next(1), 1.0)
        self.assertEqual(obj.next(10), 5.5)
        self.assertEqual(obj.next(3), 14.0 / 3)
        self.assertEqual(obj.next(5), 6.0)

    def test_top_k_frequent_elements(self):
        module = load_module('python/347_TopKFrequentElements.py', 'top_k')
        self.assertEqual(sorted(module.Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)), [1, 2])

    def test_design_tic_tac_toe(self):
        module = load_module('python/348_DesignTicTacToe.py', 'tic_tac_toe')
        game = module.TicTacToe(3)
        self.assertEqual(game.move(0, 0, 1), 0)
        self.assertEqual(game.move(0, 2, 2), 0)
        self.assertEqual(game.move(1, 1, 1), 0)
        self.assertEqual(game.move(1, 2, 2), 0)
        self.assertEqual(game.move(2, 2, 1), 1)

    def test_intersection_of_two_arrays(self):
        module = load_module('python/349_IntersectionofTwoArrays.py', 'intersection')
        self.assertEqual(sorted(module.Solution().intersection([1, 2, 2, 1], [2, 2])), [2])

    def test_intersection_of_two_arrays_ii(self):
        module = load_module('python/350_IntersectionofTwoArraysII.py', 'intersection_ii')
        self.assertEqual(sorted(module.Solution().intersect([1, 2, 2, 1], [2, 2])), [2, 2])

    def test_android_unlock_patterns(self):
        module = load_module('python/351_AndroidUnlockPatterns.py', 'android_patterns')
        self.assertEqual(module.Solution().numberOfPatterns(1, 1), 9)

    def test_data_stream_as_disjoint_intervals(self):
        module = load_module('python/352_DataStreamasDisjointIntervals.py', 'summary_ranges')
        obj = module.SummaryRanges()
        for value in [1, 3, 7, 2, 6]:
            obj.addNum(value)
        self.assertEqual(obj.getIntervals(), [[1, 3], [6, 7]])

    def test_design_snake_game(self):
        module = load_module('python/353_DesignSnakeGame.py', 'snake_game')
        game = module.SnakeGame(3, 2, [[1, 2], [0, 1]])
        self.assertEqual(game.move('R'), 0)
        self.assertEqual(game.move('D'), 0)
        self.assertEqual(game.move('R'), 1)
        self.assertEqual(game.move('U'), 1)
        self.assertEqual(game.move('L'), 2)

    def test_russian_doll_envelopes(self):
        module = load_module('python/354_RussianDollEnvelopes.py', 'envelopes')
        self.assertEqual(module.Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]), 3)

    def test_design_twitter(self):
        module = load_module('python/355_DesignTwitter.py', 'twitter')
        twitter = module.Twitter()
        twitter.postTweet(1, 5)
        self.assertEqual(twitter.getNewsFeed(1), [5])
        twitter.follow(1, 2)
        twitter.postTweet(2, 6)
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])
        twitter.unfollow(1, 2)
        self.assertEqual(twitter.getNewsFeed(1), [5])

    def test_line_reflection(self):
        module = load_module('python/356_LineReflection.py', 'line_reflection')
        self.assertTrue(module.Solution().isReflected([[1, 1], [-1, 1]]))
        self.assertFalse(module.Solution().isReflected([[1, 1], [-1, -1]]))

    def test_count_numbers_with_unique_digits(self):
        module = load_module('python/357_CountNumberswithUniqueDigits.py', 'unique_digits')
        self.assertEqual(module.Solution().countNumbersWithUniqueDigits(2), 91)

    def test_rearrange_string_k_distance_apart(self):
        module = load_module('python/358_RearrangeStringkDistanceApart.py', 'rearrange')
        result = module.Solution().rearrangeString('aabbcc', 3)
        self.assertEqual(sorted(result), sorted('aabbcc'))
        for i, ch in enumerate(result):
            for j in range(i + 1, len(result)):
                if result[j] == ch:
                    self.assertGreaterEqual(j - i, 3)

    def test_logger_rate_limiter(self):
        module = load_module('python/359_LoggerRateLimiter.py', 'logger')
        logger = module.Logger()
        self.assertTrue(logger.shouldPrintMessage(1, 'foo'))
        self.assertFalse(logger.shouldPrintMessage(2, 'foo'))
        self.assertTrue(logger.shouldPrintMessage(11, 'foo'))

    def test_sort_transformed_array(self):
        module = load_module('python/360_SortTransformedArray.py', 'transform')
        self.assertEqual(module.Solution().sortTransformedArray([-4, -2, 2, 4], 1, 3, 5), [3, 9, 15, 33])
        self.assertEqual(module.Solution().sortTransformedArray([-4, -2, 2, 4], -1, 3, 5), [-23, -5, 1, 7])


if __name__ == '__main__':
    unittest.main()
