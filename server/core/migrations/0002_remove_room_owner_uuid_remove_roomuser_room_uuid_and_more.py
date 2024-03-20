# Generated by Django 5.0.3 on 2024-03-19 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='owner_uuid',
        ),
        migrations.RemoveField(
            model_name='roomuser',
            name='room_uuid',
        ),
        migrations.RemoveField(
            model_name='roomuser',
            name='user_uuid',
        ),
        migrations.RemoveField(
            model_name='tournamenthistory',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='tournamenthistory',
            name='user2',
        ),
        migrations.RemoveField(
            model_name='tournamenthistory',
            name='user3',
        ),
        migrations.RemoveField(
            model_name='tournamenthistory',
            name='user4',
        ),
        migrations.RemoveField(
            model_name='winlosehistory',
            name='user_uuid',
        ),
        migrations.DeleteModel(
            name='OneVsOneHistory',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='RoomUser',
        ),
        migrations.DeleteModel(
            name='TournamentHistory',
        ),
        migrations.DeleteModel(
            name='WinLoseHistory',
        ),
    ]