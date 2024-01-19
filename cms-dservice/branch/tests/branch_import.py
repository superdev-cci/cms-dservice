from django.test import TestCase


# from branch.models import BranchGoodsImportStatement

class BranchImportTestCase(TestCase):
    def setUp(self):
        self.items = '1'

    def test_branch_import_create(self):
        self.assertEqual(self.items, '1')
