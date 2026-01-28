from django.template.defaultfilters import default
from secrets import choice
from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')
    


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="-")
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField(Promotion, related_name='products')



class Customer(models.Model):     

    class Membership(models.TextChoices):
        BRONZE = 'B', 'Bronze'
        SILVER = 'S', 'Silver'
        GOLD = 'G', 'Gold'

    given_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices = Membership.choices, default = Membership.BRONZE)


    class Meta:
        db_table = "store_customers"
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]


class Order(models.Model):
    
    class PaymentStatus(models.TextChoices):
        PENDING = 'P', 'Pending'
        COMPLETED = 'C', 'Completed'
        FAILED = 'F', 'Failed'
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PaymentStatus.choices, default=PaymentStatus.PENDING)

class Cart(models.Model):
    pass


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Adress(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True) #one to one
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #one to many
