from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=60)
    following = models.ManyToManyField('self', blank=True, symmetrical=False)

    def __str__(self):
        return self.name
