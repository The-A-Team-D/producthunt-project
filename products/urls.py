from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.Create, name = 'create'),
    path('<int:product_id>',views.Detail, name = 'detail'),
    path('<int:product_id>/upvote',views.Upvote, name = 'upvote'),
]