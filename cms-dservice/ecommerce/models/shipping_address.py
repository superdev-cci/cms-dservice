from django.db import models


class MemberShippingAddress(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE, null=True, blank=True)
    client_name = models.CharField(max_length=128, default=" ", blank=True, null=True)
    mobile = models.CharField(max_length=128, default=" ", blank=True, null=True)
    address = models.CharField(max_length=128, default=" ", blank=True, null=True)
    sub_district = models.CharField(max_length=64, default=" ", blank=True, null=True)
    district = models.CharField(max_length=64, default=" ", blank=True, null=True)
    province = models.CharField(max_length=64, default=" ", blank=True, null=True)
    post_code = models.IntegerField(null=True, blank=True)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.member)
