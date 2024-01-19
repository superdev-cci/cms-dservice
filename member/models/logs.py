from django.db import models


class MemberLogs(models.Model):
    """
    a class model represent a member's log event
    (ex. member have been terminate, suspend, change information profile)
    """
    TOPIC_CHOICE = (
        ('S', 'SUSPEND'),
        ('T', 'Terminate'),
        ('C', 'Change'),
    )
    member = models.ForeignKey('Member', null=True, blank=True, on_delete=models.CASCADE)
    topic = models.CharField(max_length=1, choices=TOPIC_CHOICE, blank=True, null=True)
    change = models.TextField(null=True, blank=True)
