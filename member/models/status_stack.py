from django.db import models


class MemberStatusStack(models.Model):
    """
    a class represent a history of member's status
    """
    STACK_CHOICE = (
        ('S', 'SUSPEND'),
        ('T', 'Terminate'),
    )
    member = models.ForeignKey('Member', null=True, blank=True, on_delete=models.CASCADE)
    issue_date = models.DateField(null=True, blank=True, auto_now=True)
    stack_type = models.CharField(max_length=1, choices=STACK_CHOICE, blank=True, null=True)

    class Meta:
        ordering = ['-issue_date']

    def __str__(self):
        return '{} : {}'.format(self.member.mcode, self.issue_date.strftime('%Y-%m-%d'))
