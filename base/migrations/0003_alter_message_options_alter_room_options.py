# Generated by Django 5.0.6 on 2024-05-14 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_created_at_room_host_room_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated_at', '-created_at']},
        ),
    ]
