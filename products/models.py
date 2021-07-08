from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    author = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/products/')
    available = models.BooleanField(default=True)
    BOOK_TYPE = (
        ('Islamic History', 'Islamic History'),
        ('Islamic Cultural', 'Islamic Cultural'),
        ('Fiqh', 'Fiqh'),
        ('Tafseer', 'Tafseer'),
        ('A\'akida', 'A\'akida'),
        ('Hadith', 'Hadith'),
        ('Biography', 'Biography'),
        ('Familial', 'Familial'),
        ('Invasions', 'Invasions'),
        ('Politics', 'Politics'),
    )
    typ = models.CharField(max_length=200, choices=BOOK_TYPE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #     return reverse('product_details', args=(self.id,))

    def __str__(self):
        return self.title



