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


class RandomListNode(object):

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Python121To140SolutionTest(unittest.TestCase):

    def test_best_time_to_buy_sell_stock(self):
        module = load_module('python/121_BestTimetoBuyandSellStock.py', 'stock_i')
        self.assertEqual(module.Solution().maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(module.Solution().maxProfit([7, 6, 4, 3, 1]), 0)

    def test_best_time_to_buy_sell_stock_ii(self):
        module = load_module('python/122_BestTimetoBuyandSellStockII.py', 'stock_ii')
        self.assertEqual(module.Solution().maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_best_time_to_buy_sell_stock_iii(self):
        module = load_module('python/123_BestTimetoBuyandSellStockIII.py', 'stock_iii')
        self.assertEqual(module.Solution().maxProfit([3, 3, 5, 0, 0, 3, 1, 4]), 6)

    def test_binary_tree_maximum_path_sum(self):
        module = load_module('python/124_BinaryTreeMaximumPathSum.py', 'max_path_sum')
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(module.Solution().maxPathSum(root), 42)

    def test_valid_palindrome(self):
        module = load_module('python/125_ValidPalindrome.py', 'valid_palindrome')
        self.assertTrue(module.Solution().isPalindrome('A man, a plan, a canal: Panama'))
        self.assertFalse(module.Solution().isPalindrome('race a car'))

    def test_word_ladder_ii(self):
        module = load_module('python/126_WordLadderII.py', 'word_ladder_ii')
        result = module.Solution().findLadders('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
        expected = [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
        self.assertEqual(sorted(result), sorted(expected))

    def test_word_ladder(self):
        module = load_module('python/127_WordLadder.py', 'word_ladder')
        self.assertEqual(module.Solution().ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']), 5)
        self.assertEqual(module.Solution().ladderLength('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']), 0)

    def test_longest_consecutive_sequence(self):
        module = load_module('python/128_LongestConsecutiveSequence.py', 'longest_consecutive')
        self.assertEqual(module.Solution().longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_sum_root_to_leaf_numbers(self):
        module = load_module('python/129_SumRoottoLeafNumbers.py', 'sum_root_leaf')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(module.Solution().sumNumbers(root), 25)

    def test_surrounded_regions(self):
        module = load_module('python/130_SurroundedRegions.py', 'surrounded_regions')
        board = [
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X'],
        ]
        module.Solution().solve(board)
        self.assertEqual(board, [
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X'],
        ])

    def test_palindrome_partitioning(self):
        module = load_module('python/131_PalindromePartitioning.py', 'pal_partition')
        self.assertEqual(sorted(module.Solution().partition('aab')), sorted([['a', 'a', 'b'], ['aa', 'b']]))

    def test_palindrome_partitioning_ii(self):
        module = load_module('python/132_PalindromePartitioningII.py', 'pal_partition_ii')
        self.assertEqual(module.Solution().minCut('aab'), 1)

    def test_clone_graph(self):
        module = load_module('python/133_CloneGraph.py', 'clone_graph')
        n1 = module.UndirectedGraphNode(1)
        n2 = module.UndirectedGraphNode(2)
        n3 = module.UndirectedGraphNode(3)
        n1.neighbors = [n2, n3]
        n2.neighbors = [n1, n3]
        n3.neighbors = [n1, n2]
        clone = module.Solution().cloneGraph(n1)
        self.assertIsNot(clone, n1)
        self.assertEqual(clone.label, 1)
        self.assertEqual(sorted(node.label for node in clone.neighbors), [2, 3])
        self.assertIsNot(clone.neighbors[0], n2)

    def test_gas_station(self):
        module = load_module('python/134_GasStation.py', 'gas_station')
        self.assertEqual(module.Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)

    def test_candy(self):
        module = load_module('python/135_Candy.py', 'candy')
        self.assertEqual(module.Solution().candy([1, 0, 2]), 5)
        self.assertEqual(module.Solution().candy([1, 2, 2]), 4)

    def test_single_number(self):
        module = load_module('python/136_SingleNumber.py', 'single_number')
        self.assertEqual(module.Solution().singleNumber([4, 1, 2, 1, 2]), 4)

    def test_single_number_ii(self):
        module = load_module('python/137_SingleNumberII.py', 'single_number_ii')
        self.assertEqual(module.Solution().singleNumber([2, 2, 3, 2]), 3)

    def test_copy_list_with_random_pointer(self):
        module = load_module('python/138_CopyListwithRandomPointer.py', 'copy_random')
        a = RandomListNode(1)
        b = RandomListNode(2)
        a.next = b
        a.random = b
        b.random = b
        clone = module.Solution().copyRandomList(a)
        self.assertIsNot(clone, a)
        self.assertEqual(clone.label, 1)
        self.assertEqual(clone.next.label, 2)
        self.assertIs(clone.random, clone.next)
        self.assertIs(clone.next.random, clone.next)

    def test_word_break(self):
        module = load_module('python/139_WordBreak.py', 'word_break')
        self.assertTrue(module.Solution().wordBreak('leetcode', ['leet', 'code']))
        self.assertFalse(module.Solution().wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))

    def test_word_break_ii(self):
        module = load_module('python/140_WordBreakII.py', 'word_break_ii')
        result = module.Solution().wordBreak('catsanddog', ['cat', 'cats', 'and', 'sand', 'dog'])
        self.assertEqual(sorted(result), sorted(['cats and dog', 'cat sand dog']))


if __name__ == '__main__':
    unittest.main()
