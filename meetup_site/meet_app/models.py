from django.db import models
from django.utils.text import slugify

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=100)
    suburb = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country =  models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.city})'
    


class Attendee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    date = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    attendees = models.ManyToManyField(Attendee, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

