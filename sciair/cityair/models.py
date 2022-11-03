from django.db import models
class City(models.Model):
    ip = models.SlugField(null=True)
    city = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField(null=True)

    def __str__(self):
        return self.ip