from django.db import models
from django.utils.translation import ugettext_lazy as _

from skeletodo.models import BaseModel


class Todoitem(BaseModel):
    """A user's todo item."""

    text = models.CharField(  # TextField doesn't give a fuck about max_length
        blank=False,  # Django suggests avoiding blank=True for CharField
        verbose_name=_('Text'),
        max_length=4096,
    )

    def save(self, *args, **kwargs):  # noqa: D102
        self.full_clean()
        super().save(*args, **kwargs)
