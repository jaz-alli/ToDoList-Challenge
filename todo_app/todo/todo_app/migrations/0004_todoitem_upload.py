# Generated by Django 2.2.6 on 2019-10-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20191018_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='upload',
            field=models.FileField(default='default', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
