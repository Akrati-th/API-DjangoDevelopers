from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    linkedin_url = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
