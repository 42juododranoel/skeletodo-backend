from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from skeletodo.models import BaseModel


class Task(BaseModel):
    """A user's todo item."""

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name=_('User'),
    )

    text = models.CharField(  # TextField doesn't give a fuck about max_length
        blank=False,  # Django suggests avoiding blank=True for CharField
        max_length=4096,
        verbose_name=_('Text'),
    )

    def save(self, *args, **kwargs):  # noqa: D102
        self.full_clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('tasks:detail', args=[self.id])
