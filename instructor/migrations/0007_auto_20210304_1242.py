# Generated by Django 3.1.7 on 2021-03-04 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0006_auto_20210304_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='password',
        ),
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='instructor.instructoruser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='instructoruser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='instructoruser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='instructoruser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='instructoruser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
