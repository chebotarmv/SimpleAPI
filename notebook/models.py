from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format:\
                                  '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return '%s %s' % (self.first_name, self.second_name)
