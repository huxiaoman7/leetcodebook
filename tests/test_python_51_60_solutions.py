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


class Python51To60SolutionTest(unittest.TestCase):

    def test_n_queens(self):
        module = load_module('python/51_NQueens.py', 'n_queens')
        result = module.Solution().solveNQueens(4)
        self.assertEqual(len(result), 2)
        self.assertIn(['.Q..', '...Q', 'Q...', '..Q.'], result)

    def test_n_queens_ii(self):
        module = load_module('python/52_NQueensII.py', 'n_queens_ii')
        self.assertEqual(module.Solution().totalNQueens(4), 2)
        self.assertEqual(module.Solution().totalNQueens(1), 1)

    def test_maximum_subarray(self):
        module = load_module('python/53_MaximumSubarray.py', 'maximum_subarray')
        self.assertEqual(module.Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_spiral_matrix(self):
        module = load_module('python/54_SpiralMatrix.py', 'spiral_matrix')
        self.assertEqual(module.Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_jump_game(self):
        module = load_module('python/55_JumpGame.py', 'jump_game')
        self.assertTrue(module.Solution().canJump([2, 3, 1, 1, 4]))
        self.assertFalse(module.Solution().canJump([3, 2, 1, 0, 4]))

    def test_merge_intervals(self):
        module = load_module('python/56_MergeIntervals.py', 'merge_intervals')
        self.assertEqual(module.Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]), [[1, 6], [8, 10], [15, 18]])

    def test_insert_interval(self):
        module = load_module('python/57_InsertInterval.py', 'insert_interval')
        self.assertEqual(module.Solution().insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])

    def test_length_of_last_word(self):
        module = load_module('python/58_LengthofLastWord.py', 'length_last_word')
        self.assertEqual(module.Solution().lengthOfLastWord('Hello World'), 5)
        self.assertEqual(module.Solution().lengthOfLastWord('a '), 1)

    def test_spiral_matrix_ii(self):
        module = load_module('python/59_SpiralMatrixII.py', 'spiral_matrix_ii')
        self.assertEqual(module.Solution().generateMatrix(3), [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

    def test_permutation_sequence(self):
        module = load_module('python/60_PermutationSequence.py', 'permutation_sequence')
        self.assertEqual(module.Solution().getPermutation(3, 3), '213')
        self.assertEqual(module.Solution().getPermutation(4, 9), '2314')


if __name__ == '__main__':
    unittest.main()
