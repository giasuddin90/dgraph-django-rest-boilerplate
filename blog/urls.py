from django.urls import path
from django.conf.urls import url

from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path('blog', BlogListView.as_view(), name='blog-create'),
    path('blog/<blog_id>', BlogDetailView.as_view(), name='blog-detail-view'),

]
