from django.db import models

# Create your models here.
class Hello(models.Model):
    """docstring for Hello."""
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50,blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True,null = True)
    def __unicode__(self):
        return self.title
    class Meta:
        """docstring for Meta."""
        ordering = ['-date_time']
