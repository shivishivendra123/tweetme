# Generated by Django 2.0.4 on 2018-06-11 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20180608_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=140)),
                ('Content', models.CharField(max_length=140)),
            ],
        ),
        migrations.AlterField(
            model_name='test',
            name='email',
            field=models.EmailField(max_length=60),
        ),
    ]