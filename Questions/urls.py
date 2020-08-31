from django.urls import path, include
from rest_framework import routers
from Questions import views
from .views import HomeListView, AssignmentViewSet,QuestionViewSet,GradedAssignmentViewSet


router = routers.DefaultRouter()
router.register(r'api/assignments',AssignmentViewSet, basename = 'assignments')
router.register(r'api/gradedassignments',GradedAssignmentViewSet, basename = 'gradedassignments')
router.register(r'api/questions',QuestionViewSet,basename =  'questions')


home_list_view = HomeListView.as_view(
    template_name="Questions/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path('', include(router.urls)),
]
urlpatterns += router.urls