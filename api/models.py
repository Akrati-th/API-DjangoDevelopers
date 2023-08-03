from django.db import models

SKILL_CHOICES = [("Python", "Python"), ("Java", "Java"), ("Django", "Django"), ("HTML", "HTML"), ("CSS", "CSS"),
                 ("JavaScript", "JavaScript"), ("Flask", "Flask"), ("Android Development", "Android Development"),
                 ("Kotlin", "Kotlin"), ("React.js", "React.js"), ("Node.js", "Node.js"), ("Angular", "Angular")]


class DeveloperType(models.Model):
    type_name = models.CharField(max_length=150)
    developer_skill = models.CharField(choices=SKILL_CHOICES, max_lenght=20)

    def __str__(self):
        return self.name


class Developer(models.Model):
    developer_name = models.CharField(max_length=250)
    bio = models.TextField(blank=True, null=True)
    current_location = models.CharField(max_length=500, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    developer_type = models.ForeignKey(DeveloperType, on_delete=models.CASCADE)
    linkedin_url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id', 'name']
