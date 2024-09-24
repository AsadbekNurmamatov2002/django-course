from django.db import models

# Create your models here.


class AccesRequared(models.TextChoices):
    ANYONE = 'any', 'Anyone'
    EMAIL_REQUIRED = 'email_required', "Email Required"
    
class PublishStatus(models.TextChoices):
    PUBLISHED = 'PUBLISHED', 'Published'
    DRAF = 'Draft', "Draft"

class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    # image =
    # access =
    access = models.CharField(max_length=15, choices=AccesRequared.choices, default=AccesRequared.ANYONE)
    status = models.CharField(max_length=10, choices=PublishStatus.choices, default=PublishStatus.DRAF)
    
    