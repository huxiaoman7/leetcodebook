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


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class NextNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for value in values:
        cur.next = ListNode(value)
        cur = cur.next
    return dummy.next


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def right_chain(root):
    result = []
    while root:
        result.append(root.val)
        if root.left:
            result.append('left-not-none')
            break
        root = root.right
    return result


class Python101To120SolutionTest(unittest.TestCase):

    def test_symmetric_tree(self):
        module = load_module('python/101_SymmetricTree.py', 'symmetric_tree')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertTrue(module.Solution().isSymmetric(root))
        root.right.right.val = 5
        self.assertFalse(module.Solution().isSymmetric(root))

    def test_level_order(self):
        module = load_module('python/102_BinaryTreeLevelOrderTraversal.py', 'level_order')
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(module.Solution().levelOrder(root), [[3], [9, 20], [15, 7]])

    def test_zigzag_level_order(self):
        module = load_module('python/103_BinaryTreeZigzagLevelOrderTraversal.py', 'zigzag')
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(module.Solution().zigzagLevelOrder(root), [[3], [20, 9], [15, 7]])

    def test_maximum_depth(self):
        module = load_module('python/104_MaximumDepthofBinaryTree.py', 'max_depth')
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(module.Solution().maxDepth(root), 3)

    def test_build_tree_preorder_inorder(self):
        module = load_module('python/105_ConstructBinaryTreefromPreorderandInorderTraversal.py', 'build_pre_in')
        root = module.Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
        self.assertEqual(preorder(root), [3, 9, 20, 15, 7])
        self.assertEqual(inorder(root), [9, 3, 15, 20, 7])

    def test_build_tree_inorder_postorder(self):
        module = load_module('python/106_ConstructBinaryTreefromInorderandPostorderTraversal.py', 'build_in_post')
        root = module.Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
        self.assertEqual(preorder(root), [3, 9, 20, 15, 7])
        self.assertEqual(inorder(root), [9, 3, 15, 20, 7])

    def test_level_order_bottom(self):
        module = load_module('python/107_BinaryTreeLevelOrderTraversalII.py', 'level_bottom')
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(module.Solution().levelOrderBottom(root), [[15, 7], [9, 20], [3]])

    def test_convert_sorted_array_to_bst(self):
        module = load_module('python/108_ConvertSortedArraytoBinarySearchTree.py', 'array_to_bst')
        root = module.Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
        self.assertEqual(inorder(root), [-10, -3, 0, 5, 9])

    def test_convert_sorted_list_to_bst(self):
        module = load_module('python/109_ConvertSortedListtoBinarySearchTree.py', 'list_to_bst')
        root = module.Solution().sortedListToBST(build_list([-10, -3, 0, 5, 9]))
        self.assertEqual(inorder(root), [-10, -3, 0, 5, 9])

    def test_balanced_binary_tree(self):
        module = load_module('python/110_BalancedBinaryTree.py', 'balanced_tree')
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertTrue(module.Solution().isBalanced(root))
        root.left.left = TreeNode(1)
        root.left.left.left = TreeNode(0)
        self.assertFalse(module.Solution().isBalanced(root))

    def test_minimum_depth(self):
        module = load_module('python/111_MinimumDepthofBinaryTree.py', 'min_depth')
        root = TreeNode(2)
        root.right = TreeNode(3)
        root.right.right = TreeNode(4)
        self.assertEqual(module.Solution().minDepth(root), 3)

    def test_path_sum(self):
        module = load_module('python/112_PathSum.py', 'path_sum')
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        self.assertTrue(module.Solution().hasPathSum(root, 22))
        self.assertFalse(module.Solution().hasPathSum(root, 28))

    def test_path_sum_ii(self):
        module = load_module('python/113_PathSumII.py', 'path_sum_ii')
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)
        self.assertEqual(sorted(module.Solution().pathSum(root, 22)), sorted([[5, 4, 11, 2], [5, 8, 4, 5]]))

    def test_flatten_binary_tree_to_linked_list(self):
        module = load_module('python/114_FlattenBinaryTreetoLinkedList.py', 'flatten_tree')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        module.Solution().flatten(root)
        self.assertEqual(right_chain(root), [1, 2, 3, 4, 5, 6])

    def test_distinct_subsequences(self):
        module = load_module('python/115_DistinctSubsequences.py', 'distinct_subseq')
        self.assertEqual(module.Solution().numDistinct('rabbbit', 'rabbit'), 3)
        self.assertEqual(module.Solution().numDistinct('babgbag', 'bag'), 5)

    def test_populating_next_right_pointers(self):
        module = load_module('python/116_PopulatingNextRightPointersinEachNode.py', 'connect_next')
        root = NextNode(1)
        root.left = NextNode(2)
        root.right = NextNode(3)
        root.left.left = NextNode(4)
        root.left.right = NextNode(5)
        root.right.left = NextNode(6)
        root.right.right = NextNode(7)
        module.Solution().connect(root)
        self.assertIs(root.left.next, root.right)
        self.assertIs(root.left.right.next, root.right.left)

    def test_populating_next_right_pointers_ii(self):
        module = load_module('python/117_PopulatingNextRightPointersinEachNodeII.py', 'connect_next_ii')
        root = NextNode(1)
        root.left = NextNode(2)
        root.right = NextNode(3)
        root.left.right = NextNode(5)
        root.right.right = NextNode(7)
        module.Solution().connect(root)
        self.assertIs(root.left.next, root.right)
        self.assertIs(root.left.right.next, root.right.right)

    def test_pascals_triangle(self):
        module = load_module('python/118_PascalsTriangle.py', 'pascal')
        self.assertEqual(module.Solution().generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])

    def test_pascals_triangle_ii(self):
        module = load_module('python/119_PascalsTriangleII.py', 'pascal_ii')
        self.assertEqual(module.Solution().getRow(3), [1, 3, 3, 1])

    def test_triangle(self):
        module = load_module('python/120_Triangle.py', 'triangle')
        self.assertEqual(module.Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11)


if __name__ == '__main__':
    unittest.main()
