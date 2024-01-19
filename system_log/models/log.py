from django.db import models


class Log(models.Model):
    sys_id = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    detail = models.TextField()
    chk_mobile = models.IntegerField()
    chk_id_card = models.IntegerField()
    chk_sp_code = models.IntegerField()
    chk_upa_code = models.IntegerField()
    chk_acc_no = models.IntegerField()
    ip = models.CharField(max_length=20, blank=True, null=True)
    logdate = models.DateField(blank=True, null=True)
    logtime = models.TimeField(blank=True, null=True)

    class Meta:
        db_table = 'ali_log'
        verbose_name_plural = 'System log'
