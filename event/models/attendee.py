from django.db import models


class Attendee(models.Model):
    event = models.OneToOneField('Event', on_delete=models.CASCADE, null=True, blank=True)
    members = models.ManyToManyField('member.Member', related_name='event_attendee')

    def __str__(self):
        if self.event is not None:
            str = "{} {}".format(self.event.date, self.event.name)
        else:
            str = "{}".format(self.pk)
        return str


class PreAttendee(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, null=True, blank=True)
    members = models.ManyToManyField('member.Member', related_name='event_pre_attendee')
    group = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        if self.event is not None:
            str = "{} {}".format(self.event.date, self.event.name)
        else:
            str = "{}".format(self.pk)
        return str