from django.conf.urls import url
from django.urls import path
from . import views
from .views import InventoryView

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>/<nickname>/', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('next', views.next, name='next'),
    # path('form', views.form, name='form'),
    url(r'', InventoryView.as_view(), name='index'),
    ]
