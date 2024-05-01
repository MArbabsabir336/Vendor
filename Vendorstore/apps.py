from django.apps import AppConfig

class VendorstoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Vendorstore'
    
    def ready(self):
        import Vendorstore.singals
