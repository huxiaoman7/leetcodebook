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


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def same_tree(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)


class Python81To100SolutionTest(unittest.TestCase):

    def test_search_in_rotated_sorted_array_ii(self):
        module = load_module('python/81_SearchinRotatedSortedArrayII.py', 'search_rotated_ii')
        self.assertTrue(module.Solution().search([2, 5, 6, 0, 0, 1, 2], 0))
        self.assertFalse(module.Solution().search([2, 5, 6, 0, 0, 1, 2], 3))

    def test_remove_duplicates_from_sorted_list_ii(self):
        module = load_module('python/82_RemoveDuplicatesfromSortedListII.py', 'delete_dup_list_ii')
        head = build_list([1, 2, 3, 3, 4, 4, 5])
        self.assertEqual(list_values(module.Solution().deleteDuplicates(head)), [1, 2, 5])

    def test_remove_duplicates_from_sorted_list(self):
        module = load_module('python/83_RemoveDuplicatesfromSortedList.py', 'delete_dup_list')
        head = build_list([1, 1, 2, 3, 3])
        self.assertEqual(list_values(module.Solution().deleteDuplicates(head)), [1, 2, 3])

    def test_maximal_rectangle(self):
        module = load_module('python/85_MaximalRectangle.py', 'maximal_rectangle')
        matrix = [
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0'],
        ]
        self.assertEqual(module.Solution().maximalRectangle(matrix), 6)

    def test_partition_list(self):
        module = load_module('python/86_PartitionList.py', 'partition_list')
        head = build_list([1, 4, 3, 2, 5, 2])
        self.assertEqual(list_values(module.Solution().partition(head, 3)), [1, 2, 2, 4, 3, 5])

    def test_scramble_string(self):
        module = load_module('python/87_ScrambleString.py', 'scramble_string')
        self.assertTrue(module.Solution().isScramble('great', 'rgeat'))
        self.assertFalse(module.Solution().isScramble('abcde', 'caebd'))

    def test_merge_sorted_array(self):
        module = load_module('python/88_MergeSortedArray.py', 'merge_sorted_array')
        nums1 = [1, 2, 3, 0, 0, 0]
        module.Solution().merge(nums1, 3, [2, 5, 6], 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_gray_code(self):
        module = load_module('python/89_GrayCode.py', 'gray_code')
        self.assertEqual(module.Solution().grayCode(2), [0, 1, 3, 2])

    def test_subsets_ii(self):
        module = load_module('python/90_SubsetsII.py', 'subsets_ii')
        result = module.Solution().subsetsWithDup([1, 2, 2])
        expected = [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
        self.assertEqual(sorted(result), sorted(expected))

    def test_decode_ways(self):
        module = load_module('python/91_DecodeWays.py', 'decode_ways')
        self.assertEqual(module.Solution().numDecodings('12'), 2)
        self.assertEqual(module.Solution().numDecodings('226'), 3)
        self.assertEqual(module.Solution().numDecodings('06'), 0)

    def test_reverse_linked_list_ii(self):
        module = load_module('python/92_ReverseLinkedListII.py', 'reverse_list_ii')
        head = build_list([1, 2, 3, 4, 5])
        self.assertEqual(list_values(module.Solution().reverseBetween(head, 2, 4)), [1, 4, 3, 2, 5])

    def test_restore_ip_addresses(self):
        module = load_module('python/93_RestoreIPAddresses.py', 'restore_ip')
        self.assertEqual(sorted(module.Solution().restoreIpAddresses('25525511135')), sorted(['255.255.11.135', '255.255.111.35']))

    def test_binary_tree_inorder_traversal(self):
        module = load_module('python/94_BinaryTreeInorderTraversal.py', 'inorder_traversal')
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(module.Solution().inorderTraversal(root), [1, 3, 2])

    def test_unique_binary_search_trees_ii(self):
        module = load_module('python/95_UniqueBinarySearchTreesII.py', 'unique_bst_ii')
        result = module.Solution().generateTrees(3)
        self.assertEqual(len(result), 5)
        self.assertEqual(sorted(tuple(inorder(tree)) for tree in result), [(1, 2, 3)] * 5)

    def test_unique_binary_search_trees(self):
        module = load_module('python/96_UniqueBinarySearchTrees.py', 'unique_bst')
        self.assertEqual(module.Solution().numTrees(3), 5)

    def test_interleaving_string(self):
        module = load_module('python/97_InterleavingString.py', 'interleaving_string')
        self.assertTrue(module.Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
        self.assertFalse(module.Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))

    def test_validate_binary_search_tree(self):
        module = load_module('python/98_ValidateBinarySearchTree.py', 'validate_bst')
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(module.Solution().isValidBST(root))
        bad = TreeNode(5)
        bad.left = TreeNode(1)
        bad.right = TreeNode(4)
        bad.right.left = TreeNode(3)
        bad.right.right = TreeNode(6)
        self.assertFalse(module.Solution().isValidBST(bad))

    def test_recover_binary_search_tree(self):
        module = load_module('python/99_RecoverBinarySearchTree.py', 'recover_bst')
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(2)
        module.Solution().recoverTree(root)
        self.assertEqual(inorder(root), [1, 2, 3, 4])

    def test_same_tree(self):
        module = load_module('python/100_SameTree.py', 'same_tree')
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)
        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        self.assertTrue(module.Solution().isSameTree(p, q))
        q.right.val = 4
        self.assertFalse(module.Solution().isSameTree(p, q))


if __name__ == '__main__':
    unittest.main()
