from django.urls import path
from .views import customer_corr_view

app_name = 'customer'


urlpatterns = [
          path('', customer_corr_view, name = 'main-customer-view'),
]
