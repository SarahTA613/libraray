from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowAllBooks, name='showBooks'),
    path('book/<int:pk>/', views.bookDetail, name='book'),
    path('addBook/', views.addBook, name='addBook'),
    path('updateBook/<int:pk>/', views.updateBook, name='updateBook'),
    path('deleteBook/<int:pk>/', views.deleteBook, name='deleteBook'),
    path('search/', views.searchBar, name='search'),
    path('login/',views.LoginPage,name='login'),
    #path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('signup/',views.SignupPage,name='signup'),
    
]