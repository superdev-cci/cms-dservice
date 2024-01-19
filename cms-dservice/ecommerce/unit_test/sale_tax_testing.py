from ecommerce.report import SaleInvoiceForAccountingReport


def main():
    sobj = SaleInvoiceForAccountingReport(start='2019-07-01', end='2019-07-31')
    sobj.process_data()
    sobj.save_file()