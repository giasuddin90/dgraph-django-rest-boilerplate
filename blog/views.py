from rest_framework.views import APIView
from rest_framework.response import Response
from blog.serializers import BlogCreateSerializer, BlogSerializer
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR)
from blog.models import Blogs
from service.prepare_response import prepare_success_response, prepare_error_response
from service.log import *


class BlogListView(APIView):
    """
    This function will create post
    """

    def get(self, request):
        try:
            posts_data = Blogs.blog_list()
            serializer = BlogSerializer(posts_data, many=True)
            return Response(prepare_success_response(serializer.data), status=HTTP_200_OK)
        except Exception as e:

            return Response(
                prepare_error_response(str(e)),
                status=HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        """
        This function will be used for post create
        """
        serializer = BlogCreateSerializer(data=request.data)
        if serializer.is_valid():
            data = Blogs.create_blog(request.data)
            return Response(prepare_success_response(data), status=HTTP_200_OK)
        else:
            Log.general_log(str(serializer.errors), "post_create_request_error")
            return Response(prepare_error_response(serializer.errors), status=HTTP_400_BAD_REQUEST)


class BlogDetailView(APIView):
    """
    Difficulty level detail view
    """

    def get(self, request,  **kwargs):
        blog_id = kwargs.get('blog_id')
        try:
            blog_data = Blogs.get_blog(blog_id)
            serializer = BlogSerializer(blog_data)
            return Response(prepare_success_response(serializer.data), status=HTTP_200_OK)
        except Exception as e:
            ex_message = str(e)
            return Response(
                prepare_error_response(ex_message),
                status=HTTP_400_BAD_REQUEST)

    def put(self, request,  **kwargs):
        """
        This function will be used for blog update
        """
        serializer = BlogCreateSerializer(data=request.data)
        blog_id = kwargs.get('blog_id')
        if serializer.is_valid():
            data = Blogs.update(blog_id, request.data)
            return Response(prepare_success_response(data), status=HTTP_200_OK)
        else:
            Log.general_log(str(serializer.errors), "blog_update_request_error")
            return Response(prepare_error_response(serializer.errors), status=HTTP_400_BAD_REQUEST)

    def delete(self, request,  **kwargs):
        """
        This function will be used for post create
        """
        blog_id = kwargs.get('blog_id')
        try:
            difficulty_level_data = Blogs.get_blog(blog_id)
            if difficulty_level_data:
                data_delete = Blogs.delete(blog_id)
                print(data_delete)
                message = "Data deleted successfully id :" + str(blog_id)
                return Response(prepare_success_response(message), status=HTTP_200_OK)
            else:
                message = "No Data found id :" + str(blog_id)
                return Response(prepare_success_response(message), status=HTTP_200_OK)

        except Exception as e:
            ex_message = str(e)
            return Response(
                prepare_error_response(ex_message),
                status=HTTP_400_BAD_REQUEST)

