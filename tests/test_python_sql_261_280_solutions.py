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


class PythonSql261To280SolutionTest(unittest.TestCase):

    def test_graph_valid_tree(self):
        module = load_module('python/261_GraphValidTree.py', 'graph_valid_tree')
        self.assertTrue(module.Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
        self.assertFalse(module.Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

    def test_sql_trips_and_users(self):
        content = (ROOT / 'sql/262_TripsandUsers.sql').read_text().lower()
        for fragment in ['trips', 'users', 'request_at', 'cancellation rate', 'round']:
            self.assertIn(fragment, content)

    def test_ugly_number(self):
        module = load_module('python/263_UglyNumber.py', 'ugly_number')
        self.assertTrue(module.Solution().isUgly(6))
        self.assertTrue(module.Solution().isUgly(1))
        self.assertFalse(module.Solution().isUgly(14))

    def test_ugly_number_ii(self):
        module = load_module('python/264_UglyNumberII.py', 'ugly_number_ii')
        self.assertEqual(module.Solution().nthUglyNumber(10), 12)

    def test_paint_house_ii(self):
        module = load_module('python/265_PaintHouseII.py', 'paint_house_ii')
        self.assertEqual(module.Solution().minCostII([[1, 5, 3], [2, 9, 4]]), 5)

    def test_palindrome_permutation(self):
        module = load_module('python/266_PalindromePermutation.py', 'palindrome_perm')
        self.assertFalse(module.Solution().canPermutePalindrome('code'))
        self.assertTrue(module.Solution().canPermutePalindrome('aab'))

    def test_palindrome_permutation_ii(self):
        module = load_module('python/267_PalindromePermutationII.py', 'palindrome_perm_ii')
        self.assertEqual(sorted(module.Solution().generatePalindromes('aabb')), ['abba', 'baab'])
        self.assertEqual(module.Solution().generatePalindromes('abc'), [])

    def test_missing_number(self):
        module = load_module('python/268_MissingNumber.py', 'missing_number')
        self.assertEqual(module.Solution().missingNumber([3, 0, 1]), 2)

    def test_alien_dictionary(self):
        module = load_module('python/269_AlienDictionary.py', 'alien_dictionary')
        self.assertEqual(module.Solution().alienOrder(['wrt', 'wrf', 'er', 'ett', 'rftt']), 'wertf')
        self.assertEqual(module.Solution().alienOrder(['z', 'x', 'z']), '')

    def test_closest_binary_search_tree_value(self):
        module = load_module('python/270_ClosestBinarySearchTreeValue.py', 'closest_bst')
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(module.Solution().closestValue(root, 3.714286), 4)

    def test_encode_and_decode_strings(self):
        module = load_module('python/271_EncodeandDecodeStrings.py', 'codec')
        codec = module.Codec()
        strings = ['lint', 'code', 'love', 'you', '', '12#3']
        self.assertEqual(codec.decode(codec.encode(strings)), strings)

    def test_closest_binary_search_tree_value_ii(self):
        module = load_module('python/272_ClosestBinarySearchTreeValueII.py', 'closest_bst_ii')
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(sorted(module.Solution().closestKValues(root, 3.714286, 2)), [3, 4])

    def test_integer_to_english_words(self):
        module = load_module('python/273_IntegertoEnglishWords.py', 'english_words')
        self.assertEqual(module.Solution().numberToWords(123), 'One Hundred Twenty Three')
        self.assertEqual(module.Solution().numberToWords(12345), 'Twelve Thousand Three Hundred Forty Five')

    def test_h_index(self):
        module = load_module('python/274_HIndex.py', 'h_index')
        self.assertEqual(module.Solution().hIndex([3, 0, 6, 1, 5]), 3)

    def test_h_index_ii(self):
        module = load_module('python/275_HIndexII.py', 'h_index_ii')
        self.assertEqual(module.Solution().hIndex([0, 1, 3, 5, 6]), 3)

    def test_paint_fence(self):
        module = load_module('python/276_PaintFence.py', 'paint_fence')
        self.assertEqual(module.Solution().numWays(3, 2), 6)

    def test_find_the_celebrity(self):
        module = load_module('python/277_FindtheCelebrity.py', 'celebrity')
        matrix = [
            [False, True, True],
            [False, False, True],
            [False, False, False],
        ]
        module.knows = lambda a, b: matrix[a][b]
        self.assertEqual(module.Solution().findCelebrity(3), 2)

    def test_first_bad_version(self):
        module = load_module('python/278_FirstBadVersion.py', 'bad_version')
        module.isBadVersion = lambda version: version >= 4
        self.assertEqual(module.Solution().firstBadVersion(5), 4)

    def test_perfect_squares(self):
        module = load_module('python/279_PerfectSquares.py', 'perfect_squares')
        self.assertEqual(module.Solution().numSquares(12), 3)
        self.assertEqual(module.Solution().numSquares(13), 2)

    def test_wiggle_sort(self):
        module = load_module('python/280_WiggleSort.py', 'wiggle_sort')
        nums = [3, 5, 2, 1, 6, 4]
        module.Solution().wiggleSort(nums)
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                self.assertLessEqual(nums[i], nums[i + 1])
            else:
                self.assertGreaterEqual(nums[i], nums[i + 1])


if __name__ == '__main__':
    unittest.main()
