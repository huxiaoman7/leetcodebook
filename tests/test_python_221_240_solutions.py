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


def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def list_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


class Python221To240SolutionTest(unittest.TestCase):

    def test_maximal_square(self):
        module = load_module('python/221_MaximalSquare.py', 'maximal_square')
        matrix = [
            ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0'],
        ]
        self.assertEqual(module.Solution().maximalSquare(matrix), 4)

    def test_count_complete_tree_nodes(self):
        module = load_module('python/222_CountCompleteTreeNodes.py', 'count_nodes')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        self.assertEqual(module.Solution().countNodes(root), 6)

    def test_rectangle_area(self):
        module = load_module('python/223_RectangleArea.py', 'rectangle_area')
        self.assertEqual(module.Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2), 45)

    def test_basic_calculator(self):
        module = load_module('python/224_BasicCalculator.py', 'basic_calculator')
        self.assertEqual(module.Solution().calculate('1 + 1'), 2)
        self.assertEqual(module.Solution().calculate('(1+(4+5+2)-3)+(6+8)'), 23)

    def test_implement_stack_using_queues(self):
        module = load_module('python/225_ImplementStackusingQueues.py', 'stack_queues')
        stack = module.MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertFalse(stack.empty())

    def test_invert_binary_tree(self):
        module = load_module('python/226_InvertBinaryTree.py', 'invert_tree')
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        inverted = module.Solution().invertTree(root)
        self.assertEqual(inverted.left.val, 7)
        self.assertEqual(inverted.right.val, 2)
        self.assertEqual(inverted.left.left.val, 9)
        self.assertEqual(inverted.right.right.val, 1)

    def test_basic_calculator_ii(self):
        module = load_module('python/227_BasicCalculatorII.py', 'basic_calculator_ii')
        self.assertEqual(module.Solution().calculate('3+2*2'), 7)
        self.assertEqual(module.Solution().calculate(' 3/2 '), 1)
        self.assertEqual(module.Solution().calculate(' 3+5 / 2 '), 5)

    def test_summary_ranges(self):
        module = load_module('python/228_SummaryRanges.py', 'summary_ranges')
        self.assertEqual(module.Solution().summaryRanges([0, 1, 2, 4, 5, 7]), ['0->2', '4->5', '7'])

    def test_majority_element_ii(self):
        module = load_module('python/229_MajorityElementII.py', 'majority_ii')
        self.assertEqual(sorted(module.Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2])), [1, 2])

    def test_kth_smallest_element_in_bst(self):
        module = load_module('python/230_KthSmallestElementinaBST.py', 'kth_bst')
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(module.Solution().kthSmallest(root, 1), 1)

    def test_power_of_two(self):
        module = load_module('python/231_PowerofTwo.py', 'power_two')
        self.assertTrue(module.Solution().isPowerOfTwo(16))
        self.assertFalse(module.Solution().isPowerOfTwo(3))

    def test_implement_queue_using_stacks(self):
        module = load_module('python/232_ImplementQueueusingStacks.py', 'queue_stacks')
        queue = module.MyQueue()
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.pop(), 1)
        self.assertFalse(queue.empty())

    def test_number_of_digit_one(self):
        module = load_module('python/233_NumberofDigitOne.py', 'digit_one')
        self.assertEqual(module.Solution().countDigitOne(13), 6)
        self.assertEqual(module.Solution().countDigitOne(0), 0)

    def test_palindrome_linked_list(self):
        module = load_module('python/234_PalindromeLinkedList.py', 'palindrome_list')
        self.assertTrue(module.Solution().isPalindrome(build_list([1, 2, 2, 1])))
        self.assertFalse(module.Solution().isPalindrome(build_list([1, 2])))

    def test_lowest_common_ancestor_bst(self):
        module = load_module('python/235_LowestCommonAncestorofaBinarySearchTree.py', 'lca_bst')
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        self.assertEqual(module.Solution().lowestCommonAncestor(root, root.left, root.right), root)
        self.assertEqual(module.Solution().lowestCommonAncestor(root, root.left, root.left.right), root.left)

    def test_lowest_common_ancestor_binary_tree(self):
        module = load_module('python/236_LowestCommonAncestorofaBinaryTree.py', 'lca_tree')
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        self.assertEqual(module.Solution().lowestCommonAncestor(root, root.left, root.right), root)
        self.assertEqual(module.Solution().lowestCommonAncestor(root, root.left, root.left.right.right), root.left)

    def test_delete_node_in_linked_list(self):
        module = load_module('python/237_DeleteNodeinaLinkedList.py', 'delete_node')
        head = build_list([4, 5, 1, 9])
        module.Solution().deleteNode(head.next)
        self.assertEqual(list_values(head), [4, 1, 9])

    def test_product_of_array_except_self(self):
        module = load_module('python/238_ProductofArrayExceptSelf.py', 'product_except_self')
        self.assertEqual(module.Solution().productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_sliding_window_maximum(self):
        module = load_module('python/239_SlidingWindowMaximum.py', 'sliding_window')
        self.assertEqual(module.Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])

    def test_search_a_2d_matrix_ii(self):
        module = load_module('python/240_Searcha2DMatrixII.py', 'search_matrix_ii')
        matrix = [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ]
        self.assertTrue(module.Solution().searchMatrix(matrix, 5))
        self.assertFalse(module.Solution().searchMatrix(matrix, 20))


if __name__ == '__main__':
    unittest.main()
