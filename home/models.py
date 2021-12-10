from django.db import models
import random,string
from django.utils.text import slugify
# Create your models here.
def get_random_string(size):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    slug=slugify(new_slug)
    Klass = instance
    qs_exists = Klass.objects.filter(slug=slug).exists()
    print(qs_exists)
    if qs_exists :
        new_slug = slugify(str(slug)+get_random_string(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
