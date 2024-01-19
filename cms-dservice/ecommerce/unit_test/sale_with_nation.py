from ecommerce.report.sale.sale_with_member_nation import SaleInvoiceSummaryWithNation
from ecommerce.report.excel.sale.sale_with_nation import SaleInvoiceSummaryWithNationExcel


def test_sale_with_nation():
    report = SaleInvoiceSummaryWithNationExcel(start='2019-01-01', end='2019-12-31',
                                               nation=(
                                                   ('LA', 'Lao'), ('TH', 'Thailand'), ('MY', 'Malaysia')
                                               ))
    report.process_data()
    report.save_file()
