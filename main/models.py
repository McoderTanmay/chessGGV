from django.db import models

POSITION_TYPE=(
    ('Presedent', 'Presedent'),
    ('Vice Presedent', 'Vice Presedent')
)

class Member(models.Model):
    member_name = models.CharField(max_length=50)
    member_position = models.CharField(max_length = 50)
    member_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.member_name
    
class Presedent(models.Model):
    pres_name = models.CharField(max_length=50)
    pres_position = models.CharField(max_length=50, choices=POSITION_TYPE, default = 'Presedent')
    pres_image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.pres_name
    
class Images(models.Model):
    image = models.ImageField(upload_to="gallery/")

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField()
    event_description = models.TextField()
    event_image = models.ImageField(upload_to="events/")

    def __str__(self):
        return self.event_name
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=5000)
    date = models.DateField()

    def __str__(self):
        return self.email

class Resources(models.Model):
    s_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    date = models.DateField()
    doc = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title