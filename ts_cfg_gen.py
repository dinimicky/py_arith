#!/usr/bin/env python
# encoding: utf-8
'''
ts_cfg_gen -- shortdesc

ts_cfg_gen is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2014 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import re
import importlib
from os import path

from optparse import OptionParser

__all__ = []
__version__ = 0.1
__date__ = '2014-08-15'
__updated__ = '2014-08-15'

DEBUG = 0
TESTRUN = 0
PROFILE = 0

def main(argv=None):
    '''Command line options.'''

    program_version = "v0.1"
    program_build_date = "%s" % __updated__

    program_version_string = '%%prog %s (%s)' % (program_version, program_build_date)
    #program_usage = '''usage: spam two eggs''' # optional - will be autogenerated by optparse
    program_longdesc = '''''' # optional - give further explanation about what the program does
    program_license = "Copyright 2014 user_name (organization_name)                                            \
                Licensed under the Apache License 2.0\nhttp://www.apache.org/licenses/LICENSE-2.0"

    if argv is None:
        argv = sys.argv[1:]

    # setup option parser
    parser = OptionParser(version=program_version_string, epilog=program_longdesc, description=program_license)
    parser.add_option("-c", "--envCfg", dest="envCfg", help="set environment configuraton file", metavar="FILE")
    parser.add_option("-t", "--tsTemplate", dest="tsTemplate", help="set the test suite template file", metavar="FILE")
    
    # process options
    (opts, _args) = parser.parse_args(argv)
    print(opts)
    if (not opts.envCfg) and (not opts.tsTemplate):
        parser.error('options -conf & -temp is mandatory and requires an argument')

    # MAIN BODY #
    with open(opts.tsTemplate, "r") as tsTempFh:
        tsTemp = tsTempFh.read()
    
    p = re.compile('\$([a-zA-Z0-9_]+)\$')
    
    opts.envCfg = path.basename(opts.envCfg)
    mpath = path.dirname(path.abspath(opts.envCfg))
    if mpath not in sys.path:
        sys.path.append(mpath)
    if opts.envCfg[-3:] == ".py":
        opts.envCfg = opts.envCfg[:-3]

    m = importlib.import_module(opts.envCfg)
    parameters = [ getattr(m, c.group(1)) for c in p.finditer(tsTemp)]
        
    newTsTemp = p.sub('%s', tsTemp)
    print(newTsTemp % tuple(parameters))

if __name__ == "__main__":
    sys.exit(main())