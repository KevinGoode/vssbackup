import os
from lxml import etree, objectify
from lxml.etree import XMLSyntaxError


class VSSXMLFileBase(object):
    """Constructor"""
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_data = ""
        with open(file_name) as f:
            self.file_data = f.read()

    def verify(self):
        schema_file = self._get_schema()  # pylint: disable=maybe-no-member
        try:
            schema = etree.XMLSchema(file=schema_file)
            parser = objectify.makeparser(schema=schema)
            objectify.fromstring(self.file_data, parser)
        except XMLSyntaxError as ex:
            excep_str = "XML file % s does not validate against schema %s\n" % (self.file_name, schema_file)
            excep_str += "ERROR %s \n" % str(ex)
            raise Exception(excep_str)


class VSSXMLFile(object):
    """Interface type class that mandates methods are implemented (at call time)"""
    def is_backup_file(self):  # pylint: disable=R0201
        raise Exception("Not implemented")

    def _get_schema(self):  # pylint: disable=R0201
        raise Exception("Not implemented")

    def _parse(self):  # pylint: disable=R0201
        raise Exception("Not implemented")


class VSSBackupXMLFile(VSSXMLFile, VSSXMLFileBase):
    """Constructor"""
    def __init__(self, file_name):
        VSSXMLFileBase.__init__(self, file_name)
        VSSXMLFile.__init__(self)

    def is_backup_file(self):
        return True

    def _get_schema(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        return current_path + "/../schemas/BCDocument.xsd"

    def get_writer_components(self):
        writer_components = []
        root = etree.parse(self.file_name).getroot()
        # NOTE NEED to qualify tag name See https://docs.python.org/2.7/library/xml.etree.elementtree.html#parsing-xml
        components = root.findall('./{x-schema:#VssComponentMetadata}WRITER_COMPONENTS')
        for component in components:
            writer_id = component.get('writerId')
            instance_id = component.get('instanceId')
            writer_components.append({"writer_id": writer_id, "instance_id": instance_id})
        return writer_components


class VSSWriterXMLFile(VSSXMLFile, VSSXMLFileBase):
    """Constructor"""
    def __init__(self, file_name):
        VSSXMLFileBase.__init__(self, file_name)
        VSSXMLFile.__init__(self)

    def is_backup_file(self):
        return False

    def get_backup_components(self, debug=False):
        root = etree.parse(self.file_name).getroot()
        # NOTE NEED to qualify tag name See https://docs.python.org/2.7/library/xml.etree.elementtree.html#parsing-xml
        components = root.findall('./{x-schema:#VssWriterMetadataInfo}BACKUP_LOCATIONS/')
        identification = root.findall('./{x-schema:#VssWriterMetadataInfo}IDENTIFICATION')
        writer_id = identification[0].get('writerId')
        instance_id = identification[0].get('instanceId')
        if debug:
            for component in components:
                print etree.tostring(component, pretty_print=True)
        return {"writer_id": writer_id, "instance_id": instance_id, "components": components}

    def _get_schema(self):
        current_path = os.path.dirname(os.path.realpath(__file__))
        return current_path + "/../schemas/WMX.xsd"
