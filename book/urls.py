from rest_framework import routers
from .views import BookView,CategoryView
from django.urls import path
from django.views.generic import TemplateView
router = routers.SimpleRouter()
router.register('books', BookView)
router.register('category', CategoryView)
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
]

urlpatterns += router.urls
