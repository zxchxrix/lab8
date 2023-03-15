import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin_conversion


class TestBTCConversion(TestCase):

    @patch('builtins.print')
    def test_print_result(self, mock_print):
        bitcoin_conversion.print_converted_amount(100, 2)
        mock_print.assert_called_once_with('The amount of BTC you have are worth: $200')


if __name__ == '__main__':
    unittest.main()
