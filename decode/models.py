from django.db import models
import time
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Decode(models.Model):
 barcode =  models.CharField(blank=False, max_length=255,default='',editable=True)
 ref_no =  models.CharField(blank=False, max_length=255,default='',editable=True)
 vendor_id =  models.CharField(blank=False, max_length=255,default='',editable=False)
 price =  models.CharField(blank=False, max_length=255,default='',editable=False)
    
