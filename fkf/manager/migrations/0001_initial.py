# Generated by Django 4.2.6 on 2023-10-17 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('admin_name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
                ('admin_name', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('academy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.academy')),
            ],
        ),
        migrations.AddField(
            model_name='academy',
            name='county',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.county'),
        ),
    ]
