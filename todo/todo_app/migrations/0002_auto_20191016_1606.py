# Generated by Django 2.2.6 on 2019-10-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='status',
            field=models.CharField(choices=[('on_time', 'On Time'), ('complete', 'Complete'), ('expected_late', 'Expected Late'), ('overdue', 'Overdue')], max_length=20),
        ),
    ]
