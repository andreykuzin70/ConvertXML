import argparse
import os
import sys


def main():


    parser = argparse.ArgumentParser(description="Reformat IGV Session")
    parser.add_argument('igvSession', type=str, help="Path to IGV session that needs to be reformatted")
    parser.add_argument('convertedFile', type=str, help="Name for newly formatted file")

    args = parser.parse_args()

    file_exists(args.igvSession, exit=True)

    outputfile = open(args.convertedFile + '.xml', 'w')

    with open(args.igvSession) as f:
        for line in f:
            str1 = line
            if ":\\" in str1:

                index = str1.find(":\\")
                str2 = str1[:(index-1)] + "/Volumes/giab" + str1[(index+1):]
                str2 = str2.replace("\\", "/")
                outputfile.write(str2)
            else:
                outputfile.write(str1)


def file_exists(checkFile, exit=False):
    try:
        fileHolder = open(checkFile, 'r')
    except FileNotFoundError:
        print("ERROR: File '{}' containing Variant Positions does not exist!".format(
            checkFile))
        if exit == True:
            print("Exiting...")
            sys.exit()


if __name__ == "__main__":
    main()


# python ConvertXML.py C:\Users\ank22\PythonScripts\igv_session.txt ConvertedFile
# python ConvertXML.py Y:\data\igv_sessions\AndreySession.xml ConvertedFile2