from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets

from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from Evaluation_teacher_system.application.serializers import CreateApplicationSerializer


class CreateApplicationViewSet(viewsets.ModelViewSet):  # handles POSTs
    serializer_class = CreateApplicationSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save()
        return Response({
            "application": serializer.data,

        }, status=status.HTTP_201_CREATED)

