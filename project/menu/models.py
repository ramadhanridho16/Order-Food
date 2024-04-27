from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)    # iterable
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Promos(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)

class Medias(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    size = models.IntegerField()
    media = models.ImageField(upload_to='menus_image', blank=True, null=True)

class Home_banners(models.Model):
    name = models.CharField(max_length=255)
    media_id = models.ManyToManyField(Medias, related_name='banner')

class Couponts(models.Model):
    code = models

class Menus(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, related_name='menus', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(max_length=255)
    promo_price = models.PositiveIntegerField(max_length=255)
    promo = models.BooleanField(default=False)
    promo_id = models.ForeignKey(Promos, related_name='menus', on_delete=models.CASCADE)
    media_id = models.ManyToManyField(Medias, related_name='menus')
