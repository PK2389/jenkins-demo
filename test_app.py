"""Unit tests for app.py, run by the Jenkins Test stage."""

import unittest

from app import add, subtract, greet


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)


class TestSubtract(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_negative_result(self):
        self.assertEqual(subtract(2, 5), -3)


class TestGreet(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greet("Jenkins"), "Hello, Jenkins!")

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
