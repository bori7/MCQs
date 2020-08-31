from django.urls import path, include
from rest_framework import routers
from Questions import views
from .views import HomeListView, AssignmentViewSet,QuestionViewSet,GradedAssignmentViewSet
from .models import LogMessage


router = routers.DefaultRouter()
router.register(r'api/assignments',AssignmentViewSet, basename = 'assignments')
router.register(r'api/gradedassignments',GradedAssignmentViewSet, basename = 'gradedassignments')
router.register(r'api/questions',QuestionViewSet,basename =  'questions')


home_list_view = HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="Questions/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path('', include(router.urls)),
]
urlpatterns += router.urls