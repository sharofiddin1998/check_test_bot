# Generated by Django 4.1.5 on 2023-02-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_bot', '0019_remove_testresponse_name_testresponse_answer_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresponse',
            name='answer_message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
