from django.urls import path
from sub_proj import views
from .views import index,about,faq,contact,coming_soon,blog,blog_1_details,blog_2_details,blog_3_details,login,signup,crop_rec,plants,CropRecommendation

urlpatterns = [
    #path("", home),
    path('', index),
    path('CropRecommendation/', CropRecommendation),
    path('about/', about),
    path('coming_soon/', coming_soon),
    path('faq/', faq),
    path('contact/', contact),
    path('crop_rec/', crop_rec),
    path('plants/', plants),
    
    path('login/', login),
    path('signup/', signup),

    path('blog/', blog),
    path('blog_1_details/', blog_1_details),
    path('blog_2_details/', blog_2_details),
    path('blog_3_details/', blog_3_details)
]