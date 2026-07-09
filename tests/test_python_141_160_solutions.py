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


def attach_cycle(head, pos):
    if pos < 0:
        return head
    cur = head
    entry = None
    index = 0
    tail = None
    while cur:
        if index == pos:
            entry = cur
        tail = cur
        cur = cur.next
        index += 1
    tail.next = entry
    return head


def set_read4(module, data):
    state = {'index': 0}

    def read4(buf):
        count = 0
        while count < 4 and state['index'] < len(data):
            buf[count] = data[state['index']]
            state['index'] += 1
            count += 1
        return count

    module.read4 = read4


class Python141To160SolutionTest(unittest.TestCase):

    def test_linked_list_cycle(self):
        module = load_module('python/141_LinkedListCycle.py', 'cycle')
        self.assertTrue(module.Solution().hasCycle(attach_cycle(build_list([3, 2, 0, -4]), 1)))
        self.assertFalse(module.Solution().hasCycle(build_list([1, 2, 3])))

    def test_linked_list_cycle_ii(self):
        module = load_module('python/142_LinkedListCycleII.py', 'cycle_ii')
        head = attach_cycle(build_list([3, 2, 0, -4]), 1)
        self.assertEqual(module.Solution().detectCycle(head).val, 2)
        self.assertIsNone(module.Solution().detectCycle(build_list([1, 2, 3])))

    def test_reorder_list(self):
        module = load_module('python/143_ReorderList.py', 'reorder')
        head = build_list([1, 2, 3, 4])
        module.Solution().reorderList(head)
        self.assertEqual(list_values(head), [1, 4, 2, 3])

    def test_binary_tree_preorder(self):
        module = load_module('python/144_BinaryTreePreorderTraversal.py', 'preorder')
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(module.Solution().preorderTraversal(root), [1, 2, 3])

    def test_binary_tree_postorder(self):
        module = load_module('python/145_BinaryTreePostorderTraversal.py', 'postorder')
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(module.Solution().postorderTraversal(root), [3, 2, 1])

    def test_lru_cache(self):
        module = load_module('python/146_LRUCache.py', 'lru')
        cache = module.LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        self.assertEqual(cache.get(1), 1)
        cache.put(3, 3)
        self.assertEqual(cache.get(2), -1)
        cache.put(4, 4)
        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(3), 3)
        self.assertEqual(cache.get(4), 4)

    def test_insertion_sort_list(self):
        module = load_module('python/147_InsertionSortList.py', 'insertion_sort')
        self.assertEqual(list_values(module.Solution().insertionSortList(build_list([4, 2, 1, 3]))), [1, 2, 3, 4])

    def test_sort_list(self):
        module = load_module('python/148_SortList.py', 'sort_list')
        self.assertEqual(list_values(module.Solution().sortList(build_list([4, 2, 1, 3]))), [1, 2, 3, 4])

    def test_max_points_on_a_line(self):
        module = load_module('python/149_MaxPointsonaLine.py', 'max_points')
        self.assertEqual(module.Solution().maxPoints([[1, 1], [2, 2], [3, 3]]), 3)
        self.assertEqual(module.Solution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4)

    def test_reverse_words_in_a_string(self):
        module = load_module('python/151_ReverseWordsinaString.py', 'reverse_words')
        self.assertEqual(module.Solution().reverseWords('  the sky is blue  '), 'blue is sky the')

    def test_maximum_product_subarray(self):
        module = load_module('python/152_MaximumProductSubarray.py', 'max_product')
        self.assertEqual(module.Solution().maxProduct([2, 3, -2, 4]), 6)
        self.assertEqual(module.Solution().maxProduct([-2, 0, -1]), 0)

    def test_find_minimum_rotated_sorted_array(self):
        module = load_module('python/153_FindMinimuminRotatedSortedArray.py', 'find_min')
        self.assertEqual(module.Solution().findMin([3, 4, 5, 1, 2]), 1)

    def test_find_minimum_rotated_sorted_array_ii(self):
        module = load_module('python/154_FindMinimuminRotatedSortedArrayII.py', 'find_min_ii')
        self.assertEqual(module.Solution().findMin([2, 2, 2, 0, 1]), 0)

    def test_binary_tree_upside_down(self):
        module = load_module('python/156_BinaryTreeUpsideDown.py', 'upside_down')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        new_root = module.Solution().upsideDownBinaryTree(root)
        self.assertEqual(new_root.val, 4)
        self.assertEqual(new_root.left.val, 5)
        self.assertEqual(new_root.right.val, 2)
        self.assertEqual(new_root.right.left.val, 3)
        self.assertEqual(new_root.right.right.val, 1)

    def test_read_n_characters_given_read4(self):
        module = load_module('python/157_ReadNCharactersGivenRead4.py', 'read4_once')
        set_read4(module, 'abcdef')
        buf = [''] * 4
        self.assertEqual(module.Solution().read(buf, 4), 4)
        self.assertEqual(''.join(buf), 'abcd')

    def test_read_n_characters_given_read4_ii(self):
        module = load_module('python/158_ReadNCharactersGivenRead4II.py', 'read4_many')
        set_read4(module, 'abcdef')
        solution = module.Solution()
        buf = [''] * 2
        self.assertEqual(solution.read(buf, 2), 2)
        self.assertEqual(''.join(buf), 'ab')
        buf = [''] * 3
        self.assertEqual(solution.read(buf, 3), 3)
        self.assertEqual(''.join(buf), 'cde')
        buf = [''] * 2
        self.assertEqual(solution.read(buf, 2), 1)
        self.assertEqual(''.join(buf[:1]), 'f')

    def test_longest_substring_at_most_two_distinct(self):
        module = load_module('python/159_LongestSubstringwithAtMostTwoDistinctCharacters.py', 'two_distinct')
        self.assertEqual(module.Solution().lengthOfLongestSubstringTwoDistinct('eceba'), 3)
        self.assertEqual(module.Solution().lengthOfLongestSubstringTwoDistinct('ccaabbb'), 5)

    def test_intersection_of_two_linked_lists(self):
        module = load_module('python/160_IntersectionofTwoLinkedLists.py', 'intersection')
        common = build_list([8, 4, 5])
        a = build_list([4, 1])
        b = build_list([5, 6, 1])
        tail = a
        while tail.next:
            tail = tail.next
        tail.next = common
        tail = b
        while tail.next:
            tail = tail.next
        tail.next = common
        self.assertIs(module.Solution().getIntersectionNode(a, b), common)


if __name__ == '__main__':
    unittest.main()
