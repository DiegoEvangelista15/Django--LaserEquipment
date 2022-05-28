from django.db import models
from stdimage.models import StdImageField
import uuid


# Image protection

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename  

# Create your models here.


class Base(models.Model):
    created = models.DateField(
        'Created', auto_now_add=True)  # so eh colocado na add
    # sempre que modifica, ele muda
    modify = models.DateField('Update', auto_now=True)

    class Meta:
        abstract = True


class Manual(Base):
    TYPE_CHOICE = (
        ('Mark', 'Mark'),
        ('Cut', 'Cut'),
        ('Clean', 'Clean'),
        ('Weld', 'Weld')
    )
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', max_length=255, null=True, blank=True)
    type = models.CharField('Type', max_length=20, choices=TYPE_CHOICE)
    file_upload = models.FileField('File', upload_to=get_file_path)

    def __str__(self) -> str:
        return self.name


class Software(Base):
    TYPE_CHOICE = (
        ('Mark', 'Mark'),
        ('Cut', 'Cut'),
        ('Clean', 'Clean'),
        ('Weld', 'Weld')
    )

    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', max_length=255,null=True, blank=True)
    type = models.CharField('Type', max_length=20, choices=TYPE_CHOICE)
    file_upload = models.FileField('File', upload_to=get_file_path)

    def __str__(self) -> str:
        return self.name


class SparePart(Base):
    TYPE_CHOICE = (
        ('Mark', 'Mark'),
        ('Cut', 'Cut'),
        ('Clean', 'Clean'),
        ('Weld', 'Weld')
    )
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', max_length=255)
    type = models.CharField('Type', max_length=20, choices=TYPE_CHOICE)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    image = StdImageField('Image', upload_to=get_file_path, variations={
                          'thumb': {'width': 286, 'height': 180, 'crop': True}})


class Equipment(Base):
    TYPE_CHOICE = (
        ('Mark', 'Mark'),
        ('Cut', 'Cut'),
        ('Clean', 'Clean'),
        ('Weld', 'Weld')
    )
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description', max_length=255)
    type = models.CharField('Type', max_length=20, choices=TYPE_CHOICE)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    image = StdImageField('Image', upload_to=get_file_path, variations={
                          'thumb': {'width': 286, 'height': 180, 'crop': True}})
