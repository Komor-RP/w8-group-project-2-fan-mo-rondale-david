from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import (
    UserSerializer,
    StarredItemSerializer,
    QuestionSerializer,
<<<<<<< HEAD
    AnswerSerializer)
=======
    AnswerSerializer
)
>>>>>>> master
from questions.models import User, StarredItem, Question, Answer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.permissions import (
    IsAuthorOrReadOnly,
    IsStarOwnerOrReadOnly,
    IsAnswerOwnerOrReadOnly
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions': reverse('question-list', request=request, format=format),
        'stars': reverse('star-list', request=request, format=format),
    })


class UserListView(generics.ListAPIView):
    """
    Retrieves list of all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Detail page for a single user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserQuestionListView(generics.ListAPIView):
    """ 
    Retrieves author's list of questions
    """
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Question.objects.filter(author=user.id)


class UserAnswerListView(generics.ListAPIView):
    """ 
    Retrieves author's list of answers
    """
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user = self.request.user
        return Answer.objects.filter(author=user.id)


class StarredItemList(generics.ListCreateAPIView):
    """
    Retrieves list of starred items
    TODO = make it specific for a logged in user
    """
    queryset = StarredItem.objects.all()
    serializer_class = StarredItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StarredItemDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves details of starred item
    Only owners and remove their stars
    TODO = make it specific for a logged in user
    """
    queryset = StarredItem.objects.all()
    serializer_class = StarredItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsStarOwnerOrReadOnly)


class QuestionListView(generics.ListCreateAPIView):
    """
    Retrieves list of questions
    Allows logged in users to submit new questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionDetailView(generics.RetrieveDestroyAPIView):
    """
    Retrieves details of one question
    Allows only authors to destroy their questions
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,)


class QuestionsByUserListView(generics.ListAPIView):
    """
    Retrieves list of questions by selected user
    """
    serializer_class = QuestionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = User.objects.get(pk=pk)
        return Question.objects.filter(author=user)
 
class AnswersByUserListView(generics.ListAPIView):
    """
    Retrieves list of answers by selected user
    """

class AnswerDetailView(generics.RetrieveDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAnswerOwnerOrReadOnly)


class QuestionAnswerList(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = User.objects.get(pk=pk)
        return Answer.objects.filter(question=self.kwargs['pk'])

    def perform_create(self, serializer):
        question = Question.objects.get(pk=self.kwargs['pk'])
        serializer.save(author=self.request.user, question=question)

