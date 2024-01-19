# Generated by Django 2.1.3 on 2021-02-19 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0018_member_tc_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberSocialTagConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pixel_id', models.CharField(blank=True, max_length=64, null=True)),
                ('line_tag_id', models.CharField(blank=True, max_length=64, null=True)),
                ('google_tag_id', models.CharField(blank=True, max_length=64, null=True)),
                ('google_analytics_id', models.CharField(blank=True, max_length=64, null=True)),
                ('member', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member')),
            ],
        ),
    ]
