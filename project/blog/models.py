from django.db import models


class Blog(models.Model):
    LANGUAGE_CHOICES = [
        ('Azerbaijan', 'Azerbaijan'),
        ('English', 'English'),
    ]
    slug = models.SlugField(max_length=255, unique=True,verbose_name='Slug')
    title = models.CharField(max_length=255,verbose_name='Title')
    image = models.ImageField(upload_to='blogs/%Y/%m/%d/',verbose_name='Image',null=True)
    content = models.TextField(verbose_name='Content')
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='Azerbaijan',verbose_name='Language')
    created_at = models.DateTimeField(auto_now_add=True, null=True,verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, null=True,verbose_name="Updated Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active?")
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"