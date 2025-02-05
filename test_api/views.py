from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .serializers import GroupSerializer
# Create your views here.


@api_view()
def hello_word(request: Request) -> Response:
    return Response({'message': 'Hello Word' })


# class GroupListAPIView(APIView):
#     def get(self, request: Request) -> Response:
#         groups = Group.objects.all()

#         serializer = GroupSerializer(groups, many=True)
#         # data = [group.name for group in groups]
#         return Response({'group': serializer.data })

# class GroupListAPIView(ListModelMixin, GenericAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


#     def get(self, request: Request) -> Response:
#         return self.list(request)


class GroupListAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    