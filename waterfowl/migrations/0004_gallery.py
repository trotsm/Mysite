# Generated by Django 2.1.3 on 2018-12-18 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waterfowl', '0003_articles_audio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_detail', models.ImageField(upload_to='gallery')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='waterfowl.Articles')),
            ],
        ),
    ]
