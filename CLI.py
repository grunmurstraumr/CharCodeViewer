from Converter import Converter
import sys


def print_table(data):
    # Data is assumed to be a list of dicts having one or more of the keys, decimal, hex, binary
    COLUMN_WIDTH = 15
    keys = ['original', 'decimal', 'hex', 'binary']
    print_string = '{: <%s}' % COLUMN_WIDTH + '{: >%s}' % COLUMN_WIDTH * 3
    # Print header:
    print(print_string.format('Letter', 'Decimal', 'Hex', 'Binary'))
    for i in data:
        output = {'original': '', 'decimal': 'N/A', 'hex': 'N/A', 'binary': 'N/A'}
        for key in keys:
            try:
                output[key] = i[key]
            except KeyError:
                # Catch error and silence. Default value is already assigned in output instantiantion.
                pass
        print(print_string.format(output['original'], output['decimal'], output['hex'], output['binary']))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        i = input("Input characters: ")

    else:
        i = sys.argv[1]
    print_table(Converter.convert_many(i))

