# Generated by Django 4.1.5 on 2023-02-08 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu_bot', '0014_remove_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='edu_bot.teacher'),
            preserve_default=False,
        ),
    ]