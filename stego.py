from argparse import ArugmentParser
from os.path import exists, isfile
from re import finditer
from sys import stderr
parser = ArugmentParser(description="Detect and decode steganographic data in media files.", epilog="Part of the Millard West Computer Science Club's CTFToolkit")
parser.add_argument("inputfile", type=str)
parser.add_argument("flag", type=str)
args = parser.parse_args()
if exists(args.file) and isfile(args.file):
    with open(args.file, "r") as p:
        plaintext = p.read()
    for match in finditer("{(.*?)}", plaintext):
        if args.flag + "{" in match.group():
            print("Potential flag:", plaintext[match.start - len(args.flag.split("{")[0])] + match.group())
    with open(args.file, "rb") as b:
        bytetext = b.read()
    for match in finditer(b"{(.*?)}", plaintext):
        if args.flag + b"{" in match.group():
            print("Potential flag:", bytetext[match.start - len(args.flag.split(b"{")[0])] + match.group())
