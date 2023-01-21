from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets

from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Evaluation_teacher_system.college.serializers import CreateCollegeSerializer, ListCollegeSerializer


class CreateCollegeViewSet(viewsets.ModelViewSet):  # handles POSTs
    serializer_class = CreateCollegeSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        college = serializer.save()
        return Response({
            "college": serializer.data,

        }, status=status.HTTP_201_CREATED)


class ListCollegeViewSet(viewsets.ModelViewSet):
    serializer_class = ListCollegeSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    def list(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "colleges_list": serializer.list(),

        }, status=status.HTTP_201_CREATED)
