from django.db import models

# Create your models here.
class ComputerBrands(models.Model):
    brand_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='media')

    def __str__(self):
        return self.brand_name


class ComputerGeneration(models.Model):
    generation = models.CharField(max_length=100)

    def __str__(self):
        return self.generation

class ComputerSpecification(models.Model):
    generation = models.ForeignKey(ComputerGeneration, on_delete=models.CASCADE)
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    ram = models.PositiveSmallIntegerField()
    brand = models.ForeignKey(ComputerBrands,on_delete=models.CASCADE, related_name='brand')

    def __str__(self):
        return self.brand.brand_name

class Computer(models.Model):
    computer_code = models.CharField(max_length=100, unique=True)
    computer = models.ForeignKey(ComputerGeneration,on_delete=models.CASCADE, related_name='computer')
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return self.computer_code
