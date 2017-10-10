from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=60)
    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name
