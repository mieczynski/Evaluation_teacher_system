from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Evaluation_teacher_system.application.serializers import CreateApplicationSerializer, ListApplicationSerializer, \
    UpdateApplicationSerializer


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


class ConfirmApplicationViewSet(viewsets.ModelViewSet):  # handles POSTs
    serializer_class = UpdateApplicationSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.confirm(request.data)
        if application:
            return Response({
                "application": application,

            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "application": application,

            }, status=status.HTTP_400_BAD_REQUEST)


class DeleteApplicationViewSet(viewsets.ModelViewSet):  # handles POSTs
    serializer_class = UpdateApplicationSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.delete(request.data)
        if application:
            return Response({
                "application": application,

            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "application": application,

            }, status=status.HTTP_400_BAD_REQUEST)


class ListApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ListApplicationSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    def list(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        filterType = request.GET.get('filterType')
        obj_per_page = 6
        paginator = Paginator(serializer.list(filterType), obj_per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if int(page_number) <= int(paginator.num_pages):
            return JsonResponse({
                "applications_list": page_obj.object_list,
                "page_count": paginator.num_pages
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "applications_list": [],

            }, status=status.HTTP_201_CREATED)
