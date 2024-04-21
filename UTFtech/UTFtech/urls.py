from django.contrib import admin
from django.urls import path
from dishes.views import CategoriesAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/', CategoriesAPIView.as_view(), name='food_category_list'),
]
