# Generated by Django 2.0.4 on 2018-06-12 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20180611_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
