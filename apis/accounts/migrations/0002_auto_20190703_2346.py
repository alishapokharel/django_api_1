# Generated by Django 2.2.3 on 2019-07-04 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SA', 'Superadmin'), ('NA', 'Normaladmin'), ('JA', 'Journalist'), ('GU', 'Guestuser')], default='GU', max_length=2),
        ),
    ]
