import unittest
from main import add, subtract, multiply, divide, check, mod

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 5), 7)
        self.assertNotEqual(add(3, 7), 9)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)
        self.assertNotEqual(subtract(4, 2), 1)

    def test_multiply(self):
        self.assertNotEqual(multiply(2, 5), 12)
        self.assertEqual(multiply(3, 6), 18)

    def test_divide(self):
        self.assertNotEqual(divide(4, 2), 3)
        self.assertEqual(divide(20, 5), 4)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)


class TestCheck(unittest.TestCase):
    def test_check(self):
        self.assertTrue(check(2))
        self.assertTrue(check(6))
        self.assertTrue(check(220))

        self.assertFalse(check(1))
        self.assertFalse(check(3))
        self.assertFalse(check(57))


class TestMod(unittest.TestCase):
    def test_mod_success(self):
        # Проверяем корректность вычисления остатка
        self.assertEqual(mod(10, 3), 1)  # 10 % 3 = 1
        self.assertEqual(mod(15, 4), 3)  # 15 % 4 = 3
        self.assertEqual(mod(20, 5), 0)  # 20 % 5 = 0

    def test_mod_by_zero(self):
        # Проверяем обработку деления на ноль
        self.assertRaises(ValueError, mod, 10, 0)


if __name__ == '__main__':
    unittest.main()