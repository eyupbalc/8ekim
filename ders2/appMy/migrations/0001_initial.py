# Generated by Django 4.1.3 on 2022-11-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('detay', models.TextField(blank=True, null=True, verbose_name='proje detayları')),
                ('projeuser', models.CharField(blank=True, max_length=50, null=True, verbose_name='proje sorumlusu')),
                ('maliyet', models.IntegerField(blank=True, null=True, verbose_name='maliyet')),
            ],
        ),
    ]