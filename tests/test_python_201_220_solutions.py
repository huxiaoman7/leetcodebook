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


def list_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


class Python201To220SolutionTest(unittest.TestCase):

    def assert_valid_course_order(self, order, num_courses, prerequisites):
        self.assertEqual(len(order), num_courses)
        positions = {course: index for index, course in enumerate(order)}
        for course, pre in prerequisites:
            self.assertLess(positions[pre], positions[course])

    def test_bitwise_and_of_numbers_range(self):
        module = load_module('python/201_BitwiseANDofNumbersRange.py', 'range_and')
        self.assertEqual(module.Solution().rangeBitwiseAnd(5, 7), 4)
        self.assertEqual(module.Solution().rangeBitwiseAnd(0, 1), 0)

    def test_happy_number(self):
        module = load_module('python/202_HappyNumber.py', 'happy_number')
        self.assertTrue(module.Solution().isHappy(19))
        self.assertFalse(module.Solution().isHappy(2))

    def test_remove_linked_list_elements(self):
        module = load_module('python/203_RemoveLinkedListElements.py', 'remove_list')
        self.assertEqual(list_values(module.Solution().removeElements(build_list([1, 2, 6, 3, 4, 5, 6]), 6)), [1, 2, 3, 4, 5])
        self.assertIsNone(module.Solution().removeElements(build_list([7, 7, 7]), 7))

    def test_count_primes(self):
        module = load_module('python/204_CountPrimes.py', 'count_primes')
        self.assertEqual(module.Solution().countPrimes(10), 4)
        self.assertEqual(module.Solution().countPrimes(0), 0)

    def test_isomorphic_strings(self):
        module = load_module('python/205_IsomorphicStrings.py', 'isomorphic')
        self.assertTrue(module.Solution().isIsomorphic('egg', 'add'))
        self.assertFalse(module.Solution().isIsomorphic('foo', 'bar'))
        self.assertFalse(module.Solution().isIsomorphic('badc', 'baba'))

    def test_reverse_linked_list(self):
        module = load_module('python/206_ReverseLinkedList.py', 'reverse_list')
        self.assertEqual(list_values(module.Solution().reverseList(build_list([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])

    def test_course_schedule(self):
        module = load_module('python/207_CourseSchedule.py', 'course_schedule')
        self.assertTrue(module.Solution().canFinish(2, [[1, 0]]))
        self.assertFalse(module.Solution().canFinish(2, [[1, 0], [0, 1]]))

    def test_implement_trie(self):
        module = load_module('python/208_ImplementTrie.py', 'trie')
        trie = module.Trie()
        trie.insert('apple')
        self.assertTrue(trie.search('apple'))
        self.assertFalse(trie.search('app'))
        self.assertTrue(trie.startsWith('app'))
        trie.insert('app')
        self.assertTrue(trie.search('app'))

    def test_minimum_size_subarray_sum(self):
        module = load_module('python/209_MinimumSizeSubarraySum.py', 'min_subarray')
        self.assertEqual(module.Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)
        self.assertEqual(module.Solution().minSubArrayLen(100, [1, 2, 3]), 0)

    def test_course_schedule_ii(self):
        module = load_module('python/210_CourseScheduleII.py', 'course_schedule_ii')
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        order = module.Solution().findOrder(4, prerequisites)
        self.assert_valid_course_order(order, 4, prerequisites)
        self.assertEqual(module.Solution().findOrder(2, [[1, 0], [0, 1]]), [])

    def test_add_and_search_word(self):
        module = load_module('python/211_AddandSearchWord.py', 'word_dictionary')
        dictionary = module.WordDictionary()
        dictionary.addWord('bad')
        dictionary.addWord('dad')
        dictionary.addWord('mad')
        self.assertFalse(dictionary.search('pad'))
        self.assertTrue(dictionary.search('bad'))
        self.assertTrue(dictionary.search('.ad'))
        self.assertTrue(dictionary.search('b..'))

    def test_word_search_ii(self):
        module = load_module('python/212_WordSearchII.py', 'word_search_ii')
        board = [
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v'],
        ]
        result = module.Solution().findWords(board, ['oath', 'pea', 'eat', 'rain'])
        self.assertEqual(sorted(result), ['eat', 'oath'])

    def test_house_robber_ii(self):
        module = load_module('python/213_HouseRobberII.py', 'house_robber_ii')
        self.assertEqual(module.Solution().rob([2, 3, 2]), 3)
        self.assertEqual(module.Solution().rob([1, 2, 3, 1]), 4)

    def test_shortest_palindrome(self):
        module = load_module('python/214_ShortestPalindrome.py', 'shortest_palindrome')
        self.assertEqual(module.Solution().shortestPalindrome('aacecaaa'), 'aaacecaaa')
        self.assertEqual(module.Solution().shortestPalindrome('abcd'), 'dcbabcd')

    def test_kth_largest_element(self):
        module = load_module('python/215_KthLargestElementinanArray.py', 'kth_largest')
        self.assertEqual(module.Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_combination_sum_iii(self):
        module = load_module('python/216_CombinationSumIII.py', 'combination_sum_iii')
        self.assertEqual(module.Solution().combinationSum3(3, 7), [[1, 2, 4]])
        self.assertEqual(
            sorted(module.Solution().combinationSum3(3, 9)),
            [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
        )

    def test_contains_duplicate(self):
        module = load_module('python/217_ContainsDuplicate.py', 'contains_duplicate')
        self.assertTrue(module.Solution().containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(module.Solution().containsDuplicate([1, 2, 3, 4]))

    def test_the_skyline_problem(self):
        module = load_module('python/218_TheSkylineProblem.py', 'skyline')
        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
        self.assertEqual(module.Solution().getSkyline(buildings), [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])

    def test_contains_duplicate_ii(self):
        module = load_module('python/219_ContainsDuplicateII.py', 'contains_duplicate_ii')
        self.assertTrue(module.Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
        self.assertTrue(module.Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
        self.assertFalse(module.Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))

    def test_contains_duplicate_iii(self):
        module = load_module('python/220_ContainsDuplicateIII.py', 'contains_duplicate_iii')
        self.assertTrue(module.Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
        self.assertFalse(module.Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))


if __name__ == '__main__':
    unittest.main()
