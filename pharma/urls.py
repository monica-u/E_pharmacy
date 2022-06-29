from django.urls import path
from . import views

app_name = 'pharma'
urlpatterns = [
    path("index", views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('cart', views.OrderView.as_view(), name='cart'),   #should implement cartview
    path('post/<int:pk>/', views.ViewPostView, name='view'),
    path('post/<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('', views.register_request, name="register"),
    path("login", views.login_request, name="login"),

]
