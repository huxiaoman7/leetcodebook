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
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Python361To380SolutionTest(unittest.TestCase):

    def test_bomb_enemy(self):
        module = load_module('python/361_BombEnemy.py', 'bomb_enemy')
        grid = [
            ['0', 'E', '0', '0'],
            ['E', '0', 'W', 'E'],
            ['0', 'E', '0', '0'],
        ]
        self.assertEqual(module.Solution().maxKilledEnemies(grid), 3)

    def test_design_hit_counter(self):
        module = load_module('python/362_DesignHitCounter.py', 'hit_counter')
        counter = module.HitCounter()
        counter.hit(1)
        counter.hit(2)
        counter.hit(3)
        self.assertEqual(counter.getHits(4), 3)
        counter.hit(300)
        self.assertEqual(counter.getHits(300), 4)
        self.assertEqual(counter.getHits(301), 3)

    def test_max_sum_submatrix(self):
        module = load_module('python/363_MaxSumofRectangleNoLargerThanK.py', 'max_sum_submatrix')
        matrix = [[1, 0, 1], [0, -2, 3]]
        self.assertEqual(module.Solution().maxSumSubmatrix(matrix, 2), 2)

    def test_nested_list_weight_sum_ii(self):
        module = load_module('python/364_NestedListWeightSumII.py', 'nested_weight_ii')
        nested = [
            NestedInteger([NestedInteger(1), NestedInteger(1)]),
            NestedInteger(2),
            NestedInteger([NestedInteger(1), NestedInteger(1)]),
        ]
        self.assertEqual(module.Solution().depthSumInverse(nested), 8)

    def test_water_and_jug_problem(self):
        module = load_module('python/365_WaterandJugProblem.py', 'water_jug')
        self.assertTrue(module.Solution().canMeasureWater(3, 5, 4))
        self.assertFalse(module.Solution().canMeasureWater(2, 6, 5))

    def test_find_leaves_of_binary_tree(self):
        module = load_module('python/366_FindLeavesofBinaryTree.py', 'find_leaves')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(module.Solution().findLeaves(root), [[4, 5, 3], [2], [1]])

    def test_valid_perfect_square(self):
        module = load_module('python/367_ValidPerfectSquare.py', 'perfect_square')
        self.assertTrue(module.Solution().isPerfectSquare(16))
        self.assertFalse(module.Solution().isPerfectSquare(14))

    def test_largest_divisible_subset(self):
        module = load_module('python/368_LargestDivisibleSubset.py', 'divisible_subset')
        result = module.Solution().largestDivisibleSubset([1, 2, 4, 8])
        self.assertEqual(result, [1, 2, 4, 8])

    def test_plus_one_linked_list(self):
        module = load_module('python/369_PlusOneLinkedList.py', 'plus_one_list')
        self.assertEqual(list_values(module.Solution().plusOne(build_list([1, 2, 3]))), [1, 2, 4])
        self.assertEqual(list_values(module.Solution().plusOne(build_list([9, 9]))), [1, 0, 0])

    def test_range_addition(self):
        module = load_module('python/370_RangeAddition.py', 'range_addition')
        updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
        self.assertEqual(module.Solution().getModifiedArray(5, updates), [-2, 0, 3, 5, 3])

    def test_sum_of_two_integers(self):
        module = load_module('python/371_SumofTwoIntegers.py', 'sum_two')
        self.assertEqual(module.Solution().getSum(1, 2), 3)
        self.assertEqual(module.Solution().getSum(-2, 3), 1)

    def test_super_pow(self):
        module = load_module('python/372_SuperPow.py', 'super_pow')
        self.assertEqual(module.Solution().superPow(2, [1, 0]), 1024)

    def test_find_k_pairs_with_smallest_sums(self):
        module = load_module('python/373_FindKPairswithSmallestSums.py', 'k_pairs')
        self.assertEqual(module.Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]])

    def test_guess_number_higher_or_lower(self):
        module = load_module('python/374_GuessNumberHigherorLower.py', 'guess_number')
        picked = 6
        module.guess = lambda num: 0 if num == picked else (-1 if num > picked else 1)
        self.assertEqual(module.Solution().guessNumber(10), 6)

    def test_guess_number_higher_or_lower_ii(self):
        module = load_module('python/375_GuessNumberHigherorLowerII.py', 'guess_number_ii')
        self.assertEqual(module.Solution().getMoneyAmount(10), 16)

    def test_wiggle_subsequence(self):
        module = load_module('python/376_WiggleSubsequence.py', 'wiggle')
        self.assertEqual(module.Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]), 6)
        self.assertEqual(module.Solution().wiggleMaxLength([1, 1, 1]), 1)

    def test_combination_sum_iv(self):
        module = load_module('python/377_CombinationSumIV.py', 'combination_sum_iv')
        self.assertEqual(module.Solution().combinationSum4([1, 2, 3], 4), 7)

    def test_kth_smallest_element_in_sorted_matrix(self):
        module = load_module('python/378_KthSmallestElementinaSortedMatrix.py', 'kth_matrix')
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        self.assertEqual(module.Solution().kthSmallest(matrix, 8), 13)

    def test_design_phone_directory(self):
        module = load_module('python/379_DesignPhoneDirectory.py', 'phone_directory')
        directory = module.PhoneDirectory(3)
        self.assertEqual(directory.get(), 0)
        self.assertEqual(directory.get(), 1)
        self.assertTrue(directory.check(2))
        self.assertEqual(directory.get(), 2)
        self.assertFalse(directory.check(2))
        directory.release(2)
        self.assertTrue(directory.check(2))

    def test_insert_delete_get_random(self):
        module = load_module('python/380_InsertDeleteGetRandomO1.py', 'randomized_set')
        random.seed(1)
        obj = module.RandomizedSet()
        self.assertTrue(obj.insert(1))
        self.assertFalse(obj.remove(2))
        self.assertTrue(obj.insert(2))
        self.assertIn(obj.getRandom(), {1, 2})
        self.assertTrue(obj.remove(1))
        self.assertFalse(obj.insert(2))
        self.assertEqual(obj.getRandom(), 2)


if __name__ == '__main__':
    unittest.main()
