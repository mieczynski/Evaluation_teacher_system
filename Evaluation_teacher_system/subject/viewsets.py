from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Evaluation_teacher_system.subject.serializers import CreateSubjectSerializer, ListSubjectSerializer


class CreateSubjectViewSet(viewsets.ModelViewSet):  # handles POSTs
    serializer_class = CreateSubjectSerializer
    http_method_names = ['post']
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        subject = serializer.save()
        return Response({
            "subject": serializer.data,

        }, status=status.HTTP_201_CREATED)


class ListSubjectViewSet(viewsets.ModelViewSet):
    serializer_class = ListSubjectSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    def list(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "Subjects_list": serializer.list(),

        }, status=status.HTTP_201_CREATED)
