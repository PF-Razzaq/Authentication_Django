# Generated by Django 5.0.4 on 2024-04-24 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_name_user_username_alter_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
    ]