from django.db import models


class MemberSocialTagConfig(models.Model):
    member = models.OneToOneField('Member', null=True, blank=True, on_delete=models.CASCADE)
    pixel_id = models.CharField(max_length=64, null=True, blank=True)
    line_tag_id = models.CharField(max_length=64, null=True, blank=True)
    google_tag_id = models.CharField(max_length=64, null=True, blank=True)
    google_analytics_id = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.member.mcode)
