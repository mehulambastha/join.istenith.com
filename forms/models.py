from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class WhitelistEmailValidator(EmailValidator):
    def validate_domain_part(self, domain_part):
        raise ValidationError("Kindly submit form with your college email only.")

    def __eq__(self, other):
        return isinstance(other, WhitelistEmailValidator) and super().__eq__(other)


def file_size(value):  # add this to some file where you can import it from
    limit = 3 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 3 MiB.')


class Registeration(models.Model):
    BRANCH = (
        ('', 'Choose Your Branch'),
        ("Civil Engineering", 'Civil Engineering'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Electrical Engineering', 'Electrical Engineering'),
        ('Electronics And Communication Engineering', 'Electronics And Communication Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Computer Science Engineering', 'Computer Science Engineering'),
        ('Material Science', 'Material Science'),
        ('Engineering Physics', 'Engineering Physics'),
        ('Mathematics And Computing', 'Mathematics And Computing'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, validators=[WhitelistEmailValidator(whitelist=['nith.ac.in'])])
    phone_number = models.CharField(max_length=11, unique=True)
    branch = models.CharField(choices=BRANCH, max_length=100, default='')
    resume = models.FileField(upload_to='resumes/', validators=[file_size, FileExtensionValidator(allowed_extensions=["pdf"])], blank=False, null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.email, self.phone_number)
