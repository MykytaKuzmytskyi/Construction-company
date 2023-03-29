from django.contrib.auth.admin import User
from django.conf import settings
from django.core.management import call_command
from django.db import migrations

import task_manager


def create_position(apps, schema_editor):
    Position = apps.get_model("task_manager", "Position")
    db_alias = schema_editor.connection.alias
    Position.objects.using(db_alias).bulk_create([
        Position(name="admin"),
    ])


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'fixture_data.json', app_label='task_manager')


def reverse_func(apps, schema_editor):
    print('reverse')


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_position, reverse_func),
        migrations.RunPython(load_fixture, reverse_func),
    ]
