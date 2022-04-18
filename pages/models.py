from django.db import models

# Create your models here.
class Page(models.Model):
    title =  models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)

    # We have to tell django to call our objects by their title, 
    # instead of calling them "Pages objects" by default
    def __str__(self):
        return self.title



    




