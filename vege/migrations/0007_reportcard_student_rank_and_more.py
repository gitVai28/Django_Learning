# Generated by Django 5.1.6 on 2025-02-28 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_reportcard'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportcard',
            name='student_rank',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_reportcard',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'date_of_reportcard')},
        ),
    ]
