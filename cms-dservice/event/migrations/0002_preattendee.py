# Generated by Django 2.1.3 on 2019-01-17 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20181225_1109'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreAttendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('members', models.ManyToManyField(related_name='event_pre_attendee', to='member.Member')),
            ],
        ),
    ]