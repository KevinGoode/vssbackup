import os
import unittest
from vssbackup.vss_xml_files import VSSBackupXMLFile
from vssbackup.vss_xml_files import VSSWriterXMLFile


class TestVSSXMLFiles(unittest.TestCase):

    def test_validate_backup_document_sql(self):
        self.validate_bck_in_dir("../data/with_sql/")

    def test_validate_backup_document_no_sql(self):
        self.validate_bck_in_dir("../data/no_sql/")

    def test_validate_writer_document_sql(self):
        self.validate_wms_in_dir("../data/with_sql/")

    def test_validate_writer_document_no_sql(self):
        self.validate_wms_in_dir("../data/no_sql/")

    @staticmethod
    def test_get_backup_components():
        backup_file = VSSWriterXMLFile("../data/no_sql/WM1.xml")
        backup_file.get_backup_components(debug=True)

    @staticmethod
    def validate_wms_in_dir(directory):
        print "Verifying WM files in directory %s\n" % directory
        for filename in os.listdir(directory):
            if filename.startswith("WM") and filename.endswith(".xml"):
                print "....Verifying %s\n" % filename
                backup_file = VSSWriterXMLFile(directory + filename)
                backup_file.verify()

    @staticmethod
    def validate_bck_in_dir(directory):
        print "Verifying BCK files in directory %s\n" % directory
        filename = directory + "BCDocument.xml"
        print "....Verifying %s\n" % filename
        backup_file = VSSBackupXMLFile(filename)
        backup_file.verify()


if __name__ == '__main__':
    unittest.main()
