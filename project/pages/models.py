from django.db import models



class Contact(models.Model):
    full_name = models.CharField(max_length=255,verbose_name="First and Last Name")
    phone = models.CharField(max_length=50,verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Created Date")

    def __str__(self):
        return self.phone
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        