from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Passport(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True, related_name='passport')
    scan = models.FileField(upload_to='scan_files/', null=True, blank=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    document = models.FileField(upload_to='document_files/', null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    # Patronymic
    patronymic = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateTimeField(null=True, blank=True)
    personal_number = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(_("Gender"), choices=(
        ("Male", _("Male")),
        ("Female", _("Female"))
    ), default="Male", max_length=30)
    issue_date = models.DateTimeField(null=True, blank=True)
    expire_date = models.DateTimeField(null=True, blank=True)
    issuing_authority = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}'
