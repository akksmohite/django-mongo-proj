from __future__ import unicode_literals
from django.db import migrations


def create_initial_actors(apps, schema_editor):
    Actor = apps.get_model('actor', 'Actor')

    Actor(name='Salama Hayek', description='Salama Hayek', film="Desparado").save()
    Actor(name='Al Pacino', description='Al Pacino', film="The Godfather").save()
    Actor(name='Robert De Niro', description='Robert De Niro', film="Raging Bull").save()
    Actor(name='Jack Nicholson', description='Jack Nicholson', film="Chinatown").save()
    Actor(name='Clint Eastwood', description='Clint Eastwood', film="A fistful of dollars").save()
    Actor(name='Nicolas Cage', description='Nicolas Cage', film="Adaptation").save()
    Actor(name='John Travolta', description='John Travolta', film="Grease").save()
    Actor(name='Martin Lawrence', description='Martin Lawrence', film="Bad Boys").save()


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_actors),
    ]	