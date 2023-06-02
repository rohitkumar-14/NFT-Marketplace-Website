from django.db import models

# Create your models here.
class Add(models.Model):
    nft_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, default="")
    phone = models.CharField(max_length=111, default="")
    nft_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300, default="")
    image = models.ImageField(upload_to="upload/images")

    def __str__(self):
        return self.nft_name
    
class Contact(models.Model):
    name = models.CharField(max_length=300, default="")
    email = models.EmailField()
    subject = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.email