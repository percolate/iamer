"""iamer

Manage your IAM rules in git.
Dump your existing IAM rules into human readable text files.
Load IAM rules off text files.

Usage:
    iamer load
    iamer dump

Options:
    -h --help   Show this screen.

"""
from docopt import docopt

from iamcloud import IamCloud


class IamFiles(object):
    """Representation of the local files mimicking IAM"""
    pass


def dump():
    """Dump the IAM rules into text files"""
    iam = IamCloud()
    iam.dump()


def load():
    """Load local text files into IAM rules on AWS"""
    print "TBD"


def main():
    """The main entry point"""
    args = docopt(__doc__)

    if args['dump']:
        dump()
    elif args['load']:
        load()
