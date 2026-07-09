import importlib.util
import pathlib
import subprocess
import textwrap
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


class PythonSqlShell181To200SolutionTest(unittest.TestCase):

    def run_shell(self, relative_path, content):
        result = subprocess.run(
            ['bash', str(ROOT / relative_path)],
            input=textwrap.dedent(content).lstrip(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return result.stdout

    def test_reverse_words_in_string_ii(self):
        module = load_module('python/186_ReverseWordsinaStringII.py', 'reverse_words_ii')
        chars = list('the sky is blue')
        module.Solution().reverseWords(chars)
        self.assertEqual(''.join(chars), 'blue is sky the')

    def test_repeated_dna_sequences(self):
        module = load_module('python/187_RepeatedDNASequences.py', 'repeated_dna')
        result = module.Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
        self.assertEqual(sorted(result), ['AAAAACCCCC', 'CCCCCAAAAA'])

    def test_best_time_to_buy_and_sell_stock_iv(self):
        module = load_module('python/188_BestTimetoBuyandSellStockIV.py', 'stock_iv')
        self.assertEqual(module.Solution().maxProfit(2, [2, 4, 1]), 2)
        self.assertEqual(module.Solution().maxProfit(2, [3, 2, 6, 5, 0, 3]), 7)

    def test_rotate_array(self):
        module = load_module('python/189_RotateArray.py', 'rotate_array')
        nums = [1, 2, 3, 4, 5, 6, 7]
        module.Solution().rotate(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_reverse_bits(self):
        module = load_module('python/190_ReverseBits.py', 'reverse_bits')
        self.assertEqual(module.Solution().reverseBits(43261596), 964176192)

    def test_number_of_one_bits(self):
        module = load_module('python/191_Numberof1Bits.py', 'one_bits')
        self.assertEqual(module.Solution().hammingWeight(11), 3)
        self.assertEqual(module.Solution().hammingWeight(128), 1)

    def test_house_robber(self):
        module = load_module('python/198_HouseRobber.py', 'house_robber')
        self.assertEqual(module.Solution().rob([1, 2, 3, 1]), 4)
        self.assertEqual(module.Solution().rob([2, 7, 9, 3, 1]), 12)

    def test_binary_tree_right_side_view(self):
        module = load_module('python/199_BinaryTreeRightSideView.py', 'right_side')
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        self.assertEqual(module.Solution().rightSideView(root), [1, 3, 4])

    def test_number_of_islands(self):
        module = load_module('python/200_NumberofIslands.py', 'number_islands')
        grid = [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
        ]
        self.assertEqual(module.Solution().numIslands(grid), 1)
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1'],
        ]
        self.assertEqual(module.Solution().numIslands(grid), 3)

    def test_sql_files_exist_with_expected_clauses(self):
        expectations = {
            'sql/181_EmployeesEarningMoreThanTheirManagers.sql': ['employee', 'manager', 'salary', 'join'],
            'sql/182_DuplicateEmails.sql': ['email', 'group by', 'having count'],
            'sql/183_CustomersWhoNeverOrder.sql': ['customers', 'orders', 'left join'],
            'sql/184_DepartmentHighestSalary.sql': ['department', 'employee', 'salary', 'max'],
            'sql/185_DepartmentTopThreeSalaries.sql': ['dense_rank', 'partition by', 'department'],
            'sql/196_DeleteDuplicateEmails.sql': ['delete', 'person', 'email', 'id'],
            'sql/197_RisingTemperature.sql': ['weather', 'datediff', 'temperature'],
        }
        for relative_path, fragments in expectations.items():
            content = (ROOT / relative_path).read_text().lower()
            for fragment in fragments:
                self.assertIn(fragment, content)

    def test_word_frequency_shell(self):
        output = self.run_shell('shell/192_WordFrequency.sh', '''
            the day is sunny the the
            the sunny is is
        ''')
        self.assertEqual(output, 'the 4\nis 3\nsunny 2\nday 1\n')

    def test_valid_phone_numbers_shell(self):
        output = self.run_shell('shell/193_ValidPhoneNumbers.sh', '''
            987-123-4567
            123 456 7890
            (123) 456-7890
            (123)-456-7890
        ''')
        self.assertEqual(output, '987-123-4567\n(123) 456-7890\n')

    def test_transpose_file_shell(self):
        output = self.run_shell('shell/194_TransposeFile.sh', '''
            name age
            alice 21
            ryan 30
        ''')
        self.assertEqual(output, 'name alice ryan\nage 21 30\n')

    def test_tenth_line_shell(self):
        content = ''.join('line%s\n' % i for i in range(1, 12))
        output = self.run_shell('shell/195_TenthLine.sh', content)
        self.assertEqual(output, 'line10\n')


if __name__ == '__main__':
    unittest.main()
