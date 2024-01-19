from django.db import models


class StructureSponsorIndex(models.Model):
    mcode_index = models.CharField(max_length=1000)
    mcode_ref = models.CharField(max_length=255)
    tot_pv = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_structure_sponsor'


class StructureBinaryIndex(models.Model):
    mcode_index = models.CharField(max_length=1000)
    mcode_ref = models.CharField(max_length=255)
    tot_pv = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ali_structure_binary'


class StructureBinaryRcodeIndex(models.Model):
    rcode = models.CharField(max_length=255)
    mcode_ref = models.CharField(max_length=255)
    mcode_index = models.CharField(max_length=5000)
    sp_code = models.CharField(max_length=255)
    status_terminate = models.IntegerField()
    pos_cur = models.CharField(max_length=255)
    pos_cur1 = models.CharField(max_length=255)
    pos_cur2 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ali_structure_binary_rcode'
