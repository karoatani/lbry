from rest_framework import routers
from .views import AuthorView
router = routers.SimpleRouter()

router.register('author', AuthorView)

urlpatterns = router.urls
