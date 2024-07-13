from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255,unique=True)
    email = models.CharField(max_length=255,default='')
    phone = models.CharField(max_length=11,unique=True)
    address = models.CharField(max_length=10000,default='')
    zipcode = models.CharField(max_length=10000,default='')
    is_vip=models.BooleanField(default=False)
    def __str__(self):
        return self.username

class HeaderImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)

    def __str__(self):
        return self.title
  

class Color(models.Model):
    name = models.CharField(max_length=255)
    rgb = models.CharField(max_length=7) 

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=255)
    shoulder_width = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    chest_width = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    top_length = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    bottom_length = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    waist_width = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    shoews_width = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    shoews_length = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    category = models.ManyToManyField(Category)
    payment_link = models.URLField(max_length=200, null=True, blank=True) 


    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Image for {self.product.title}"
    

    
    
class OrderStatus(models.Model):
    code = models.CharField(max_length=100, unique=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.code
    


class LaundryService(models.Model):
    name = models.CharField(max_length=255)
    cost = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='laundry_images/', null=True, blank=True)

    def __str__(self):
        return self.name    
    

