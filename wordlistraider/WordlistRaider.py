import os
import sys
import argparse
import re

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from more_termcolor import cprint 
from pyfiglet import figlet_format

cprint(figlet_format('WordlistRaider!', font='starwars', width=100), 'red')
cprint('Coded by Gregor Biswanger, Jürgen Gutsch & Community - Version 1.0', 'yellow')

parser = argparse.ArgumentParser(description='Returns a selection of words that matches the passed conditions in an existing list.')
parser.add_argument('-w', '--wordlist', metavar='path to source file', type=str, required=True, help='the wordlist to raid')
parser.add_argument('-t', '--target', metavar='path to the target file', type=str, required=True, help='the target wordlist')
parser.add_argument('--min', '--minlength', default=8, type=int, help='minimum length of password (default: 8)')
parser.add_argument('--max', '--maxlength', default=100, type=int, help='maximum length of password')
parser.add_argument('-n', '--numbers', type=bool, help='password must include numbers (default: false)')
parser.add_argument('-s', '--specialcharacters', type=bool, help='includes passwords with special characters (default: false)')

args = parser.parse_args()


def process_line_by_line():
    with open(args.wordlist, 'r') as read_stream:
        with open(args.target, 'w') as write_stream:
            count = 0
            for line in read_stream:
                password = line.replace('\r', '').replace('\n', '')
                passwordLength = len(password)
                if (args.min <= passwordLength and args.max >= passwordLength):
                    if(args.numbers is not True and hasNumbers(password)):
                        continue
                    
                    if(args.specialcharacters is not True and hasSpecialCharacters(password)):
                        continue

                    write_stream.write(line)
                    count += 1

    print(f'{count} of Passwords written.')

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def hasSpecialCharacters(inputString):
    return bool(re.findall('[^A-Za-z0-9]',inputString))

process_line_by_line()