# Generated by Django 2.1 on 2018-08-30 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180824_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='color',
        ),
        migrations.AddField(
            model_name='classinfo',
            name='color',
            field=models.CharField(default='#000000', help_text='#을 포함한 색상 코드. 예) 빨간색 => #ff0000', max_length=9, verbose_name='컬러코드'),
            preserve_default=False,
        ),
    ]
