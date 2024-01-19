# Generated by Django 2.1.3 on 2019-01-17 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0008_auto_20181225_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=64)),
                ('description', models.CharField(default='', max_length=128)),
                ('date', models.DateField()),
                ('location', models.CharField(default=' ', max_length=64)),
                ('mentor', models.CharField(default=' ', max_length=64)),
                ('tag', models.CharField(default=' ', max_length=8)),
                ('event_tag', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='attendee',
            name='event',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event'),
        ),
        migrations.AddField(
            model_name='attendee',
            name='members',
            field=models.ManyToManyField(related_name='event_attendee', to='member.Member'),
        ),
    ]