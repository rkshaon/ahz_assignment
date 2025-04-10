from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=100,
        blank=True,
        null=True
    )
    date_of_birth = models.DateField(
        _('Birth Date'),
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(
        _('Added Date Time'),
        auto_now_add=True
    )
    updated_date_time = models.DateTimeField(
        _('Updated Date Time'),
        auto_now=True
    )

    def __str__(self):
        return self.name if self.name else "Unknown Author"
