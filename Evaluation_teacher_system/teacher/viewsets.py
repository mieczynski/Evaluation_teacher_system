from django.core.paginator import Paginator
from rest_framework import status, viewsets

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Evaluation_teacher_system.teacher.models import Teacher
from Evaluation_teacher_system.teacher.serializers import CreateTeacherSerializer, ListTeacherSerializer, \
    GetTeacherSerializer


class CreateTeacherViewSet(viewsets.ModelViewSet):  # handles POSTs
    serializer_class = CreateTeacherSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()

        return Response({
            "teacher": serializer.data,

        }, status=status.HTTP_201_CREATED)


class ListTeacherViewSet(viewsets.ModelViewSet):
    serializer_class = ListTeacherSerializer
    http_method_names = ['get']
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        filter = request.GET.get('filter')
        filterType = request.GET.get('filterType')
        obj_per_page = 6
        paginator = Paginator(serializer.list(filterType, filter), obj_per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if int(page_number) <= int(paginator.num_pages):
            return Response({
                "teachers_list": page_obj.object_list,
                "page_count": paginator.num_pages
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "teachers_list": [],

            }, status=status.HTTP_201_CREATED)


class GetTeacherViewSet(viewsets.ModelViewSet):
    serializer_class = GetTeacherSerializer
    http_method_names = ['get']
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        teacher_id = self.request.GET.get('teacher_id')
        queryset = Teacher.objects.filter(pk=teacher_id)
        return queryset
