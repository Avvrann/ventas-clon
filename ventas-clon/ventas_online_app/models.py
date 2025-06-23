from django.db import models 

class Products(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    
    
    def __str__(self):
        return self.name
    
    
