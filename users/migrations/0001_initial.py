# Generated by Django 5.1 on 2024-08-26 06:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('nickname', models.CharField(blank=True, max_length=40, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('followers', models.ManyToManyField(related_name='following', through='users.Follow', to='users.profile')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='follow',
            name='followed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_set', to='users.profile'),
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_set', to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'followed')},
        ),
    ]
