import importlib.util
import pathlib
import random
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_module(relative_path, name):
    path = ROOT / relative_path
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def nested_to_list(nested):
    if nested.isInteger():
        return nested.getInteger()
    return [nested_to_list(item) for item in nested.getList()]


class Python381To400SolutionTest(unittest.TestCase):

    def test_insert_delete_get_random_duplicates_allowed(self):
        module = load_module('python/381_InsertDeleteGetRandomO1DuplicatesAllowed.py', 'randomized_collection')
        obj = module.RandomizedCollection()
        self.assertTrue(obj.insert(1))
        self.assertFalse(obj.insert(1))
        self.assertTrue(obj.insert(2))
        self.assertIn(obj.getRandom(), {1, 2})
        self.assertTrue(obj.remove(1))
        self.assertIn(obj.getRandom(), {1, 2})
        self.assertTrue(obj.remove(1))
        self.assertEqual(obj.getRandom(), 2)

    def test_linked_list_random_node(self):
        module = load_module('python/382_LinkedListRandomNode.py', 'random_node')
        self.assertEqual(module.Solution(build_list([7])).getRandom(), 7)
        random.seed(1)
        self.assertIn(module.Solution(build_list([1, 2, 3])).getRandom(), {1, 2, 3})

    def test_ransom_note(self):
        module = load_module('python/383_RansomNote.py', 'ransom_note')
        self.assertFalse(module.Solution().canConstruct('aa', 'ab'))
        self.assertTrue(module.Solution().canConstruct('aa', 'aab'))

    def test_shuffle_an_array(self):
        module = load_module('python/384_ShuffleanArray.py', 'shuffle_array')
        nums = [1, 2, 3]
        obj = module.Solution(nums)
        random.seed(1)
        shuffled = obj.shuffle()
        self.assertEqual(sorted(shuffled), nums)
        self.assertEqual(obj.reset(), nums)

    def test_mini_parser(self):
        module = load_module('python/385_MiniParser.py', 'mini_parser')
        self.assertEqual(module.Solution().deserialize('324').getInteger(), 324)
        nested = module.Solution().deserialize('[123,[456,[789]]]')
        self.assertEqual(nested_to_list(nested), [123, [456, [789]]])

    def test_lexicographical_numbers(self):
        module = load_module('python/386_LexicographicalNumbers.py', 'lexical_numbers')
        self.assertEqual(module.Solution().lexicalOrder(13), [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_first_unique_character(self):
        module = load_module('python/387_FirstUniqueCharacterinaString.py', 'first_unique')
        self.assertEqual(module.Solution().firstUniqChar('leetcode'), 0)
        self.assertEqual(module.Solution().firstUniqChar('loveleetcode'), 2)
        self.assertEqual(module.Solution().firstUniqChar('aabb'), -1)

    def test_longest_absolute_file_path(self):
        module = load_module('python/388_LongestAbsoluteFilePath.py', 'file_path')
        path = 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
        self.assertEqual(module.Solution().lengthLongestPath(path), 20)

    def test_find_the_difference(self):
        module = load_module('python/389_FindtheDifference.py', 'find_difference')
        self.assertEqual(module.Solution().findTheDifference('abcd', 'abcde'), 'e')

    def test_elimination_game(self):
        module = load_module('python/390_EliminationGame.py', 'elimination_game')
        self.assertEqual(module.Solution().lastRemaining(9), 6)

    def test_perfect_rectangle(self):
        module = load_module('python/391_PerfectRectangle.py', 'perfect_rectangle')
        self.assertTrue(module.Solution().isRectangleCover([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]))
        self.assertFalse(module.Solution().isRectangleCover([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]]))

    def test_is_subsequence(self):
        module = load_module('python/392_IsSubsequence.py', 'subsequence')
        self.assertTrue(module.Solution().isSubsequence('abc', 'ahbgdc'))
        self.assertFalse(module.Solution().isSubsequence('axc', 'ahbgdc'))

    def test_utf8_validation(self):
        module = load_module('python/393_UTF8Validation.py', 'utf8')
        self.assertTrue(module.Solution().validUtf8([197, 130, 1]))
        self.assertFalse(module.Solution().validUtf8([235, 140, 4]))

    def test_decode_string(self):
        module = load_module('python/394_DecodeString.py', 'decode_string')
        self.assertEqual(module.Solution().decodeString('3[a]2[bc]'), 'aaabcbc')
        self.assertEqual(module.Solution().decodeString('3[a2[c]]'), 'accaccacc')

    def test_longest_substring_with_at_least_k_repeating(self):
        module = load_module('python/395_LongestSubstringwithAtLeastKRepeatingCharacters.py', 'longest_k')
        self.assertEqual(module.Solution().longestSubstring('aaabb', 3), 3)
        self.assertEqual(module.Solution().longestSubstring('ababbc', 2), 5)

    def test_rotate_function(self):
        module = load_module('python/396_RotateFunction.py', 'rotate_function')
        self.assertEqual(module.Solution().maxRotateFunction([4, 3, 2, 6]), 26)

    def test_integer_replacement(self):
        module = load_module('python/397_IntegerReplacement.py', 'integer_replacement')
        self.assertEqual(module.Solution().integerReplacement(8), 3)
        self.assertEqual(module.Solution().integerReplacement(7), 4)

    def test_random_pick_index(self):
        module = load_module('python/398_RandomPickIndex.py', 'random_pick')
        obj = module.Solution([1, 2, 3, 3, 3])
        self.assertEqual(obj.pick(1), 0)
        self.assertIn(obj.pick(3), {2, 3, 4})

    def test_evaluate_division(self):
        module = load_module('python/399_EvaluateDivision.py', 'evaluate_division')
        equations = [['a', 'b'], ['b', 'c']]
        values = [2.0, 3.0]
        queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]
        self.assertEqual(module.Solution().calcEquation(equations, values, queries), [6.0, 0.5, -1.0, 1.0, -1.0])

    def test_nth_digit(self):
        module = load_module('python/400_NthDigit.py', 'nth_digit')
        self.assertEqual(module.Solution().findNthDigit(3), 3)
        self.assertEqual(module.Solution().findNthDigit(11), 0)


if __name__ == '__main__':
    unittest.main()
