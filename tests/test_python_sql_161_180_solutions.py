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


class PythonSql161To180SolutionTest(unittest.TestCase):

    def test_one_edit_distance(self):
        module = load_module('python/161_OneEditDistance.py', 'one_edit')
        self.assertTrue(module.Solution().isOneEditDistance('ab', 'acb'))
        self.assertFalse(module.Solution().isOneEditDistance('cab', 'ad'))
        self.assertFalse(module.Solution().isOneEditDistance('a', 'a'))

    def test_find_peak_element(self):
        module = load_module('python/162_FindPeakElement.py', 'find_peak')
        nums = [1, 2, 1, 3, 5, 6, 4]
        index = module.Solution().findPeakElement(nums)
        self.assertIn(index, [1, 5])
        self.assertGreater(nums[index], nums[index - 1] if index > 0 else float('-inf'))
        self.assertGreater(nums[index], nums[index + 1] if index + 1 < len(nums) else float('-inf'))

    def test_missing_ranges(self):
        module = load_module('python/163_MissingRanges.py', 'missing_ranges')
        self.assertEqual(module.Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99), ['2', '4->49', '51->74', '76->99'])

    def test_maximum_gap(self):
        module = load_module('python/164_MaximumGap.py', 'maximum_gap')
        self.assertEqual(module.Solution().maximumGap([3, 6, 9, 1]), 3)
        self.assertEqual(module.Solution().maximumGap([10]), 0)

    def test_compare_version_numbers(self):
        module = load_module('python/165_CompareVersionNumbers.py', 'compare_version')
        self.assertEqual(module.Solution().compareVersion('1.01', '1.001'), 0)
        self.assertEqual(module.Solution().compareVersion('1.0', '1.0.0'), 0)
        self.assertEqual(module.Solution().compareVersion('0.1', '1.1'), -1)

    def test_fraction_to_recurring_decimal(self):
        module = load_module('python/166_FractiontoRecurringDecimal.py', 'fraction_decimal')
        self.assertEqual(module.Solution().fractionToDecimal(1, 2), '0.5')
        self.assertEqual(module.Solution().fractionToDecimal(2, 1), '2')
        self.assertEqual(module.Solution().fractionToDecimal(2, 3), '0.(6)')

    def test_two_sum_ii(self):
        module = load_module('python/167_TwoSumIIInputArrayisSorted.py', 'two_sum_ii')
        self.assertEqual(module.Solution().twoSum([2, 7, 11, 15], 9), [1, 2])

    def test_excel_sheet_column_title(self):
        module = load_module('python/168_ExcelSheetColumnTitle.py', 'excel_title')
        self.assertEqual(module.Solution().convertToTitle(1), 'A')
        self.assertEqual(module.Solution().convertToTitle(28), 'AB')
        self.assertEqual(module.Solution().convertToTitle(701), 'ZY')

    def test_majority_element(self):
        module = load_module('python/169_MajorityElement.py', 'majority')
        self.assertEqual(module.Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)

    def test_two_sum_iii(self):
        module = load_module('python/170_TwoSumIII.py', 'two_sum_iii')
        obj = module.TwoSum()
        obj.add(1)
        obj.add(3)
        obj.add(5)
        self.assertTrue(obj.find(4))
        self.assertFalse(obj.find(7))

    def test_excel_sheet_column_number(self):
        module = load_module('python/171_ExcelSheetColumnNumber.py', 'excel_number')
        self.assertEqual(module.Solution().titleToNumber('A'), 1)
        self.assertEqual(module.Solution().titleToNumber('AB'), 28)
        self.assertEqual(module.Solution().titleToNumber('ZY'), 701)

    def test_factorial_trailing_zeroes(self):
        module = load_module('python/172_FactorialTrailingZeroes.py', 'trailing_zeroes')
        self.assertEqual(module.Solution().trailingZeroes(3), 0)
        self.assertEqual(module.Solution().trailingZeroes(5), 1)
        self.assertEqual(module.Solution().trailingZeroes(30), 7)

    def test_bst_iterator(self):
        module = load_module('python/173_BinarySearchTreeIterator.py', 'bst_iterator')
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)
        iterator = module.BSTIterator(root)
        result = []
        while iterator.hasNext():
            result.append(iterator.next())
        self.assertEqual(result, [3, 7, 9, 15, 20])

    def test_dungeon_game(self):
        module = load_module('python/174_DungeonGame.py', 'dungeon')
        dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
        self.assertEqual(module.Solution().calculateMinimumHP(dungeon), 7)

    def test_largest_number(self):
        module = load_module('python/179_LargestNumber.py', 'largest_number')
        self.assertEqual(module.Solution().largestNumber([10, 2]), '210')
        self.assertEqual(module.Solution().largestNumber([3, 30, 34, 5, 9]), '9534330')

    def test_sql_files_exist_with_expected_clauses(self):
        expectations = {
            'sql/175_CombineTwoTables.sql': ['left join', 'person', 'address'],
            'sql/176_SecondHighestSalary.sql': ['select', 'max', 'salary'],
            'sql/177_NthHighestSalary.sql': ['create function', 'getnthhighestsalary', 'limit'],
            'sql/178_RankScores.sql': ['dense_rank', 'score'],
            'sql/180_ConsecutiveNumbers.sql': ['logs', 'consecutivenums'],
        }
        for relative_path, fragments in expectations.items():
            content = (ROOT / relative_path).read_text().lower()
            for fragment in fragments:
                self.assertIn(fragment, content)


if __name__ == '__main__':
    unittest.main()
