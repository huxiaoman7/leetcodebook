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
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next


def list_values(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Python61To80SolutionTest(unittest.TestCase):

    def test_rotate_list(self):
        module = load_module('python/61_RotateList.py', 'rotate_list')
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(list_values(module.Solution().rotateRight(head, 2)), [4, 5, 1, 2, 3])

    def test_unique_paths(self):
        module = load_module('python/62_UniquePaths.py', 'unique_paths')
        self.assertEqual(module.Solution().uniquePaths(3, 7), 28)

    def test_unique_paths_ii(self):
        module = load_module('python/63_UniquePathsII.py', 'unique_paths_ii')
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(module.Solution().uniquePathsWithObstacles(grid), 2)

    def test_minimum_path_sum(self):
        module = load_module('python/64_MinimumPathSum.py', 'minimum_path_sum')
        self.assertEqual(module.Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]), 7)

    def test_valid_number(self):
        module = load_module('python/65_ValidNumber.py', 'valid_number')
        self.assertTrue(module.Solution().isNumber('0'))
        self.assertTrue(module.Solution().isNumber(' 0.1 '))
        self.assertTrue(module.Solution().isNumber('2e10'))
        self.assertFalse(module.Solution().isNumber('abc'))
        self.assertFalse(module.Solution().isNumber('1 a'))

    def test_plus_one(self):
        module = load_module('python/66_PlusOne.py', 'plus_one')
        self.assertEqual(module.Solution().plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(module.Solution().plusOne([9, 9]), [1, 0, 0])

    def test_add_binary(self):
        module = load_module('python/67_AddBinary.py', 'add_binary')
        self.assertEqual(module.Solution().addBinary('11', '1'), '100')
        self.assertEqual(module.Solution().addBinary('1010', '1011'), '10101')

    def test_text_justification(self):
        module = load_module('python/68_TextJustification.py', 'text_justification')
        words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification.']
        self.assertEqual(
            module.Solution().fullJustify(words, 16),
            ['This    is    an', 'example  of text', 'justification.  '],
        )

    def test_sqrtx(self):
        module = load_module('python/69_Sqrtx.py', 'sqrtx')
        self.assertEqual(module.Solution().mySqrt(4), 2)
        self.assertEqual(module.Solution().mySqrt(8), 2)

    def test_climbing_stairs(self):
        module = load_module('python/70_ClimbingStairs.py', 'climbing_stairs')
        self.assertEqual(module.Solution().climbStairs(2), 2)
        self.assertEqual(module.Solution().climbStairs(5), 8)

    def test_simplify_path(self):
        module = load_module('python/71_SimplifyPath.py', 'simplify_path')
        self.assertEqual(module.Solution().simplifyPath('/home/'), '/home')
        self.assertEqual(module.Solution().simplifyPath('/a/./b/../../c/'), '/c')

    def test_edit_distance(self):
        module = load_module('python/72_EditDistance.py', 'edit_distance')
        self.assertEqual(module.Solution().minDistance('horse', 'ros'), 3)
        self.assertEqual(module.Solution().minDistance('intention', 'execution'), 5)

    def test_set_matrix_zeroes(self):
        module = load_module('python/73_SetMatrixZeroes.py', 'set_matrix_zeroes')
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        module.Solution().setZeroes(matrix)
        self.assertEqual(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    def test_search_2d_matrix(self):
        module = load_module('python/74_Searcha2DMatrix.py', 'search_2d_matrix')
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        self.assertTrue(module.Solution().searchMatrix(matrix, 3))
        self.assertFalse(module.Solution().searchMatrix(matrix, 13))

    def test_sort_colors(self):
        module = load_module('python/75_SortColors.py', 'sort_colors')
        nums = [2, 0, 2, 1, 1, 0]
        module.Solution().sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_minimum_window_substring(self):
        module = load_module('python/76_MinimumWindowSubstring.py', 'minimum_window')
        self.assertEqual(module.Solution().minWindow('ADOBECODEBANC', 'ABC'), 'BANC')
        self.assertEqual(module.Solution().minWindow('a', 'aa'), '')

    def test_combinations(self):
        module = load_module('python/77_Combinations.py', 'combinations')
        result = module.Solution().combine(4, 2)
        self.assertEqual(sorted(result), sorted([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))

    def test_subsets(self):
        module = load_module('python/78_Subsets.py', 'subsets')
        result = module.Solution().subsets([1, 2, 3])
        self.assertEqual(len(result), 8)
        self.assertIn([1, 2, 3], result)

    def test_word_search(self):
        module = load_module('python/79_WordSearch.py', 'word_search')
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E'],
        ]
        self.assertTrue(module.Solution().exist(board, 'ABCCED'))
        self.assertFalse(module.Solution().exist(board, 'ABCB'))

    def test_remove_duplicates_from_sorted_array_ii(self):
        module = load_module('python/80_RemoveDuplicatesfromSortedArrayII.py', 'remove_dup_ii')
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        length = module.Solution().removeDuplicates(nums)
        self.assertEqual(length, 7)
        self.assertEqual(nums[:length], [0, 0, 1, 1, 2, 3, 3])


if __name__ == '__main__':
    unittest.main()
