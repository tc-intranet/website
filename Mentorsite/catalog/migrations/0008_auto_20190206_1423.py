# Generated by Django 2.0.10 on 2019-02-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20190206_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mentorgroup',
            options={'ordering': ['name_group', 'last_name']},
        ),
        migrations.AddField(
            model_name='mentorgroup',
            name='last_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
