from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=254)
    image = models.ImageField(default='images/pp/profile-p.png', upload_to='images/pp', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        index_together = (('id', 'name'),)
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

#
# @receiver(post_save, sender=User)
# def create_user_as_customer(sender, instance, created, **kwargs):
#     if created:
#         Customer.objects.create(user=instance)
