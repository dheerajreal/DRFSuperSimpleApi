from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from api.models import Blog

# Create your views here.
from api.serializer import BlogSerializer


class BlogListView(ListAPIView):
    queryset = Blog.objects.all()
    lookup_field = "pk"
    serializer_class = BlogSerializer


class BlogRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    lookup_field = "pk"
    serializer_class = BlogSerializer
