from django.test import TestCase

# from branch.report import ExcelStockMovement
# from ecommerce.models import Product

# prod_list = Product.objects.filter(pcode__startswith='CCI').values_list('pcode', flat=True)
# branch_list = ['BKK01', 'BKK02', 'HY01', 'KL01', 'CRI01']
# for br in branch_list:
# for pd in prod_list:
#     excel = ExcelStockMovement(product=pd, branch='HQ', start='2018-12-01', end='2018-12-31')
#     excel.process_data()
#     excel.save_file()

# from ecommerce.models import SaleInvoice
# import datetime
# print('START !!! ', datetime.datetime.now())
# for b in ['BKK01', 'BKK02', 'CRI01', 'HY01', 'KL01', 'STHQ']:
#     print(b, datetime.datetime.now())
#     for item in SaleInvoice.objects.filter(sadate__range=('2019-01-01', '2019-01-15'), inv_code=b):
#         print(item)
# print('DONE !!! ', datetime.datetime.now())


# from ecommerce.report import SaleInvoiceForAccountingReport
# sobj=SaleInvoiceForAccountingReport(start='2019-03-01',end='2019-03-31')
# sobj.process_data()
# sobj.save_file()
# sobj=SaleInvoiceForAccountingReport(start='2019-02-01',end='2019-02-28')
# sobj.process_data()
# sobj.save_file()
# sobj=SaleInvoiceForAccountingReport(start='2019-01-01',end='2019-01-31')
# sobj.process_data()
# sobj.save_file()


# for i in instance:
#     if mc not in pool:
#         pool[mc] = {i["mcode"]: {i["month"].strftime("%Y-%m-%d"): {
#             i["sa_type"]: {"count": i["count"], "max": i["max"], "min": i["min"]}
#         }}}
#     else:
#         if i["mcode"] not in pool[mc]:
#             pool[mc][i["mcode"]] = {i["month"].strftime("%Y-%m-%d"): {
#                 i["sa_type"]: {"count": i["count"], "max": i["max"], "min": i["min"]}
#             }}
#         else:
#             if i["month"].strftime("%Y-%m-%d") not in pool[mc][i["mcode"]]:
#                 pool[mc][i["mcode"]][i["month"].strftime("%Y-%m-%d")] = {
#                     i["sa_type"]: {"count": i["count"], "max": i["max"], "min": i["min"]}
#                 }
#             else:
#                 if i["sa_type"] not in pool[mc][i["mcode"]][i["month"].strftime("%Y-%m-%d")]:
#                     pool[mc][i["mcode"]][i["month"].strftime("%Y-%m-%d")][i["sa_type"]] = {
#                         "count": i["count"], "max": i["max"], "min": i["min"]
#                     }
# return pool





