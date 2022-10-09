from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView
from .models import Blog 
# # Create your views here.
# posts = {
#     "tech" : "this is tech stack",
# }
# posts_collection = [
    
# ]
# def get_date(post):
# #     return post['date']
# class CommentHandle(View):
#     def post(self, request):
#         comment = request.POST
        
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Blog
    ordering = ["-date_d"]
    context_object_name = "posts"
    def get_queryset(self) :
        data =  super().get_queryset()
        data = data[:3]
        return data
# def starting_page(request):
#     posts_collection = Blog.objects.all().order_by("-date_d")[:3]
  
#   #sliced the last 3 elements
#     return render(request,'blog/index.html',{
#         "posts" : posts_collection,
#     })
    # return HttpResponse("everythonng working")
def posts(request):
    posts_collection = Blog.objects.all().order_by("-date_d")
    return render(request,'blog/posts.html',{
        "posts":posts_collection,
    })
def post_detail(request,slug):
    # identified_post = Blog.objects.get(slug=slug) I commented it because it might get error so we have another good django alternative
    identified_post = get_object_or_404(Blog,slug=slug)
    return render(request,'blog/post-detail.html',{
        "post":identified_post,
        "tags": identified_post.tags.all(),
    })