from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.AddLaptopView.as_view(),name='add_laptop'),
    path('show',views.ShowLaptopView.as_view(),name='show_laptop'),
    path('delete/<int:i>/',views.LaptopDelete.as_view(),name='delete_laptop'),
    path('update/<int:i>/',views.LaptopUpdate.as_view(),name='update_laptop'),

]