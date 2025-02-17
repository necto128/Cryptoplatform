from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    """Create a command class."""

    help = 'Run makemigrations and migrate'

    def handle(self, *args, **kwargs):
        """Execute the command."""
        self.stdout.write(self.style.NOTICE('Running makemigrations...'))
        call_command('makemigrations')

        self.stdout.write(self.style.NOTICE('Running migrate...'))
        call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Migrations completed successfully!'))
