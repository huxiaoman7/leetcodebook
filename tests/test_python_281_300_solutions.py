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


class SimpleIterator(object):

    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def hasNext(self):
        return self.index < len(self.nums)

    def next(self):
        value = self.nums[self.index]
        self.index += 1
        return value


class Python281To300SolutionTest(unittest.TestCase):

    def test_zigzag_iterator(self):
        module = load_module('python/281_ZigzagIterator.py', 'zigzag_iterator')
        iterator = module.ZigzagIterator([1, 2], [3, 4, 5, 6])
        result = []
        while iterator.hasNext():
            result.append(iterator.next())
        self.assertEqual(result, [1, 3, 2, 4, 5, 6])

    def test_expression_add_operators(self):
        module = load_module('python/282_ExpressionAddOperators.py', 'expression_add')
        self.assertEqual(sorted(module.Solution().addOperators('123', 6)), ['1*2*3', '1+2+3'])
        self.assertEqual(sorted(module.Solution().addOperators('105', 5)), ['1*0+5', '10-5'])

    def test_move_zeroes(self):
        module = load_module('python/283_MoveZeroes.py', 'move_zeroes')
        nums = [0, 1, 0, 3, 12]
        module.Solution().moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_peeking_iterator(self):
        module = load_module('python/284_PeekingIterator.py', 'peeking_iterator')
        iterator = module.PeekingIterator(SimpleIterator([1, 2, 3]))
        self.assertEqual(iterator.peek(), 1)
        self.assertEqual(iterator.next(), 1)
        self.assertEqual(iterator.next(), 2)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 3)
        self.assertFalse(iterator.hasNext())

    def test_inorder_successor_in_bst(self):
        module = load_module('python/285_InorderSuccessorinBST.py', 'successor')
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        self.assertEqual(module.Solution().inorderSuccessor(root, root.left).val, 4)
        self.assertEqual(module.Solution().inorderSuccessor(root, root.right), None)

    def test_walls_and_gates(self):
        module = load_module('python/286_WallsandGates.py', 'walls_gates')
        inf = 2147483647
        rooms = [
            [inf, -1, 0, inf],
            [inf, inf, inf, -1],
            [inf, -1, inf, -1],
            [0, -1, inf, inf],
        ]
        module.Solution().wallsAndGates(rooms)
        self.assertEqual(rooms, [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ])

    def test_find_duplicate_number(self):
        module = load_module('python/287_FindtheDuplicateNumber.py', 'find_duplicate')
        self.assertEqual(module.Solution().findDuplicate([1, 3, 4, 2, 2]), 2)

    def test_unique_word_abbreviation(self):
        module = load_module('python/288_UniqueWordAbbreviation.py', 'valid_word_abbr')
        dictionary = module.ValidWordAbbr(['deer', 'door', 'cake', 'card'])
        self.assertFalse(dictionary.isUnique('dear'))
        self.assertTrue(dictionary.isUnique('cart'))
        self.assertFalse(dictionary.isUnique('cane'))
        self.assertTrue(dictionary.isUnique('make'))

    def test_game_of_life(self):
        module = load_module('python/289_GameofLife.py', 'game_life')
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        module.Solution().gameOfLife(board)
        self.assertEqual(board, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]])

    def test_word_pattern(self):
        module = load_module('python/290_WordPattern.py', 'word_pattern')
        self.assertTrue(module.Solution().wordPattern('abba', 'dog cat cat dog'))
        self.assertFalse(module.Solution().wordPattern('abba', 'dog cat cat fish'))

    def test_word_pattern_ii(self):
        module = load_module('python/291_WordPatternII.py', 'word_pattern_ii')
        self.assertTrue(module.Solution().wordPatternMatch('abab', 'redblueredblue'))
        self.assertFalse(module.Solution().wordPatternMatch('aabb', 'xyzabcxzyabc'))

    def test_nim_game(self):
        module = load_module('python/292_NimGame.py', 'nim_game')
        self.assertFalse(module.Solution().canWinNim(4))
        self.assertTrue(module.Solution().canWinNim(5))

    def test_flip_game(self):
        module = load_module('python/293_FlipGame.py', 'flip_game')
        self.assertEqual(sorted(module.Solution().generatePossibleNextMoves('++++')), ['++--', '+--+', '--++'])

    def test_flip_game_ii(self):
        module = load_module('python/294_FlipGameII.py', 'flip_game_ii')
        self.assertTrue(module.Solution().canWin('++++'))

    def test_find_median_from_data_stream(self):
        module = load_module('python/295_FindMedianfromDataStream.py', 'median_finder')
        finder = module.MedianFinder()
        finder.addNum(1)
        finder.addNum(2)
        self.assertEqual(finder.findMedian(), 1.5)
        finder.addNum(3)
        self.assertEqual(finder.findMedian(), 2)

    def test_best_meeting_point(self):
        module = load_module('python/296_BestMeetingPoint.py', 'meeting_point')
        grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
        self.assertEqual(module.Solution().minTotalDistance(grid), 6)

    def test_serialize_and_deserialize_binary_tree(self):
        module = load_module('python/297_SerializeandDeserializeBinaryTree.py', 'codec_tree')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        codec = module.Codec()
        restored = codec.deserialize(codec.serialize(root))
        self.assertEqual(codec.serialize(restored), codec.serialize(root))

    def test_binary_tree_longest_consecutive_sequence(self):
        module = load_module('python/298_BinaryTreeLongestConsecutiveSequence.py', 'longest_consecutive')
        root = TreeNode(1)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(5)
        self.assertEqual(module.Solution().longestConsecutive(root), 3)

    def test_bulls_and_cows(self):
        module = load_module('python/299_BullsandCows.py', 'bulls_cows')
        self.assertEqual(module.Solution().getHint('1807', '7810'), '1A3B')
        self.assertEqual(module.Solution().getHint('1123', '0111'), '1A1B')

    def test_longest_increasing_subsequence(self):
        module = load_module('python/300_LongestIncreasingSubsequence.py', 'lis')
        self.assertEqual(module.Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)


if __name__ == '__main__':
    unittest.main()
