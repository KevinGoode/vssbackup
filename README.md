# VSSBACKUP
This folder contains vssbackup code that scans a directory of xml files generated after a MS Windows diskshadow snapshot and generates a single XML file that contains a list of quiesced files that were part of the snapshot.

The single XML file simply contains a concatenated list of the
'BACKUP_LOCATIONS' elements in the VSS writer files for all writers
that participated in the snapshot. Since some locations are directories
with/without the 'recursive' flag, to have a definitive list of quiesced
files requires the snapshot to be mounted. In future versions this utility
will take a second argument (mount path of snapshot) and provide this
definitive list.

## Steps to Setup
See Setup.md

## Steps to Run
Best way is to run from gui

1. From eclipse select file gui/main.py and select menu 'Run/Run'

2. Click on 'Select Directory' and select a directory (data/no_sql or data/with_sql)
   
3. See file list in tree

## Notes

