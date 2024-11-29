from rest_framework.routers import SimpleRouter
from users.apps import UsersConfig

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', )

urlpatterns = [


] + router.urls
