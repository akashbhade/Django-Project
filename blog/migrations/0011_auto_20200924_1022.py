# Generated by Django 3.1.1 on 2020-09-24 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200924_0927'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='postslug',
        ),
    ]
