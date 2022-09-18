from django.contrib import admin
from django.urls import path

from words import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('random/', views.RandomText.as_view()),

]
