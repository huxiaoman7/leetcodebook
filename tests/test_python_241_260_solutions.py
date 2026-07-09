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


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Python241To260SolutionTest(unittest.TestCase):

    def test_different_ways_to_add_parentheses(self):
        module = load_module('python/241_DifferentWaystoAddParentheses.py', 'diff_parentheses')
        self.assertEqual(sorted(module.Solution().diffWaysToCompute('2-1-1')), [0, 2])
        self.assertEqual(sorted(module.Solution().diffWaysToCompute('2*3-4*5')), [-34, -14, -10, -10, 10])

    def test_valid_anagram(self):
        module = load_module('python/242_ValidAnagram.py', 'valid_anagram')
        self.assertTrue(module.Solution().isAnagram('anagram', 'nagaram'))
        self.assertFalse(module.Solution().isAnagram('rat', 'car'))

    def test_shortest_word_distance(self):
        module = load_module('python/243_ShortestWordDistance.py', 'shortest_word')
        words = ['practice', 'makes', 'perfect', 'coding', 'makes']
        self.assertEqual(module.Solution().shortestDistance(words, 'coding', 'practice'), 3)
        self.assertEqual(module.Solution().shortestDistance(words, 'makes', 'coding'), 1)

    def test_shortest_word_distance_ii(self):
        module = load_module('python/244_ShortestWordDistanceII.py', 'shortest_word_ii')
        obj = module.WordDistance(['practice', 'makes', 'perfect', 'coding', 'makes'])
        self.assertEqual(obj.shortest('coding', 'practice'), 3)
        self.assertEqual(obj.shortest('makes', 'coding'), 1)

    def test_shortest_word_distance_iii(self):
        module = load_module('python/245_ShortestWordDistanceIII.py', 'shortest_word_iii')
        words = ['practice', 'makes', 'perfect', 'coding', 'makes']
        self.assertEqual(module.Solution().shortestWordDistance(words, 'makes', 'makes'), 3)
        self.assertEqual(module.Solution().shortestWordDistance(words, 'coding', 'practice'), 3)

    def test_strobogrammatic_number(self):
        module = load_module('python/246_StrobogrammaticNumber.py', 'strobogrammatic')
        self.assertTrue(module.Solution().isStrobogrammatic('69'))
        self.assertFalse(module.Solution().isStrobogrammatic('962'))

    def test_strobogrammatic_number_ii(self):
        module = load_module('python/247_StrobogrammaticNumberII.py', 'strobogrammatic_ii')
        self.assertEqual(sorted(module.Solution().findStrobogrammatic(2)), ['11', '69', '88', '96'])

    def test_strobogrammatic_number_iii(self):
        module = load_module('python/248_StrobogrammaticNumberIII.py', 'strobogrammatic_iii')
        self.assertEqual(module.Solution().strobogrammaticInRange('50', '100'), 3)

    def test_group_shifted_strings(self):
        module = load_module('python/249_GroupShiftedStrings.py', 'group_shifted')
        result = [sorted(group) for group in module.Solution().groupStrings(['abc', 'bcd', 'acef', 'xyz', 'az', 'ba', 'a', 'z'])]
        self.assertEqual(sorted(result), sorted([['abc', 'bcd', 'xyz'], ['acef'], ['az', 'ba'], ['a', 'z']]))

    def test_count_univalue_subtrees(self):
        module = load_module('python/250_CountUnivalueSubtrees.py', 'univalue')
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(5)
        self.assertEqual(module.Solution().countUnivalSubtrees(root), 4)

    def test_flatten_2d_vector(self):
        module = load_module('python/251_Flatten2DVector.py', 'vector2d')
        iterator = module.Vector2D([[1, 2], [], [3]])
        result = []
        while iterator.hasNext():
            result.append(iterator.next())
        self.assertEqual(result, [1, 2, 3])

    def test_meeting_rooms(self):
        module = load_module('python/252_MeetingRooms.py', 'meeting_rooms')
        self.assertFalse(module.Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]))
        self.assertTrue(module.Solution().canAttendMeetings([[7, 10], [2, 4]]))

    def test_meeting_rooms_ii(self):
        module = load_module('python/253_MeetingRoomsII.py', 'meeting_rooms_ii')
        self.assertEqual(module.Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEqual(module.Solution().minMeetingRooms([[7, 10], [2, 4]]), 1)

    def test_factor_combinations(self):
        module = load_module('python/254_FactorCombinations.py', 'factor_combinations')
        self.assertEqual(sorted(module.Solution().getFactors(12)), [[2, 2, 3], [2, 6], [3, 4]])

    def test_verify_preorder_sequence_in_bst(self):
        module = load_module('python/255_VerifyPreorderSequenceinBinarySearchTree.py', 'verify_preorder')
        self.assertFalse(module.Solution().verifyPreorder([5, 2, 6, 1, 3]))
        self.assertTrue(module.Solution().verifyPreorder([5, 2, 1, 3, 6]))

    def test_paint_house(self):
        module = load_module('python/256_PaintHouse.py', 'paint_house')
        self.assertEqual(module.Solution().minCost([[17, 2, 17], [16, 16, 5], [14, 3, 19]]), 10)

    def test_binary_tree_paths(self):
        module = load_module('python/257_BinaryTreePaths.py', 'tree_paths')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        self.assertEqual(sorted(module.Solution().binaryTreePaths(root)), ['1->2->5', '1->3'])

    def test_add_digits(self):
        module = load_module('python/258_AddDigits.py', 'add_digits')
        self.assertEqual(module.Solution().addDigits(38), 2)
        self.assertEqual(module.Solution().addDigits(0), 0)

    def test_three_sum_smaller(self):
        module = load_module('python/259_3SumSmaller.py', 'three_sum_smaller')
        self.assertEqual(module.Solution().threeSumSmaller([-2, 0, 1, 3], 2), 2)

    def test_single_number_iii(self):
        module = load_module('python/260_SingleNumberIII.py', 'single_number_iii')
        self.assertEqual(sorted(module.Solution().singleNumber([1, 2, 1, 3, 2, 5])), [3, 5])


if __name__ == '__main__':
    unittest.main()
