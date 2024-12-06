from django.db import models

class Models(models.Model):
    model_name = models.CharField(max_length=75,verbose_name="modelning oti")
    model_bio = models.TextField(verbose_name="model xaqida malumot",null=True,blank=True)
    model_logo = models.ImageField(upload_to='photos/',verbose_name="model rasmi",null=True,blank=True)

    def __str__(self):
        return self.model_name



class Cars(models.Model):
    car_name = models.CharField(max_length=100,unique=True,verbose_name='moshina oti')
    car_bio = models.TextField(null=True,blank=True,verbose_name='Moshina haqida malaumot')
    car_color = models.CharField(max_length=50,verbose_name='moshina rangi')
    photo = models.ImageField(upload_to='photos/',verbose_name='moshina rasmi')
    model = models.ForeignKey(Models,verbose_name='modelni kiriting',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.TimeField(auto_now=True,blank=True,null=True)


    def __str__(self):
        return self.car_name