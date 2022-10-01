from django.contrib import admin

# Register your models here.
from api.models import MovieModel, RatingModel
from office.models import EmployeeModel, OfficeModel

admin.site.register(MovieModel)
admin.site.register(RatingModel)
admin.site.register(EmployeeModel)
admin.site.register(OfficeModel)
