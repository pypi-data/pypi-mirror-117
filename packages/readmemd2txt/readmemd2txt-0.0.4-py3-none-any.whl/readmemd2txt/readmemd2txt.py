#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#    readmemd2txt Copyright (C) 2021 suizokukan
#    Contact: suizokukan _A.T._ orange dot fr
#
#    This file is part of readmemd2txt.
#    readmemd2txt is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    readmemd2txt is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with readmemd2txt.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
"""
    readmemd2txt.py

    Transform a README.md file into a pure text.
"""
import argparse
import os.path
import re

# Even if Pylint disagrees, module readmemd2txt.aboutproject
# can be imported.
# pylint: disable=no-name-in-module
# pylint: disable=import-error
from readmemd2txt.aboutproject import __projectname__, __version__


PARSER = \
    argparse.ArgumentParser(description="Transform a README.md file into a pure text.",
                            epilog=f"{__projectname__}: {__version__}",
                            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
PARSER.add_argument('--version', '-v',
                    action='version',
                    version=f"{__projectname__}: {__version__}",
                    help="Show the version and exit")
PARSER.add_argument('--inputfile',
                    action='store',
                    default="README.md",
                    help="Input file")
PARSER.add_argument('--linemaxlength',
                    action='store',
                    default="79",
                    help="Lines' maximal length")

ARGS = PARSER.parse_args()


REGEX_LINK = re.compile(r"\[(?P<text>[^\[\]]+)\](?P<link>\([^\(\)]+\))")

REGEX_TRIPLEGRAVEACCENT = re.compile("```(?P<text>[^`]+)```", re.MULTILINE)

REGEX_INITIALSHARP = re.compile(r"^#+\s*(?P<text>[^#]+)")


def add_a_prefix(string,
                 prefix):
    """
        add_a_prefix()

        Add a prefix at the beginning of every line in <string>.
        This methods only support "\n" as the only EOF character.

        ________________________________________________________________________

        ARGUMENTS:
        o  (str)string, something like "line1\nline2"
        o  (str)prefix

        RETURNED VALUE: (str)<string> with a prefix added at the beginning of each
                        line found in <string>.
    """
    res = []
    for line in string.split("\n"):
        res.append(prefix + line)
    return "\n".join(res)


def split_by_length(string,
                    maxsize):
    """
        split_by_length()

        Split <string> in sub-strings whose length can not be greater than <maxsize>
        _______________________________________________________________________

        ARGUMENTS:
        o  (str)string, the string to be splitted
        o  (int)maxsize
    """
    if len(string)==0:
        return ("",)
    return (string[i:i+maxsize] for i in range(0, len(string), maxsize))


def sub__regex_link(match):
    """
        sub__regex_link()

        [text](link) -> text

        _______________________________________________________________________

        ARGUMENT: (re.Match) match

        RETURNED VALUE: (str)the expected string replacing <match>.
    """
    return match.group("text")


def sub__triple_grave_accent(match):
    """
        sub__triple_grave_accent()

        ```text``` -> text

        _______________________________________________________________________

        ARGUMENT: (re.Match) match

        RETURNED VALUE: (str)the expected string replacing <match>.
    """
    return add_a_prefix(match.group("text"), prefix="  | ")


def sub__regex_initial_sharp(match):
    """
        sub__regex_initial_sharp()

        ###text -> text

        _______________________________________________________________________

        ARGUMENT: (re.Match) match

        RETURNED VALUE: (str)the expected string replacing <match>.
    """
    return match.group("text")


def main():
    """
        main()

        Main entrypoint.
    """
    if not os.path.exists(ARGS.inputfile):
        print(f"Missing file {ARGS.inputfile}.")
        return

    res = [f"Text automatically generated from '{ARGS.inputfile}' .",
           ""]

    with open(ARGS.inputfile, encoding="utf-8") as inputfile:
        for line in inputfile:
            if len(line.strip()) == 0:
                res.append("")
            else:
                line = re.sub(REGEX_LINK, sub__regex_link, line)
                line = re.sub(REGEX_INITIALSHARP, sub__regex_initial_sharp, line)
                line = line.replace("**", "")
                if len(line.strip()) != 0:
                    res.append(line.rstrip())

    res = "\n".join(res)

    res = re.sub(REGEX_TRIPLEGRAVEACCENT, sub__triple_grave_accent, res)
    res = res.replace("`", "")  # simple `, ``` being already deleted

    for line in res.split("\n"):
        for _line in split_by_length(line,
                                     maxsize=int(ARGS.linemaxlength)):
            print(_line.rstrip())


if __name__ == '__main__':
    main()
