from django.conf.urls import url
from .views import *

route_list = [
    {
        'path': r'api/adjust/stock',
        'view': StockAdjustView
    },
    {
        'path': r'api/branch/stock',
        'view': BranchStockView
    },
    {
        'path': r'api/branches',
        'view': BranchView
    },
    {
        'path': r'api/stock/movement',
        'view': StockMovementView
    },
    {
        'path': r'api/branch/import',
        'view': BranchImportStatementView
    },
    {
        'path': r'api/branch/export',
        'view': BranchExportStatementView
    },
    {
        'path': r'api/snap_remaining',
        'view': SnapRemainingView
    },
    {
        'path': r'api/branch/transfer_hq',
        'view': BranchTransferHqView
    },
]
