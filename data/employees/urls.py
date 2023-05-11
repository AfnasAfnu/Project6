from django.urls import path
from django.urls.conf import path
from . import views
urlpatterns = [
    path('',views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('destroy/<int:id>', views.destroy),
]
