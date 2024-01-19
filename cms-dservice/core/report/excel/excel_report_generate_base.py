from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook


class GenerateExcel(object):
    """
    This's a class base to create excel object with method to save as excel file or response via http request.

    Attributes:
        wb (:obj:`excel object`): an excel workbook object create by `Openpyxl` Library
    """
    def __init__(self, *args, **kwargs):
        self.wb = Workbook()

    @property
    def response_file(self):
        """
        a method for response file via http request

        :return: excel object
        """
        return save_virtual_workbook(self.wb)

    def save_file(self):
        """
        a method for save an excel file to local machine path

        :return: excel file
        """
        self.wb.save(self.file_name)

    @property
    def file_name(self):
        """
        a method to verified an excel object that have a filename
        """
        raise NotImplementedError('`file_name` must be implemented.')
