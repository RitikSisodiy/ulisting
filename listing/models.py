from django.db import models

# Create your models here.
from home.models import unique_slug_generator


class listingCat(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True,blank=True)
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(listingCat,self.name)
        super(listingCat, self).save(*args, **kwargs)