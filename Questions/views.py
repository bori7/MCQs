from django.shortcuts import render
import re
from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import LogMessageForm
from .models import LogMessage, Assignment,GradedAssignment, Question
from .serializers import LogMessageSerializer, AssignmentSerializer,QuestionSerializer, GradedAssignmentSerializer
from rest_framework import viewsets, renderers, permissions
from django.views.generic import ListView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)
# Create your views here.

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AssignmentSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)


    def list(self, request, *args, **kwargs):
        queryset1 = Assignment.objects.all()
        serializer1 = AssignmentSerializer(queryset1, many=True)
        queryset2 = Question.objects.all()
        #questions = [q for q in assignment.questions.all()]
        serializer2 = QuestionSerializer(queryset2, many=True)
        
        return Response({'assignment_list': serializer1.data,
                         'question_list': serializer2.data}, template_name='Questions/assignment.html')
       

    

class GradedAssignmentViewSet(viewsets.ModelViewSet):
    queryset = GradedAssignment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GradedAssignmentSerializer
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def create(self, request):
        print(request.data)
        serializer = GradedAssignmentSerializer()
        grade = serializer.create(request)
        # if serializer.is_valid(raise_exception=True):
        #     assignment = serializer.create(request)
        if grade:
            return redirect("gradedassignments-list")
        return Response(status=HTTP_400_BAD_REQUEST,template_name='Questions/assignment.html')

    
    def list(self, request, *args, **kwargs):
        queryset = GradedAssignment.objects.all()
        serializer = GradedAssignmentSerializer(queryset, many=True)
        return Response({'result_list': serializer.data[-1]}, template_name='Questions/results.html')
        

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer


# def home(request):
#     return render(request, "Questions/home.html")

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    content2 = '<h3>{Hello there, " + clean_name + "!}</h3>'
    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return render(
        request,
        'Questions/hello_there.html',
        {
            'name': clean_name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "Questions/about.html")

def contact(request):
    return render(request, "Questions/contact.html")

# Add these to existing imports at the top of the file:


# Add this code elsewhere in the file:
def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now(tz=timezone.utc)
            message.save()
            return redirect("home")
    else:
        return render(request, "Questions/log_message.html", {"form": form})