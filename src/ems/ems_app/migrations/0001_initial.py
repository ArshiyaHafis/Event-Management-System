# Generated by Django 4.2.2 on 2023-06-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_link', models.URLField()),
                ('event_time', models.DateTimeField(null=True)),
                ('event_image', models.ImageField(upload_to='images/')),
                ('event_descp', models.TextField()),
                ('event_location', models.TextField()),
            ],
        ),
    ]
