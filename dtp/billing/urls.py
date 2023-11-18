from django.urls import path
from . import views

app_name = 'billing'

urlpatterns = [
    path("", view=views.billing_home, name="home"),
    # ... other url patterns ...
]
