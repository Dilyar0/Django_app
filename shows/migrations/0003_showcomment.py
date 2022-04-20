# Generated by Django 4.0.4 on 2022-04-20 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_tvshow_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('shows', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows_comment', to='shows.tvshow')),
            ],
        ),
    ]
