from django.conf.urls import url
from .views import DropShipProductView, MemberDiscountView, SalesSummaryView, ProductView, ChildrenSaleItemView, \
    SalesAnalyzedView, PromotionView, CategoryView


route_list = [
    {
        'path': r'api/dropship',
        'view': DropShipProductView
    },
    #  Disable this view
    # {
    #     'path': r'api/discount/',
    #     'view': MemberDiscountView
    # },
    {
        'path': r'api/sales',
        'view': SalesSummaryView
    },
    {
        'path': r'api/sales_analyzed',
        'view': SalesAnalyzedView
    },
    {
        'path': r'api/products',
        'view': ProductView
    },
    {
        'path': r'api/children_saleitems',
        'view': ChildrenSaleItemView
    },
    {
        'path': r'api/promotion',
        'view': PromotionView
    },
    {
        'path': r'api/category',
        'view': CategoryView
    },
]
