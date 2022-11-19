from django.db import models

# Create your models here.

class Constraction(models.Model):
    title = models.CharField(max_length=50)
    detay = models.TextField(("proje detayları"),null=True,blank=True)
    projeuser = models.CharField(("proje sorumlusu"), max_length=50,null=True,blank=True)
    maliyet = models.IntegerField(("maliyet"),null=True,blank=True)
    image = models.FileField(("proje resmi"), upload_to='', max_length=100,null=True,blank=True) 
    def __str__(self) -> str:
        return self.title