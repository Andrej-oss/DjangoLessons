from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class OfficeModel(models.Model):
    class Meta:
        db_table = 'OFFICE'

    name = models.CharField(max_length=20, validators=[RegexValidator('^[a-zA-Z]{2,10}$',
                                                                      'should be a-z and 2-10 symbols')])
    city = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} - {self.city}'

    def __repr__(self):
        return self.__str__()


class EmployeeModel(models.Model):
    class Meta:
        db_table = 'EMPLOYEE'
    name = models.CharField(max_length=20, validators=[RegexValidator('^[a-zA-Z]{2,10}$',
                                                                      'should be a-z and 2-10 symbols')])
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    office = models.ForeignKey(OfficeModel, related_name='employees', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.city}'

    def __repr__(self):
        return self.__str__()
