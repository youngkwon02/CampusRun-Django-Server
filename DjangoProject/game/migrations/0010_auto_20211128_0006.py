# Generated by Django 3.2.7 on 2021-11-27 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_univ_domain'),
        ('game', '0009_alter_record_rank'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrance',
            new_name='GameEntrance',
        ),
        migrations.AddField(
            model_name='room',
            name='is_full',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='waiting_url',
            field=models.TextField(default='_'),
        ),
        migrations.CreateModel(
            name='WaitEntrance',
            fields=[
                ('ent_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_out', models.BooleanField(default=False)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wait_room', to='game.room')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wait_user', to='account.user')),
            ],
        ),
    ]
