from django.db import models
from django_mysql.models import ListCharField

class File(models.Model):
    # file = models.FileField(blank=False, null=False)
    content_id = models.CharField(max_length=100, null=False)
    content_type = models.CharField(max_length=200, null=True)
    content_name = models.CharField(max_length=200, null=True)
    # language = models.CharField(max_length=200, null=True)

    language = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
    )
    duration = models.CharField(max_length=100, null=True)
    partner = models.CharField(max_length=200, null=True)
    genre = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
    )
    actor = ListCharField(
        base_field=models.CharField(max_length=10),
        size=6,
        max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
    )
    parent_id = models.CharField(max_length=200, null=True)
    parent_name = models.CharField(max_length=200, null=True)