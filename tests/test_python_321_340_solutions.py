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


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class NestedInteger(object):

    def __init__(self, value):
        self.value = value

    def isInteger(self):
        return isinstance(self.value, int)

    def getInteger(self):
        return self.value if self.isInteger() else None

    def getList(self):
        return self.value if not self.isInteger() else None


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


class Python321To340SolutionTest(unittest.TestCase):

    def test_create_maximum_number(self):
        module = load_module('python/321_CreateMaximumNumber.py', 'create_max_number')
        self.assertEqual(module.Solution().maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5), [9, 8, 6, 5, 3])

    def test_coin_change(self):
        module = load_module('python/322_CoinChange.py', 'coin_change')
        self.assertEqual(module.Solution().coinChange([1, 2, 5], 11), 3)
        self.assertEqual(module.Solution().coinChange([2], 3), -1)

    def test_number_of_connected_components(self):
        module = load_module('python/323_NumberofConnectedComponentsinanUndirectedGraph.py', 'components')
        self.assertEqual(module.Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]), 2)

    def test_wiggle_sort_ii(self):
        module = load_module('python/324_WiggleSortII.py', 'wiggle_ii')
        nums = [1, 5, 1, 1, 6, 4]
        module.Solution().wiggleSort(nums)
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                self.assertLess(nums[i], nums[i + 1])
            else:
                self.assertGreater(nums[i], nums[i + 1])
        self.assertEqual(sorted(nums), [1, 1, 1, 4, 5, 6])

    def test_maximum_size_subarray_sum_equals_k(self):
        module = load_module('python/325_MaximumSizeSubarraySumEqualsk.py', 'max_subarray_len')
        self.assertEqual(module.Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3), 4)
        self.assertEqual(module.Solution().maxSubArrayLen([-2, -1, 2, 1], 1), 2)

    def test_power_of_three(self):
        module = load_module('python/326_PowerofThree.py', 'power_three')
        self.assertTrue(module.Solution().isPowerOfThree(27))
        self.assertFalse(module.Solution().isPowerOfThree(45))

    def test_count_of_range_sum(self):
        module = load_module('python/327_CountofRangeSum.py', 'range_sum_count')
        self.assertEqual(module.Solution().countRangeSum([-2, 5, -1], -2, 2), 3)

    def test_odd_even_linked_list(self):
        module = load_module('python/328_OddEvenLinkedList.py', 'odd_even')
        self.assertEqual(list_values(module.Solution().oddEvenList(build_list([1, 2, 3, 4, 5]))), [1, 3, 5, 2, 4])

    def test_longest_increasing_path_in_matrix(self):
        module = load_module('python/329_LongestIncreasingPathinaMatrix.py', 'longest_path')
        self.assertEqual(module.Solution().longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)

    def test_patching_array(self):
        module = load_module('python/330_PatchingArray.py', 'patching_array')
        self.assertEqual(module.Solution().minPatches([1, 3], 6), 1)
        self.assertEqual(module.Solution().minPatches([1, 5, 10], 20), 2)

    def test_verify_preorder_serialization(self):
        module = load_module('python/331_VerifyPreorderSerializationofaBinaryTree.py', 'verify_serialization')
        self.assertTrue(module.Solution().isValidSerialization('9,3,4,#,#,1,#,#,2,#,6,#,#'))
        self.assertFalse(module.Solution().isValidSerialization('1,#'))

    def test_reconstruct_itinerary(self):
        module = load_module('python/332_ReconstructItinerary.py', 'itinerary')
        tickets = [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]
        self.assertEqual(module.Solution().findItinerary(tickets), ['JFK', 'MUC', 'LHR', 'SFO', 'SJC'])

    def test_largest_bst_subtree(self):
        module = load_module('python/333_LargestBSTSubtree.py', 'largest_bst')
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(8)
        root.right.right = TreeNode(7)
        self.assertEqual(module.Solution().largestBSTSubtree(root), 3)

    def test_increasing_triplet_subsequence(self):
        module = load_module('python/334_IncreasingTripletSubsequence.py', 'triplet')
        self.assertTrue(module.Solution().increasingTriplet([1, 2, 3, 4, 5]))
        self.assertFalse(module.Solution().increasingTriplet([5, 4, 3, 2, 1]))

    def test_self_crossing(self):
        module = load_module('python/335_SelfCrossing.py', 'self_crossing')
        self.assertTrue(module.Solution().isSelfCrossing([2, 1, 1, 2]))
        self.assertFalse(module.Solution().isSelfCrossing([1, 2, 3, 4]))

    def test_palindrome_pairs(self):
        module = load_module('python/336_PalindromePairs.py', 'palindrome_pairs')
        result = sorted(module.Solution().palindromePairs(['abcd', 'dcba', 'lls', 's', 'sssll']))
        self.assertEqual(result, [[0, 1], [1, 0], [2, 4], [3, 2]])

    def test_house_robber_iii(self):
        module = load_module('python/337_HouseRobberIII.py', 'house_robber_iii')
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(1)
        self.assertEqual(module.Solution().rob(root), 7)

    def test_counting_bits(self):
        module = load_module('python/338_CountingBits.py', 'counting_bits')
        self.assertEqual(module.Solution().countBits(5), [0, 1, 1, 2, 1, 2])

    def test_nested_list_weight_sum(self):
        module = load_module('python/339_NestedListWeightSum.py', 'nested_weight')
        nested = [
            NestedInteger([NestedInteger(1), NestedInteger(1)]),
            NestedInteger(2),
            NestedInteger([NestedInteger(1), NestedInteger(1)]),
        ]
        self.assertEqual(module.Solution().depthSum(nested), 10)

    def test_longest_substring_with_at_most_k_distinct(self):
        module = load_module('python/340_LongestSubstringwithAtMostKDistinctCharacters.py', 'k_distinct')
        self.assertEqual(module.Solution().lengthOfLongestSubstringKDistinct('eceba', 2), 3)
        self.assertEqual(module.Solution().lengthOfLongestSubstringKDistinct('aa', 1), 2)


if __name__ == '__main__':
    unittest.main()
