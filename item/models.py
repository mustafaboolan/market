from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        # this use to order databse by name 
        ordering = ('name',)
        # change name of table in database
        verbose_name_plural = 'Categories'



    # this use to show name of item  in data base not show object string  
          
    def __str__(self):
        return self.name



class Item(models.Model):
    category =  models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add =True)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name