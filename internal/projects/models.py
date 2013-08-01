from django.db import models
from profiles.models import TeamMember
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey('Project', related_name='tasks')

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(TeamMember, related_name="projects_owned")
    collaborators = models.ManyToManyField(TeamMember, related_name="projects", through='Role')
    start_date = models.DateField(max_length=10)
    deadline = models.DateField(max_length=10)
    website = models.URLField()

class Role(models.Model):
    profile = models.ForeignKey(TeamMember)
    project = models.ForeignKey(Project)
    role_name = models.CharField(max_length=100)
