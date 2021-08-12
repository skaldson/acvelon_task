"""The Acvelon Coding task

This module contain NumberFormatter class which have
parseInt method. With this method you can convert
stringified integer into integer(positive or negative,
all depend on sign before number)

Typical usage example:

test_str = '-1282021'
print(NumberFormatter.parseInt(test_str))
"""

import unittest


class NumberFormatter:
    """User-defined NumberFormatter class

    It has been writing as Acvelon coding task.
    Contain only single classmethod parseInt for
    parsing and converting stringified int into int."""

    @classmethod
    def parseInt(cls, number: str) -> int:
        """Main method for stringified integer parsing and converting"""
        if isinstance(number, str):
            if not number:
                return -1

            l_bound = len(str(2 ** 1))
            r_bound = len(str(2 ** 32 - 1))
            num_len = len(number)

            correct_len = \
                (True if num_len >= l_bound and num_len <= r_bound
                 else False)
            if correct_len:
                try:
                    result_value = int(number)
                    return result_value
                except ValueError:
                    return -1
            else:
                return -1
        elif isinstance(number, int):
            return -1


class TestNumberFormatter(unittest.TestCase):
    """Unittest class

     This class contains several tests
     for NumberFormatter class"""

    def test_is_not_str(self):
        """Test for check is_not_str case"""
        test_obj = 612
        fail_msg = "Decimal value is not applicable!"
        # in this case test_str it's just decimal int, test fail
        self.assertIsNot(NumberFormatter.parseInt(test_obj), -1, fail_msg)

    def test_empty_str(self):
        """Test for check empty_str case"""
        test_str = ""
        fail_msg = "Empty string is not applicable!"
        # in this case test_str is empty, test fail
        self.assertIsNot(NumberFormatter.parseInt(test_str), -1, fail_msg)

    def test_correct_length(self):
        """Test for check correct_length case"""
        test_str = "234230958209358239582935825029358209"
        str_len = len(test_str)
        fail_msg = ('Number length must be in [2;2^32-1] '
                    'range, but it len is %s!' % str_len)
        # in this case length of test_str bigger than 10, test fail
        self.assertIsNot(NumberFormatter.parseInt(test_str), -1, fail_msg)

    def test_stringified_int(self):
        """Test for check if input str is truly stringified integer case"""
        test_str = "-12_1231Ka"
        fail_msg = "Method parameter isn't a stringified integer!"
        # in this case test_str isn't a stringified integer, test fail
        self.assertIsNot(NumberFormatter.parseInt(test_str), -1, fail_msg)

    def test_negative_number(self):
        """Test for check negative_number case"""
        test_str = "-943112"
        assumed_res = -943112
        fail_msg = "Method returns an incorrect result!"
        # all OK, test completely success
        self.assertEqual(NumberFormatter.parseInt(test_str), assumed_res, fail_msg)

    def test_positive_number(self):
        """Test for check positive_number case"""
        test_str = "+1312"
        assumed_res = 1312
        fail_msg = "Method returns an incorrect result!"
        # all OK, test completely success
        self.assertEqual(NumberFormatter.parseInt(test_str), assumed_res, fail_msg)


if __name__ == "__main__":
    unittest.main()
