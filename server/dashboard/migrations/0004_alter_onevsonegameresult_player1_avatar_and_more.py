# Generated by Django 5.0.4 on 2024-04-11 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_tournamentgameresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onevsonegameresult',
            name='player1_avatar',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='onevsonegameresult',
            name='player1_nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='onevsonegameresult',
            name='player2_avatar',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='onevsonegameresult',
            name='player2_nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='twovstwogameresult',
            name='team1_player1_avatar',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='twovstwogameresult',
            name='team1_player1_nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='twovstwogameresult',
            name='team1_player2_avatar',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='twovstwogameresult',
            name='team1_player2_nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='twovstwogameresult',
            name='team2_player1_avatar',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='twovstwogameresult',
            name='team2_player1_nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='twovstwogameresult',
            name='team2_player2_avatar',
            field=models.CharField(null=True),
        ),
        migrations.AlterField(
            model_name='twovstwogameresult',
            name='team2_player2_nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
