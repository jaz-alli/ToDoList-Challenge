# Generated by Django 2.2.6 on 2019-10-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('On Time', 'on_time'), ('Complete', 'complete'), ('Expected Late', 'expected_late'), ('Overdue', 'overdue')], max_length=20)),
                ('due_date', models.DateField()),
            ],
        ),
    ]
