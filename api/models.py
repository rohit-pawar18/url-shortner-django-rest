from django.db import models
from django.conf import settings

from random import choice

from string import ascii_letters, digits

from django.core.cache import cache
# Create your models here.

class Shortener(models.Model):
    '''
    Creates a short url based on the long one
    
   

    long_url -> The original link

    short_url ->  shortened link https://domain/(short_url)
    ''' 

    long_url = models.URLField()

    short_url = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return f"{self.short_url}"

    
    def save(self, *args, **kwargs):

        # If the short url wasn't specified
        if not self.short_url:
            # We pass the model instance that is being saved
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)



# Try to get the value from the settings module
SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAIABLE_CHARS = ascii_letters + digits


def create_random_code(chars=AVAIABLE_CHARS):
    """
    Creates a random string with the predetermined size
    """
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )

def create_shortened_url(short_url):
    random_code = create_random_code()
    # Gets the model class
    if Shortener.objects.filter(short_url=random_code).exists() or cache.get(short_url):
        # Run the function again
        return create_shortened_url(short_url)

    return random_code
