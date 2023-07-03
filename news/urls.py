from django.urls import path
from news import views

urlpatterns = [
  path('scrape/', views.scrape, name="scrape"),
  path('', views.news_list, name="home"),
  # path('search/', views.search, name='search'),
]