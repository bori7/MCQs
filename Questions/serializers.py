from rest_framework import serializers
from .models import LogMessage, Assignment, Choice, Question, GradedAssignment


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value

class LogMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogMessage
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):
    title = StringSerializer(many=False)
    class Meta:
        model = Assignment
        fields = '__all__'

    def get_questions(self, obj):
        questions = QuestionSerializer(obj.questions.all(), many=True).data
        return questions    


class QuestionSerializer(serializers.ModelSerializer):
    choices = StringSerializer(many=True)
    answer = StringSerializer(many=False)
    assignment = StringSerializer(many=False)
    class Meta:
        model = Question
        fields = '__all__'
        
class GradedAssignmentSerializer(serializers.ModelSerializer):
    assignment = StringSerializer(many=False)
    class Meta:
        model = GradedAssignment
        fields = '__all__'

    def create(self, request):
        data = request.data
        print(data)     

        assignment = Assignment.objects.get(id=1)
        grader = GradedAssignment()
        answer = {}
        for key, value in data.items():
            if key != 'csrfmiddlewaretoken':
                answer[key] = value
        print(answer)         

        questions = [q for q in assignment.questions.all()]
        
        correct = 0

        
        for k, v in answer.items():
            if answer[k] == questions[int(k)-1].answer.title:
                correct += 1

        grade = ((correct * 5) / 50)*100
        grader.grade = grade
        grader.asnt = 'IELTS'
        grader.save()
        print(grade) 
        return grader

        
                               