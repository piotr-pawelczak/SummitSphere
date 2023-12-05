from django.db import models
from django.utils.translation import gettext_lazy as _

from summit_sphere.peaks.models import Peak
from summit_sphere.users.models import User


class Badge(models.Model):
    class Source(models.IntegerChoices):
        SYSTEM = 0, _("System")
        USER = 1, _("User")

    name = models.CharField(max_length=200)
    peaks = models.ManyToManyField(Peak, related_name="badges")
    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE, related_name="badges"
    )
    source = models.IntegerField(choices=Source.choices)

    def __str__(self):
        """Return string representation of the Badge."""
        return self.name
