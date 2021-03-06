# Generated by Django 4.0.4 on 2022-04-21 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Arduino UNO', 'Arduino UNO'), ('Raspberry', 'Raspberry'), ('ESP8266', 'ESP8266'), ('ESP32', 'ESP32')], max_length=20)),
                ('device_id', models.CharField(blank=True, max_length=255)),
                ('placed', models.CharField(choices=[('Colombia', 'Colombia'), ('Argentina', 'Argentina'), ('Brasil', 'Brasil'), ('Chile', 'Chile')], max_length=20)),
                ('details', models.CharField(blank=True, max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_item', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
