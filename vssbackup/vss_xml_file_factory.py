from vssbackup.vss_xml_files import VSSBackupXMLFile
from vssbackup.vss_xml_files import VSSWriterXMLFile


class VSSXMLFileFactory(object):
    """Constructor"""
    def __init__(self):
        pass

    @staticmethod
    def create_instance(filename):
        xml_file = None
        if "WM" in filename and filename.endswith(".xml"):
            xml_file = VSSWriterXMLFile(filename)
        elif "BCD" in filename and filename.endswith(".xml"):
            xml_file = VSSBackupXMLFile(filename)  # pylint: disable=redefined-variable-type
        return xml_file
