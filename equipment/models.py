from django.db import models
from inventory.models import Inventory

# Create your models here.
class Model(models.Model):   
    id = models.AutoField(primary_key=True)
    description = models.CharField("Model description",max_length=100,null=False,unique=False,default='N/A')  
    category  = models.CharField("Mode category",max_length=20,null=False,unique=False,default='N/A')  # Modem, Switch, Modem Switch, Controller, SC-90 Upgrades
    band = models.CharField("Model band",max_length=29,null=False,unique=False,default='N/A')  # L-Band, Ku-Band, C-Band, Ka-Band
    vendor = models.CharField("Model vendor",max_length=50,null=True,unique=False)  
    model = models.CharField("Model",max_length=50,null=False,unique=True)  
    comments = models.CharField("comments",max_length=200,null=True,unique=False)  
    image_file = models.CharField("Image file",max_length=20,null=True,unique=False) 
    status = models.CharField("Model status",max_length=20,null=True,unique=False) 
    last_update = models.DateField()
    inventory_id = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True)
    
    def add_new(self, description, category,band, vendor, model, comments, image_file, status, last_update):
        self.description = description
        self.category = category
        self.band = band
        self.vendor = vendor
        self.model = model
        self.comments = comments
        self.image_file = image_file
        self.status = status
        self.last_update = last_update
        self.save()	
		
    def serialize(self):
        return {
            'id': self.id, 
            'description': self.description,
            'category': self.category,
            'band': self.band,
            'vendor': self.vendor,
            'model': self.model,
            'comments': self.comments,
            'image_file': self.image_file,
            'status': self.status,
            'last_update': self.last_update,
            'inventorys_id': self.inventory_id,
        }
 
 
 