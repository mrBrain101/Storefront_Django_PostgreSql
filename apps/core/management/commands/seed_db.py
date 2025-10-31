from django.core.management.base import BaseCommand
from django.db import connection
from pathlib import Path
import os
import logging


logger = logging.getLogger(__name__)
class Command(BaseCommand):
    help = 'Populates the database with collections and products'

    def handle(self, *args, **options):
        logger.info('Checking if population is enabled...')
        populate_db = os.getenv('POPULATE_DB', 'false').lower()

        if not populate_db == 'true':
            self.stdout.write(self.style.WARNING(
                f'Database seeding skipped (POPULATE_DB={populate_db})'
                ))
            return
        
        self.stdout.write(self.style.SUCCESS(
            'Starting database population...'
            ))

        current_dir = Path(__file__).resolve().parent.parent
        file_path = os.path.join(current_dir, 'seed_db.sql')
        sql = Path(file_path).read_text()

        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
            self.stdout.write(
                self.style.SUCCESS('Database populated successfully!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error populating database: {str(e)}')
            )
            raise