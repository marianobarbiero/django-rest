from __future__ import unicode_literals
from django.utils.translation import ugettext as _

from django.db import models

class Common(models.Model):
    class Meta:
        abstract = True

class PersonalData(Common):
    GENDERS = [ ('M', _("Male")),
                ('F', _("Female")),
                ('O', _("Other"))]
    
    id_doc_number   = models.CharField(max_length=32, verbose_name=_("person doc"))
    first_name      = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("person first name"))
    last_name       = models.CharField(max_length=50, null=True, blank=True, verbose_name=_("person last name"))
    gender          = models.CharField(max_length=1, choices=GENDERS, null=True, blank=True, verbose_name=_("person gender"))
    birthdate       = models.DateField(null=True, blank=True, verbose_name=_("person birthdate"))
    nickname        = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("person nickname"))
    address_line_1  = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("person address1"))
    address_line_2  = models.CharField(max_length=80, null=True, blank=True, verbose_name=_("person address2"))
    postcode        = models.CharField(max_length=16, null=True, blank=True, verbose_name=_("person postcode"))

    email           = models.EmailField()
    image_url       = models.URLField(null=True, blank=True)
    
    def __unicode__(self):
        return self.last_name + ', ' + self.first_name
    
    class Meta:
        verbose_name = _("Personal Data")
        verbose_name_plural = _("Personal Data")

