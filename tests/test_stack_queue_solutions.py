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


class StackQueueSolutionTest(unittest.TestCase):

    def test_largest_rectangle_in_histogram(self):
        module = load_module('python/84_LargestRectangleinHistogram.py', 'largest_rectangle')
        self.assertEqual(module.Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
        self.assertEqual(module.Solution().largestRectangleArea([2, 4]), 4)

    def test_evaluate_reverse_polish_notation(self):
        module = load_module('python/150_EvaluateReversePolishNotation.py', 'eval_rpn')
        self.assertEqual(module.Solution().evalRPN(["2", "1", "+", "3", "*"]), 9)
        self.assertEqual(module.Solution().evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_min_stack(self):
        module = load_module('python/155_MinStack.py', 'min_stack')
        stack = module.MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        self.assertEqual(stack.getMin(), -3)
        stack.pop()
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.getMin(), -2)

    def test_course_schedule(self):
        module = load_module('python/207_CourseSchedule.py', 'course_schedule')
        self.assertTrue(module.Solution().canFinish(2, [[1, 0]]))
        self.assertFalse(module.Solution().canFinish(2, [[1, 0], [0, 1]]))

    def test_implement_queue_using_stacks(self):
        module = load_module('python/232_ImplementQueueusingStacks.py', 'queue_using_stacks')
        queue = module.MyQueue()
        queue.push(1)
        queue.push(2)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.pop(), 1)
        self.assertFalse(queue.empty())
        self.assertEqual(queue.pop(), 2)
        self.assertTrue(queue.empty())

    def test_sliding_window_maximum(self):
        module = load_module('python/239_SlidingWindowMaximum.py', 'sliding_window')
        self.assertEqual(
            module.Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7],
        )
        self.assertEqual(module.Solution().maxSlidingWindow([1], 1), [1])


if __name__ == '__main__':
    unittest.main()
