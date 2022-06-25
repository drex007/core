from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
     path('cols/', views.get_cols_data, name='cols'),
      path('branches/<str:branch>/', views.get_json_model_data, name='get-branch-cols'),
]