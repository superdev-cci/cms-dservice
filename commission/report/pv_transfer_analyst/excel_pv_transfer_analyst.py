# from openpyxl import Workbook
# from member.models import Member
# from core.mixin.month_mixin import MonthMixIn
# from datetime import datetime
# from collections import OrderedDict
#
# from openpyxl.styles.numbers import FORMAT_NUMBER_COMMA_SEPARATED1
#
# from core.report.excel import ExcelTemplateReport
# from .pv_transfer_analyst import SummaryPvTransferAgencyAnalyst, \
#     SummaryPvTransferReceiverAnalyst, SummaryPvTransferAnalyst
#
#
# class ExcelSummaryPvTransferAnalyst(MonthMixIn):
#     # template_file = './templates/report/commission/summary_commission.xlsx'
#
#     class Meta:
#         title = 'Pv Transfer Analyst'
#         file_name = 'pv_transfer_analyst'
#         head_file = 'Pv Transfer Analyst'
#         content_start_col = 1
#         content_start_row = 8
#         head_start_col = 3
#         head_start_row = 7
#
#     def __init__(self, *args, **kwargs):
#         super(ExcelSummaryPvTransferAnalyst, self).__init__(*args, **kwargs)
#         self.agency_view = SummaryPvTransferAgencyAnalyst(*args, **kwargs)
#         self.receiver_view = SummaryPvTransferReceiverAnalyst(*args, **kwargs)
#         self.report = SummaryPvTransferAnalyst(*args, **kwargs)
#         self.start = kwargs.get('start', None)
#         self.end = kwargs.get('end', None)
#
#     def create_summary_head(self):
#         month_list = self.month_diff_range(self.end, self.start)
#     #     self.work_sheet['E4'] = self.report.week.start.strftime('%Y-%m-%d')
#     #     self.work_sheet['G4'] = self.report.week.end.strftime('%Y-%m-%d')
#     #     self.work_sheet['E5'] = self.report.week.get_type
#         # super(ExcelSummaryCommission, self).create_head()
#
#     # def build_row_meta(self, row_index, data, **kwargs):
#     #     meta = OrderedDict([
#     #         ('no', {'data': row_index, 'alignment': self.style['align_center']}),
#     #         ('date', {'data': data['time'], 'alignment': self.style['align_center']}),
#     #         ('mcode', {'data': data['mcode'], 'alignment': self.style['align_center']}),
#     #         ('name', {'data': data['name'], 'alignment': self.style['align_center']}),
#     #         ('total', {'data': data['total'], 'alignment': self.style['align_right'],
#     #                    'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
#     #         ('ws_bonus', {'data': data['ws'], 'alignment': self.style['align_right'],
#     #                       'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
#     #         ('fast_bonus', {'data': data['fast'], 'alignment': self.style['align_right'],
#     #                         'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
#     #         ('resale', {'data': data['resale'], 'alignment': self.style['align_right'],
#     #                     'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
#     #         ('matching', {'data': data['matching'], 'alignment': self.style['align_right'],
#     #                       'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
#     #         ('all_sales', {'data': data['all_sales'], 'alignment': self.style['align_right'],
#     #                        'number_format': FORMAT_NUMBER_COMMA_SEPARATED1}),
#     #     ])
#     #     return meta
#     #
#     # def fill_row(self, row_index, data, *args, **kwargs):
#     #     row = kwargs.get('row')
#     #     current_col = self.Meta.content_start_col
#     #     count = row_index
#     #     for k_time, v in data['data'].items():
#     #         cell = self.get_cell(current_col, row)
#     #         cell.border = self.style['full_border']
#     #         current_meta = {
#     #             'mcode': data['mcode'],
#     #             'name': data['name'],
#     #             'time': k_time,
#     #             **v
#     #         }
#     #         meta = self.build_row_meta(count, current_meta, **kwargs)
#     #         for write_key, write_value in meta.items():
#     #             cell = self.fill_data(cell, write_value)
#     #         row += 1
#     #         count += 1
#     #     return count
#     #
#     # def process_data(self):
#     #     count = 1
#     #     current_row = self.Meta.content_start_row
#     #     self.create_head()
#     #     for k, v in self.report.total.items():
#     #         count += self.fill_row(count, v, row=current_row)
#     #         current_row += 1
#
#     def main(date_tuple):
#         # date_tuple = ("2019-09-01", "2019-11-30")
#         startdate = datetime.strptime(date_tuple[0], "%Y-%m-%d")
#         enddate = datetime.strptime(date_tuple[1], "%Y-%m-%d")
#
#         pool_sum = pull_summary(date_tuple)
#         pool_mcode = pull_summary_mcode(date_tuple)
#         pool_data = pull_data(date_tuple)
#         wb = Workbook()
#         sht = wb.active
#         sht.title = "Summary_AG_view"
#         sht.merge_cells("A1:A2")
#         sht["A1"] = "รหัสผู้ทำรายการ"
#         sht.merge_cells("B1:B2")
#         sht["B1"] = "ชื่อผู้ทำรายการ"
#         start_head_col = 3
#         bill_type_shift_index = {"y200": 1, "yf": 2, "ym": 3, "a/am": 4}
#         month_shift_index = {}
#         start_row = 3
#         for index, m in enumerate(month_list):
#             month_shift_index[m.strftime("%Y-%m")] = index
#         for month in month_list:
#             sht.merge_cells(start_row=1, start_column=start_head_col, end_row=1, end_column=(start_head_col + 3))
#             sht.cell(column=start_head_col, row=1, value=month.strftime("%b-%y"))
#             sht.cell(column=start_head_col, row=2, value="Y200")
#             sht.cell(column=(start_head_col + 1), row=2, value="YF")
#             sht.cell(column=(start_head_col + 2), row=2, value="YM")
#             sht.cell(column=(start_head_col + 3), row=2, value="A/AM")
#             start_head_col += 4
#         for uid, data_list in pool_sum.items():
#             for bill_type, query_list in data_list.items():
#                 for i in query_list:
#                     sht.cell(column=1, row=start_row, value=uid[0])
#                     sht.cell(column=2, row=start_row, value=uid[1])
#                     current_col = 2 + (
#                             bill_type_shift_index[bill_type] + (month_shift_index[i["month"].strftime("%Y-%m")] * 4))
#                     if sht.cell(column=current_col, row=start_row).value is None:
#                         sht.cell(column=current_col, row=start_row, value=i["count"])
#                     else:
#                         sht.cell(column=current_col, row=start_row).value += i["count"]
#             start_row += 1
#         for bill_type, data_dict in pool_data.items():
#             if bill_type == "a/am":
#                 ws = wb.create_sheet("a_am")
#             else:
#                 ws = wb.create_sheet(bill_type)
#             write_on_sheet(ws, data_dict)
#         msht = wb.create_sheet("Summary_mcode_view", 1)
#         msht.merge_cells("A1:A2")
#         msht["A1"] = "รหัสผู้ทำรายการ"
#         msht.merge_cells("B1:B2")
#         msht["B1"] = "ชื่อผู้ทำรายการ"
#         start_head_col = 3
#         for month in month_list:
#             msht.merge_cells(start_row=1, start_column=start_head_col, end_row=1, end_column=(start_head_col + 3))
#             msht.cell(column=start_head_col, row=1, value=month.strftime("%b-%y"))
#             msht.cell(column=start_head_col, row=2, value="Y200")
#             msht.cell(column=(start_head_col + 1), row=2, value="YF")
#             msht.cell(column=(start_head_col + 2), row=2, value="YM")
#             msht.cell(column=(start_head_col + 3), row=2, value="A/AM")
#             start_head_col += 4
#         start_row = 3
#         for mcode, data_dict in pool_mcode.items():
#             for bill_type, item_list in data_dict.items():
#                 for i in item_list:
#                     msht.cell(column=1, row=start_row, value=i["mcode"])
#                     msht.cell(column=2, row=start_row, value=i["name_t"])
#                     current_col = 2 + (
#                             bill_type_shift_index[bill_type] + (month_shift_index[i["month"].strftime("%Y-%m")] * 4))
#                     if msht.cell(column=current_col, row=start_row).value is None:
#                         msht.cell(column=current_col, row=start_row, value=i["count"])
#                     else:
#                         msht.cell(column=current_col, row=start_row).value += i["count"]
#             start_row += 1
#         wb.save("/home/jew/Desktop/PvTransferAnalyst_v4.xlsx")
#
#     @property
#     def file_name(self):
#         name = '{}'.format(
#             self.Meta.file_name + '_' + self.report.week.mcode + '_' + self.report.week.start.strftime(
#                 '%Y-%m-%d') + '_' + self.report.week.end.strftime('%Y-%m-%d'))
#         return '{}.xlsx'.format(name)
#
#
# def write_on_sheet(sheet, data_dict):
#     sheet["A1"] = "รหัสผู้ทำรายการ"
#     sheet["B1"] = "ชื่อผู้ทำรายการ"
#     sheet["C1"] = "รหัสผู้รับ"
#     sheet["D1"] = "ชื่อผู้รับ"
#     sheet["E1"] = "month"
#     sheet["F1"] = "bill_type"
#     sheet["G1"] = "จำนวนรายการ"
#     sheet["H1"] = "avg"
#     sheet["I1"] = "min"
#     sheet["J1"] = "max"
#     start_row = 2
#     for uid, data_list in data_dict.items():
#         for data in data_list:
#             sheet.cell(column=1, row=start_row, value=uid[0])
#             sheet.cell(column=2, row=start_row, value=uid[1])
#             sheet.cell(column=3, row=start_row, value=data["mcode"])
#             sheet.cell(column=4, row=start_row, value=data["member__name_t"])
#             sheet.cell(column=5, row=start_row, value=data["month"].strftime("%Y-%m"))
#             sheet.cell(column=6, row=start_row, value=data["sa_type"])
#             sheet.cell(column=7, row=start_row, value=data["count"])
#             sheet.cell(column=8, row=start_row, value=data["avg"])
#             sheet.cell(column=9, row=start_row, value=data["min"])
#             sheet.cell(column=10, row=start_row, value=data["max"])
#             start_row += 1
#
#
# def main(date_tuple):
#     # date_tuple = ("2019-09-01", "2019-11-30")
#     startdate = datetime.strptime(date_tuple[0], "%Y-%m-%d")
#     enddate = datetime.strptime(date_tuple[1], "%Y-%m-%d")
#     month_list = MonthMixIn.month_diff_range(enddate, startdate)
#     # pool_sum = pull_summary(date_tuple)
#     # pool_mcode = pull_summary_mcode(date_tuple)
#     # pool_data = pull_data(date_tuple)
#     wb = Workbook()
#     sht = wb.active
#     sht.title = "Summary_AG_view"
#     sht.merge_cells("A1:A2")
#     sht["A1"] = "รหัสผู้ทำรายการ"
#     sht.merge_cells("B1:B2")
#     sht["B1"] = "ชื่อผู้ทำรายการ"
#     start_head_col = 3
#     bill_type_shift_index = {"y200": 1, "yf": 2, "ym": 3, "a/am": 4}
#     month_shift_index = {}
#     start_row = 3
#     for index, m in enumerate(month_list):
#         month_shift_index[m.strftime("%Y-%m")] = index
#     for month in month_list:
#         sht.merge_cells(start_row=1, start_column=start_head_col, end_row=1, end_column=(start_head_col + 3))
#         sht.cell(column=start_head_col, row=1, value=month.strftime("%b-%y"))
#         sht.cell(column=start_head_col, row=2, value="Y200")
#         sht.cell(column=(start_head_col + 1), row=2, value="YF")
#         sht.cell(column=(start_head_col + 2), row=2, value="YM")
#         sht.cell(column=(start_head_col + 3), row=2, value="A/AM")
#         start_head_col += 4
#     for uid, data_list in pool_sum.items():
#         for bill_type, query_list in data_list.items():
#             for i in query_list:
#                 sht.cell(column=1, row=start_row, value=uid[0])
#                 sht.cell(column=2, row=start_row, value=uid[1])
#                 current_col = 2 + (
#                         bill_type_shift_index[bill_type] + (month_shift_index[i["month"].strftime("%Y-%m")] * 4))
#                 if sht.cell(column=current_col, row=start_row).value is None:
#                     sht.cell(column=current_col, row=start_row, value=i["count"])
#                 else:
#                     sht.cell(column=current_col, row=start_row).value += i["count"]
#         start_row += 1
#     for bill_type, data_dict in pool_data.items():
#         if bill_type == "a/am":
#             ws = wb.create_sheet("a_am")
#         else:
#             ws = wb.create_sheet(bill_type)
#         write_on_sheet(ws, data_dict)
#     msht = wb.create_sheet("Summary_mcode_view", 1)
#     msht.merge_cells("A1:A2")
#     msht["A1"] = "รหัสผู้ทำรายการ"
#     msht.merge_cells("B1:B2")
#     msht["B1"] = "ชื่อผู้ทำรายการ"
#     start_head_col = 3
#     for month in month_list:
#         msht.merge_cells(start_row=1, start_column=start_head_col, end_row=1, end_column=(start_head_col + 3))
#         msht.cell(column=start_head_col, row=1, value=month.strftime("%b-%y"))
#         msht.cell(column=start_head_col, row=2, value="Y200")
#         msht.cell(column=(start_head_col + 1), row=2, value="YF")
#         msht.cell(column=(start_head_col + 2), row=2, value="YM")
#         msht.cell(column=(start_head_col + 3), row=2, value="A/AM")
#         start_head_col += 4
#     start_row = 3
#     for mcode, data_dict in pool_mcode.items():
#         for bill_type, item_list in data_dict.items():
#             for i in item_list:
#                 msht.cell(column=1, row=start_row, value=i["mcode"])
#                 msht.cell(column=2, row=start_row, value=i["name_t"])
#                 current_col = 2 + (
#                         bill_type_shift_index[bill_type] + (month_shift_index[i["month"].strftime("%Y-%m")] * 4))
#                 if msht.cell(column=current_col, row=start_row).value is None:
#                     msht.cell(column=current_col, row=start_row, value=i["count"])
#                 else:
#                     msht.cell(column=current_col, row=start_row).value += i["count"]
#         start_row += 1
#     wb.save("/home/jew/Desktop/PvTransferAnalyst_v4.xlsx")
#
#
#
#
#
# # from openpyxl import Workbook
# # from commission.report.pv_transfer_analyst.pv_transfer_analyst import PvTransferInnerOuterAnalyst, \
# #     SummaryPvTransferInOutAnalyst
# #
# #
# # def write_column_set(sheet, start_row, start_col, data_list):
# #     for i in data_list:
# #         # sheet.cell(column=start_col, row=start_row, value=i["mcode"])
# #         # sheet.cell(column=start_col + 1, row=start_row, value=i["count"])
# #         # sheet.cell(column=start_col + 2, row=start_row, value=i["min"])
# #         # sheet.cell(column=start_col + 3, row=start_row, value=i["max"])
# #         # sheet.cell(column=start_col + 4, row=start_row, value=i["sum_pv"])
# #         sheet.cell(column=start_col, row=start_row, value=i["count"])
# #         sheet.cell(column=start_col + 1, row=start_row, value=i["min"])
# #         sheet.cell(column=start_col + 2, row=start_row, value=i["max"])
# #         sheet.cell(column=start_col + 3, row=start_row, value=i["sum_pv"])
# #         start_row += 1
# #
# #
# # def write_on_sheet(sheet, ag_code, ag_name, start_row, data_dict):
# #     sheet.cell(column=1, row=start_row, value=ag_code)
# #     sheet.cell(column=2, row=start_row, value=ag_name)
# #     # write_column_set(sheet, start_row, 3, list(data_dict["all_bill"]))
# #     # write_column_set(sheet, start_row, 8, list(data_dict["inner_bill"]))
# #     # write_column_set(sheet, start_row, 13, list(data_dict["outer_bill"]))
# #     write_column_set(sheet, start_row, 3, list(data_dict["all_bill"]))
# #     write_column_set(sheet, start_row, 7, list(data_dict["inner_bill"]))
# #     write_column_set(sheet, start_row, 11, list(data_dict["outer_bill"]))
# #
# #
# # def main():
# #     summary = SummaryPvTransferInOutAnalyst(start='2019-05-01', end='2019-11-30').total
# #     # report = PvTransferInnerOuterAnalyst(start='2019-05-01', end='2019-11-30').total
# #     wb = Workbook()
# #     sht = wb.active
# #     sht.title = "Y200"
# #     row_start = 3
# #     # for ag_code, data_list in report.items():
# #     for ag_code, data_list in summary.items():
# #         write_on_sheet(sht, ag_code, data_list["name"], row_start, data_list["y200"])
# #         row_start = sht.max_row + 1
# #     sht2 = wb.create_sheet("Y")
# #     row_start = 3
# #     # for ag_code, data_list in report.items():
# #     for ag_code, data_list in summary.items():
# #         write_on_sheet(sht2, ag_code, data_list["name"], row_start, data_list["y"])
# #         row_start = sht2.max_row + 1
# #     sht3 = wb.create_sheet("A_AM")
# #     row_start = 3
# #     # for ag_code, data_list in report.items():
# #     for ag_code, data_list in summary.items():
# #         write_on_sheet(sht3, ag_code, data_list["name"], row_start, data_list["a/am"])
# #         row_start = sht3.max_row + 1
# #     # wb.save("/home/jew/Desktop/PvTransferInOutAnalyst_Person_V2.xlsx")
# #     wb.save("/home/jew/Desktop/PvTransferInOutAnalyst_Summary_V2.xlsx")
