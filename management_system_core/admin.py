from django.contrib import admin
from management_system_core.models import (
    Statistics,
    ElectronicProduct,
    OfficeProduct
)

admin.site.register(Statistics)
admin.site.register(ElectronicProduct)
admin.site.register(OfficeProduct)
