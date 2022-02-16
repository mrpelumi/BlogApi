from posixpath import basename
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserList,PostList

router = SimpleRouter()
router.register('users',UserList,basename='users')
router.register('',PostList,basename='posts')

urlpatterns = router.urls
