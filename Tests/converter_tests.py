import unittest

from Converter import Converter

class Test_converter(unittest.TestCase):
    def test_ascii_codes(self):
        ascii_table = {'a': 97,
                       'b': 98,
                       'c': 99,
                       'A': 65,
                       'B': 66,
                       'C': 67,
                       ' ': 32,
                       '!': 33,
                       '\"': 34,
                       '\'': 39,
                       '*': 42,
                       '?': 63}
        for key, val in ascii_table.items():
            self.assertEqual(Converter.convert_ascii(key), val)

    def test_pretty_binary(self):
        #Correct length < byte
        self.assertEqual(9, len(Converter._pretty_print_binary('111')))
        #Correct length < 2 bytes & > byte
        self.assertEqual(19, len(Converter._pretty_print_binary('100010001000')))
        #Test single number
        self.assertEqual(Converter._pretty_print_binary('1'), '0000 0001')
        #Test full nibble
        self.assertEqual(Converter._pretty_print_binary('0010'), '0000 0010')
        #Test 5 characters
        self.assertEqual(Converter._pretty_print_binary('11001'), '0001 1001')
        #Test wrong split nibble
        self.assertEqual(Converter._pretty_print_binary('1 00 1'), '0000 1001')
        #Test wrong split full byte
        self.assertEqual(Converter._pretty_print_binary('10 0101 10'), '1001 0110')

    def test_binary(self):
        binary_test_table = {
            'a': ''
        }
        self.assertEqual('0110 0001', Converter.convert_binary('a'))
if __name__ == '__main__':
    unittest.main()