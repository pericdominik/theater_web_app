from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=50, default='Croatia')

    def __str__(self):
        return self.user.username
    

class Predstava(models.Model):
    title = models.CharField(max_length=120, unique=True)     
    description = models.TextField(null=True, blank=True)
    duration_minutes = models.PositiveSmallIntegerField(default=45)
    age_min = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='predstave', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title