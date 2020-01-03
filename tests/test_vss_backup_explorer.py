
import unittest
from vssbackup.vss_backup_explorer import VSSBackupExplorer


class TestBackupExplorer(unittest.TestCase):

    @staticmethod
    def test_all_files_ok_sql():
        explorer = VSSBackupExplorer("../data/with_sql/")
        # No not check return. Just checking files validate
        explorer.process()

    @staticmethod
    def test_all_files_ok_nosql():
        # Constructor validates dir and contents
        explorer = VSSBackupExplorer("../data/with_sql/")
        # No not check return. Just checking files validate
        explorer.process()


if __name__ == '__main__':
    unittest.main()
