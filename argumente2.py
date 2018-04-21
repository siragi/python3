#!/usr/bin/python
# coding: utf-8

# jemand transferiert jemandem eine summe am datum für etwas

import sys, getopt


def main(argv):
    comment = ''
    
    try:
        opts, args = getopt.getopt(argv,"hc:",["comment="])
    except getopt.GetoptError:
        print(__file__ + ' -c <"Kommentar">')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(__file__ + ' überweiser empfänger summe -c <"Kommentar">')
            sys.exit()
        elif opt in ("-c", "--comment"):
            comment = arg
        print(arg)

    inputfile = argv[0]	
    outputfile = argv[1]

        
##        elif arg != ''
##
##        elif && argv[2] == '':
      
          
    print("Input file is " + inputfile)
    print("Output file is " + outputfile)
    print("comment is " + comment)

if __name__ == "__main__":
    main(sys.argv[1:])
