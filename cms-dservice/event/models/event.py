from django.db import models


class Event(models.Model):
    TYPE_CHOICE = (
        ('OPP', 'OPP'),
        ('BSS', 'BSS'),
        ('CAMP', 'CAMP'),
        ('OTHER', 'OTHER'),
    )
    name = models.CharField(max_length=64, default=" ")
    description = models.CharField(max_length=128, default="")
    date = models.DateField()
    location = models.CharField(max_length=64, default=" ")
    mentor = models.CharField(max_length=64, default=" ")
    tag = models.CharField(max_length=8, default=" ")
    event_tag = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.date, self.location)

    # def attendee_report(self):
        # member = self.attendee.members.count()
        # person = self.attendee.person_set.count()
        # members = self.attendee.member_set.count()
        # print(members, members, person)