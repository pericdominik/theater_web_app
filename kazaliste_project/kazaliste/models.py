from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    

class Calendar(models.Model):
    predstava = models.ForeignKey('Predstava', on_delete=models.CASCADE, related_name='raspored')
    date = models.DateField()
    time = models.TimeField()
    dvorana = models.CharField(max_length=50)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date', 'time', 'predstava__title']

    def __str__(self):
        return f"{self.predstava.title} - {self.date} {self.time}"    


class Comment(models.Model):
    predstava = models.ForeignKey('Predstava', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Komentar od {self.user.username} - {self.predstava.title}"
    

class Like(models.Model):
    predstava = models.ForeignKey('Predstava', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('predstava', 'user') 

    def __str__(self):
        return f"Like od {self.user.username} - {self.predstava.title}"



class PriceItem(models.Model):
    name = models.CharField(max_length=80)                  
    price = models.DecimalField(max_digits=4, decimal_places=2)  
    description = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} ({self.price} €)"
    
class Reservation(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nova rezervacija'),
        ('contacted', 'Kontaktirana osoba'),
        ('closed', 'Zatvorena rezervacija'),
    ]

    predstava = models.ForeignKey('Predstava', on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=120)
    email = models.EmailField()
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.predstava.title} - {self.quantity}"        
