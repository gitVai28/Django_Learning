# Generated by Django 5.1.6 on 2025-02-20 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_student_date_remove_student_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student',
        ),
        migrations.DeleteModel(
            name='teachers',
        ),
    ]
