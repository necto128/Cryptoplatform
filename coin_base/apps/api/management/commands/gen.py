from django.core.management.base import BaseCommand

from src.generators.crypto_directive import create_record


class Command(BaseCommand):
    """Create a command class to generate initial data."""

    help = 'Generate initial data for the application'

    def handle(self, *args, **kwargs):
        """Execute the command to generate initial data."""
        self.stdout.write(self.style.NOTICE('Generating initial data...'))

        try:
            create_record()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error generating initial data: {e}'))
