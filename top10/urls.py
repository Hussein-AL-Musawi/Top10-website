from django.urls import path
from .import views

urlpatterns = [
    path("movies",views.top10_movies,name='top10'),
    path("rich",views.top10_rich,name="top10_rich"),
    path('insta',views.top10_instgram,name= 'top10_instgram'),
    path('youtube_channels',views.top10_youtube_channels,name  ='top10_youtube_channels'),
    path('influential_persons',views.top10_Influential_Persons,name="top10_Influential_Persons"),
    path('internt_companies',views.top10_internet_companies,name= "top10_internt_companies"),
    path('videos',views.top10_videos,name='videos'),
    path('series',views.top10_series,name='series'),
    path('popluations',views.top10_popluations,name='popluations'),
    path('largest_contries',views.top10_largest_contries,name='largest_contries'),
    path('cheapist_laptops',views.top10_cheap_laptops,name='cheapist_laptops'),
    path('best_phones',views.top10_phones,name='best_phones'),
    path('gaming_laptops',views.top10_gaming_laptops,name='gaming_laptops'),
    path('useful_apps',views.top10_useful_apps,name='useful_apps'),
    path('',views.home,name='home')
    








]
