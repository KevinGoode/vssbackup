import sys

import os
from vssbackup.vss_backup_explorer import VSSBackupExplorer
# Run from command line as:
# ../workspace/vssbackup>  python -m vssbackup.main /home/rmc-dev/workspace/vssbackup/data/no_sql/


def main(args):
    general = """-----------------------------------------------------------------------
vssbackup scans a directory of xml files generated after a MS Windows
diskshadow snapshot and generates a single XML file that contains a
list of quiesced files that were part of the snapshot.

The single XML file simply contains a concatenated list of the
'BACKUP_LOCATIONS' elements in the VSS writer files for all writers
that participated in the snapshot. Since some locations are directories
with/without the 'recursive' flag, to have a definitive list of quiesced
files requires the snapshot to be mounted. In future versions this utility
will take a second argument (mount path of snapshot) and provide this
definitive list.
-----------------------------------------------------------------------
"""
    if len(args) != 1:
        print general
        print "ERROR! : Pass directory containing backup and writer metadata as argument\n"
        exit(-1)
    if not os.path.isdir(args[0]):
        print general
        print "ERROR!: %s is NOT a directory\n" % args[0]
        exit(-1)
    explorer = VSSBackupExplorer(args[0])
    try:
        print explorer.process()
    except Exception as ex:
        print ex
        exit(-1)


if __name__ == '__main__':
    main(sys.argv[1:])
