from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    add = models.CharField(max_length=50, blank=True, null=True)
    pic_profile = models.ImageField(upload_to='accounts_images/', null=True)
    # height_field=None, width_field=None, max_length=100, **options

    def __str__(self):
        return str(self.user)


# signal , kwargs -> sender
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Friend(models.Model):
    friend = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Friends'
