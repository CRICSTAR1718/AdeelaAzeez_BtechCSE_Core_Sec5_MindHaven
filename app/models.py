from django.db import models

# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "tblevents"

class JournalEntry(models.Model):
    content = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return f"Entry on {self.date}"
    
    class Meta:
        ordering = ['-date']