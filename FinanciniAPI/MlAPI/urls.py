from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MlAPI', views.ApprovalsView)
urlpatterns = [
    path('ml-form/',views.sctcontact, name='mlform'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
]
