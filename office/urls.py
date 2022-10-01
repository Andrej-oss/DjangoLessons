from django.urls import path

from office.views import OfficeView

urlpatterns = [
    path('', OfficeView.as_view())
]
