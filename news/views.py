from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# class PostList(APIView):
#     response_data = {
#         'reservations': get_reservations_count_and_sum_from_date(date_sold),
#         'tickets': get_tickets_count_and_sum_from_date(date_sold),
#         # 'wszystkie': wszystkie,
#     }

    # return Response(data=response_data, status=status.HTTP_200_OK)
class PostListAPIView(ListAPIView):
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination
    # parser_classes = (XMLParser,)
    # renderer_classes = (XMLRenderer, JSONRenderer,)

	#renderer_classes = (XMLRenderer, JSONRenderer, )

    # def get(self, request):
    #     queryset = Post.objects.all()
    #     serializer_class = PostSerializer(queryset, many=True)
    #     # results = {'posts': serializer.data}
    #
    #     return Response(serializer_class.data)
    #
    # def post(self):
    #     pass

class PostDetailApiView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    #lookup_field = 'slug'

class PostDeleteApiView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    #lookup_field = 'slug'

class PostUpdateApiView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    #lookup_field = 'slug'
