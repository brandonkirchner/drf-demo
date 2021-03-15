from rest_framework import routers

from core.views import StudentViewSet, UniversityViewSet, ClassViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)
router.register(r'classes', ClassViewSet)

urlpatterns = router.urls
