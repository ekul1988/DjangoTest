from django.apps import AppConfig

from .import views

class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dtp.billing'
