# Generated by Django 3.0.3 on 2020-02-09 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todoitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=4096, verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
