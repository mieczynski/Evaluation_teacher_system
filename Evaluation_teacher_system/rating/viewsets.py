from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Evaluation_teacher_system.rating.serializers import CreateRatingSerializer, ListRatingSerializer


class CreateRatingViewSet(viewsets.ModelViewSet):  # handles POSTs
    serializer_class = CreateRatingSerializer
    http_method_names = ['post']
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rating = serializer.save()
        return Response({
            "rating": serializer.data,
        }, status=status.HTTP_201_CREATED)


class ListRatingViewSet(viewsets.ModelViewSet):
    serializer_class = ListRatingSerializer
    http_method_names = ['get']
    permission_classes = (AllowAny,)

    def list(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj_per_page = 6;
        teacher_id = request.GET.get('teacher_id')
        paginator = Paginator(serializer.list(teacher_id), obj_per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if int(page_number) <= int(paginator.num_pages):
            return Response({
                "ratings_list": page_obj.object_list,
                "page_count": paginator.num_pages

            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "ratings_list": [],

            }, status=status.HTTP_201_CREATED)