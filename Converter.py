from collections import OrderedDict
class Converter:

    @staticmethod
    def convert_ascii(char: str):
        """Converts a character into it's decimal representation in ASCII. Assumes the string is of length 1."""
        return ord(char)

    @staticmethod
    def convert_hex(char: str):
        """Converts a character into it's hexadecimal equivalent in ASCII. Assumes string of len 1 (no checks)"""
        return hex(ord(char))

    @staticmethod
    def convert_binary(char: str):
        """Converts a character into it's binary equivalent in ASCII. Assumes a string of len 1 (no checks)"""
        return Converter._pretty_print_binary(bin(ord(char))[2:]) #[2:] removes the leading 0b1

    @staticmethod
    def _pretty_print_binary(ugly: str):
        #Should be format binary and accept grouping argument. and min length?
        #This function breaks the single responsibility principle of the class
        ugly = ''.join(ugly.split()) #Remove spaces
        length = len(ugly)
        #Check if padding is needed to reach full bytes
        if not length % 8 == 0:
            padding = (((length // 8) + 1) * 8) - length
            ugly = ugly.zfill(length + padding) #Add padding 0's
        pretty = ''.join([ugly[i:i+4] + ' ' for i in range(0, len(ugly), 4)]).rstrip() #Insert spaces to group by 4

        return pretty

    @classmethod
    def convert_one(cls, char: str):
        """Converts one character into a dict with it's original, decimal, hecadecinal and binary ASCII representations."""
        return {'original': char,
                'decimal': cls.convert_ascii(char),
                'hex': cls.convert_hex(char),
                'binary': cls.convert_binary(char)}

    @classmethod
    def convert_many(cls, string: str):
        """Converts several characters. Input must be a string"""
        #Remove duplicates
        string = ''.join(OrderedDict.fromkeys(string))
        return [cls.convert_one(char) for char in string]

if __name__ == '__main__':
    pass