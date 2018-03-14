import csv
import sys


def main(filename, out_filename):
    file = open(filename, "r")
    outfile = open(out_filename, "w")

    csv_reader = csv.reader(file)
    first_column = []

    for row in csv_reader:
        first_column.append(row[0].title())

    names = first_column[1:-1]

    outfile.writelines('\n'.join(names))

    file.close()
    outfile.close()

if __name__ == '__main__':
    filename = sys.argv[1]
    out_filename = sys.argv[2]
    main(filename, out_filename)
