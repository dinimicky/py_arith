#!/usr/bin/env python
# encoding: utf-8
'''
list_src_file -- shortdesc

list_src_file is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2014 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os

from optparse import OptionParser

__all__ = []
__version__ = 0.1
__date__ = '2014-08-19'
__updated__ = '2014-08-19'

DEBUG = 0
TESTRUN = 0
PROFILE = 0
import fnmatch
def get_src_dirs(directory, extension):
    paths = set()
    for root, _dirs, files in os.walk(directory):
        for filepath in files:
            filepath = os.path.join(root,filepath)
            if fnmatch.fnmatch(filepath, extension):
                p = os.path.dirname(filepath)
                paths.add(p)
    return paths

def print_paths(paths, sep=";"):
    s = ''
    for p in paths:
        s += p + sep
    print(s)
def main(argv=None):
    '''Command line options.'''

    program_name = os.path.basename(sys.argv[0])
    program_version = "v0.1"
    program_build_date = "%s" % __updated__

    program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)
    #program_usage = '''usage: spam two eggs''' # optional - will be autogenerated by optparse
    program_longdesc = '''''' # optional - give further explanation about what the program does
    program_license = "Copyright 2014 user_name (organization_name)                                            \
                Licensed under the Apache License 2.0\nhttp://www.apache.org/licenses/LICENSE-2.0"

    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = OptionParser(version=program_version_string, epilog=program_longdesc, description=program_license)
        parser.add_option("-d", "--directory", dest="directory", help="set input path [default: %default]", metavar="FILE")
        parser.add_option("-x", "--extension", dest="extension", help="set output path [default: %default]", metavar="FILE")


        # set defaults
        parser.set_defaults(outfile="./out.txt", infile="./in.txt")

        # process options
        (opts, _args) = parser.parse_args(argv)

        # MAIN BODY #
        print_paths(get_src_dirs(opts.directory, opts.extension))

    except Exception as e:
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2


if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'list_src_file_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())