from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('DlAPI', views.ApprovalsDlView)
urlpatterns = [
    path('dl-form/',views.sctcontact, name='dlform'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
]