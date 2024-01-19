from django.db import models


class AliUser(models.Model):
    uid = models.AutoField(primary_key=True)
    usercode = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    usertype = models.IntegerField(blank=True, null=True)
    object1 = models.IntegerField(blank=True, null=True)
    object2 = models.IntegerField(blank=True, null=True)
    object3 = models.IntegerField(blank=True, null=True)
    object4 = models.IntegerField(blank=True, null=True)
    object5 = models.IntegerField(blank=True, null=True)
    object6 = models.IntegerField()
    object7 = models.IntegerField()
    object8 = models.IntegerField()
    object9 = models.IntegerField()
    object10 = models.IntegerField()
    inv_ref = models.CharField(max_length=20, blank=True, null=True)
    accessright = models.TextField(blank=True, null=True)
    code_ref = models.CharField(max_length=255)
    checkbackdate = models.IntegerField()
    limitcredit = models.IntegerField()
    mtype = models.IntegerField()

    class Meta:
        db_table = 'ali_user'
        verbose_name_plural = 'StaffUser'
