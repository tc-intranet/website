# Generated by Django 2.0.10 on 2019-02-06 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20190206_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentorgroup',
            name='mentor_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Mentor'),
        ),
    ]
