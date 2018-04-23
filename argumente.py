""".

jemand transferiert jemandem eine summe am datum für etwas.
===========================================================
Optionen
    -h
        help
    -i (inputfile)
    -o (outputfile)

"""
import sys
import getopt


def main(argv):
    """trniaetrnae."""
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["infile=", "outfile="])
    except getopt.GetoptError:
        print(sys.argv[0] + ' -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(sys.argv[0] + ' -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg
        elif opt in ("-o", "--outfile"):
            outputfile = arg
    print("Input file is " + inputfile)
    print("Output file is " + outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
