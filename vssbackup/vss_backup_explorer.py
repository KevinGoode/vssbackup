import os
from vssbackup.vss_xml_file_factory import VSSXMLFileFactory
from lxml import etree


class VSSBackupExplorer(object):
    """Constructor"""
    def __init__(self, backup_dir):
        self.backup_dir = backup_dir
        self.file_list = []

    def process(self):
        if not os.path.isdir(self.backup_dir):
            raise Exception("%s is not a directory" % self.backup_dir)
        self._get_files()
        self._verify_files()
        components = self._get_backup_components()
        components = self._get_backup_components_in_snap(components)
        return self._print_backup_components(components)

    def _get_files(self):
        # Get all files in directory and check they are backup or writer files
        files = [f for f in os.listdir(self.backup_dir) if os.path.isfile(os.path.join(self.backup_dir, f)) and '.xml' in f]
        if len(files) == 0:
            raise Exception("No xml files found. Xml files must have .xml extension")

        factory = VSSXMLFileFactory()
        for xml_file in files:
            file_instance = factory.create_instance(self.backup_dir + xml_file)
            # Not interested in other XML files (eg Manifest.xml) so need to check for not None
            if file_instance:
                self.file_list.append(file_instance)

    def _verify_files(self):
        # Perform integrity checks on files
        self._verify_one_backup_file()
        for xml_file in self.file_list:
            xml_file.verify()

    def _verify_one_backup_file(self):
        backup_file = None
        count = 0
        for xml_file in self.file_list:
            if xml_file.is_backup_file():
                backup_file = xml_file
                count += 1
        if count != 1:
            raise Exception("Expected 1 backup file. Found %d" % count)

        return backup_file

    def _get_backup_components(self):
        components = []
        for xml_file in self.file_list:
            if not xml_file.is_backup_file():
                components.append(xml_file.get_backup_components())
        return components

    def _get_backup_components_in_snap(self, components):
        backup_components = []
        backup_file = self._verify_one_backup_file()
        writer_components = backup_file.get_writer_components()
        for writer_component in writer_components:
            for component in components:
                if writer_component['writer_id'] == component['writer_id'] and writer_component['instance_id'] == component['instance_id']:
                    backup_components.append(component['components'])
                    break
        return backup_components

    @staticmethod
    def _print_backup_components(backup_components):
        return_str = "<BACKUP_LOCATIONS>\n"
        for backup_component in backup_components:
            for component in backup_component:
                return_str += etree.tostring(component, pretty_print=True)
        return_str += "</BACKUP_LOCATIONS>\n"
        return return_str
   