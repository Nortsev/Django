from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name="products"),
    path('<int:category_id>/', mainapp.products, name='product'),
    path('<int:page>/', mainapp.products, name='page'),
]



