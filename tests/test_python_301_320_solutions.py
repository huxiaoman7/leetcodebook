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


class Python301To320SolutionTest(unittest.TestCase):

    def test_remove_invalid_parentheses(self):
        module = load_module('python/301_RemoveInvalidParentheses.py', 'remove_invalid')
        self.assertEqual(sorted(module.Solution().removeInvalidParentheses('()())()')), ['(())()', '()()()'])

    def test_smallest_rectangle_enclosing_black_pixels(self):
        module = load_module('python/302_SmallestRectangleEnclosingBlackPixels.py', 'smallest_rect')
        image = [['0', '0', '1', '0'], ['0', '1', '1', '0'], ['0', '1', '0', '0']]
        self.assertEqual(module.Solution().minArea(image, 0, 2), 6)

    def test_range_sum_query_immutable(self):
        module = load_module('python/303_RangeSumQueryImmutable.py', 'range_sum')
        nums = module.NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(nums.sumRange(0, 2), 1)
        self.assertEqual(nums.sumRange(2, 5), -1)
        self.assertEqual(nums.sumRange(0, 5), -3)

    def test_range_sum_query_2d_immutable(self):
        module = load_module('python/304_RangeSumQuery2DImmutable.py', 'range_sum_2d')
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
        obj = module.NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(obj.sumRegion(1, 1, 2, 2), 11)

    def test_number_of_islands_ii(self):
        module = load_module('python/305_NumberofIslandsII.py', 'islands_ii')
        self.assertEqual(module.Solution().numIslands2(3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]), [1, 1, 2, 3])

    def test_additive_number(self):
        module = load_module('python/306_AdditiveNumber.py', 'additive')
        self.assertTrue(module.Solution().isAdditiveNumber('112358'))
        self.assertTrue(module.Solution().isAdditiveNumber('199100199'))
        self.assertFalse(module.Solution().isAdditiveNumber('1023'))

    def test_range_sum_query_mutable(self):
        module = load_module('python/307_RangeSumQueryMutable.py', 'range_sum_mutable')
        nums = module.NumArray([1, 3, 5])
        self.assertEqual(nums.sumRange(0, 2), 9)
        nums.update(1, 2)
        self.assertEqual(nums.sumRange(0, 2), 8)

    def test_range_sum_query_2d_mutable(self):
        module = load_module('python/308_RangeSumQuery2DMutable.py', 'range_sum_2d_mutable')
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
        obj = module.NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(2, 1, 4, 3), 8)
        obj.update(3, 2, 2)
        self.assertEqual(obj.sumRegion(2, 1, 4, 3), 10)

    def test_best_time_to_buy_and_sell_stock_with_cooldown(self):
        module = load_module('python/309_BestTimetoBuyandSellStockwithCooldown.py', 'stock_cooldown')
        self.assertEqual(module.Solution().maxProfit([1, 2, 3, 0, 2]), 3)

    def test_minimum_height_trees(self):
        module = load_module('python/310_MinimumHeightTrees.py', 'mht')
        self.assertEqual(sorted(module.Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]])), [1])
        self.assertEqual(sorted(module.Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])), [3, 4])

    def test_sparse_matrix_multiplication(self):
        module = load_module('python/311_SparseMatrixMultiplication.py', 'sparse_matrix')
        mat1 = [[1, 0, 0], [-1, 0, 3]]
        mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
        self.assertEqual(module.Solution().multiply(mat1, mat2), [[7, 0, 0], [-7, 0, 3]])

    def test_burst_balloons(self):
        module = load_module('python/312_BurstBalloons.py', 'burst_balloons')
        self.assertEqual(module.Solution().maxCoins([3, 1, 5, 8]), 167)

    def test_super_ugly_number(self):
        module = load_module('python/313_SuperUglyNumber.py', 'super_ugly')
        self.assertEqual(module.Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]), 32)

    def test_binary_tree_vertical_order_traversal(self):
        module = load_module('python/314_BinaryTreeVerticalOrderTraversal.py', 'vertical_order')
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(module.Solution().verticalOrder(root), [[9], [3, 15], [20], [7]])

    def test_count_of_smaller_numbers_after_self(self):
        module = load_module('python/315_CountofSmallerNumbersAfterSelf.py', 'count_smaller')
        self.assertEqual(module.Solution().countSmaller([5, 2, 6, 1]), [2, 1, 1, 0])

    def test_remove_duplicate_letters(self):
        module = load_module('python/316_RemoveDuplicateLetters.py', 'remove_duplicate')
        self.assertEqual(module.Solution().removeDuplicateLetters('bcabc'), 'abc')
        self.assertEqual(module.Solution().removeDuplicateLetters('cbacdcbc'), 'acdb')

    def test_shortest_distance_from_all_buildings(self):
        module = load_module('python/317_ShortestDistancefromAllBuildings.py', 'shortest_buildings')
        grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
        self.assertEqual(module.Solution().shortestDistance(grid), 7)

    def test_maximum_product_of_word_lengths(self):
        module = load_module('python/318_MaximumProductofWordLengths.py', 'word_lengths')
        self.assertEqual(module.Solution().maxProduct(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef']), 16)

    def test_bulb_switcher(self):
        module = load_module('python/319_BulbSwitcher.py', 'bulb_switcher')
        self.assertEqual(module.Solution().bulbSwitch(3), 1)

    def test_generalized_abbreviation(self):
        module = load_module('python/320_GeneralizedAbbreviation.py', 'abbreviation')
        result = module.Solution().generateAbbreviations('word')
        self.assertEqual(len(result), 16)
        self.assertIn('4', result)
        self.assertIn('w1r1', result)


if __name__ == '__main__':
    unittest.main()
