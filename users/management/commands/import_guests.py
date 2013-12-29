import csv

from django.core.management.base import BaseCommand

from ... import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        filename = args[0]
        file = open(filename)
        rows = csv.reader(file)
        for row in rows:
            if row[0]:
                u = models.WeddingUser(
                    short_name=row[0],
                    long_name=row[1],
                    username=row[2],
                    number=row[4],
                )
                u.set_password(row[3])
                u.save()
                self.stdout.write("Created '{}'".format(u.short_name))
