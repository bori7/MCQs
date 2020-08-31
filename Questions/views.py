from datetime import datetime
from django.utils import timezone
from django.shortcuts import redirect
from .models import Assignment,GradedAssignment, Question
from .serializers import  AssignmentSerializer, QuestionSerializer, GradedAssignmentSerializer
from rest_framework import viewsets, renderers, permissions
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_400_BAD_REQUEST)
from django.views.generic import ListView
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
        #print(request.data)
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


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    queryset = Question.objects.all()
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
