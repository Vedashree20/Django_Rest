from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
   #path('articlelist/', article_list),
   #path('articlelist/', ArticleAPIView.as_view()), #for class based view
   path('generic/article/<int:id>/', GenericAPIView.as_view()), #for generic view
   #path('detail/<int:pk>/', article_detail)
   #path('detail/<int:pk>/', ArticleDetails.as_view()),
   path('viewset/', include(router.urls)),
   path('viewset/<int:pk>/', include(router.urls))
]

