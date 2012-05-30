from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(blank=True)
    
    class Meta:
        db_table = "clients"
        ordering = ['name']

    def __repr__(self):
        return self.name
    
class Medium(models.Model):
    name = models.CharField(max_length=250)
    
    class Meta:
        db_table = "media"
        verbose_name_plural = "media"
        ordering = ['name']

    def __repr__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    project_url = models.URLField('Project URL')
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client)
    media = models.ManyToManyField(Medium)
    disciplines = models.CharField(max_length=200)
    completion_date = models.DateField()
    in_development = models.BooleanField()
    is_public = models.BooleanField(default=True)
    overview_image = models.URLField()
    detail_image = models.URLField()
    
    class Meta:
        db_table = "projects"
        ordering = ['-completion_date']
     
    def __repr__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/work/%s/" % self.slug
