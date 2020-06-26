from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField( max_length= 20)
    url   = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField( default=1)
    image = models.ImageField( upload_to= "image/")
    icon = models.ImageField( upload_to= "image/")
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

