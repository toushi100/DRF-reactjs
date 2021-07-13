
from django.urls import path,include
from . import views
from django.views.generic import TemplateView
app_name='blog_api'
urlpatterns = [

    path('<int:pk>/',views.PostDetail.as_view(),name='detailcreate' ),
    path('',views.PostList.as_view(),name='listcreate' ),
    path('category',views.CategoryList.as_view(),name='Categorylistcreate' ),
    path('category/<int:pk>',views.CategoryDetail.as_view(),name='CategoryDetail' ),

]
