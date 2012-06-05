from django.db import models
from djolio.portfolio.models import Project

class Files(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    files = models.FileField(upload_to='files')

    class Meta:
        db_table = "files"
	verbose_name_plural = "files"
        ordering = ['name']

    def __unicode__(self):
        return self.name
