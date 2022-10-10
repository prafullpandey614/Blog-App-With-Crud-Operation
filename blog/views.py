from django.shortcuts import render ,get_object_or_404
from django.views.generic import ListView ,  DetailView
from django.views import View
from .models import Blog 
from django.urls import reverse
from .forms import CommentForm
from django.http import HttpResponseRedirect
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
class AllPostsView(ListView):
    template_name = "blog/posts.html"
    model = Blog
    ordering = ["-date_d"]
    context_object_name = "posts"
# def posts(request):
#     posts_collection = Blog.objects.all().order_by("-date_d")
#     return render(request,'blog/posts.html',{
#         "posts":posts_collection,
#     })
class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Blog
    
    def get(self, request , slug): # here we can accept anything as parameter which comes through url
        post = Blog.objects.get(slug = slug)
        comments = post.comments.all()
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form" : CommentForm(),
            "comments": comments.order_by("-id")
        }
        return render(request, 'blog/post-detail.html', context)
    def post(self, request,slug):
        post = Blog.objects.get(slug = slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            
            comment =  comment_form.save(commit=False)
            comment.post = post
            comment.save()
            
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "tags": post.tags.all(),
            "comment_form" : CommentForm(request.POST),
            "comments" : post.comments.all().order_by("-id"),
        }
        return render(request, 'blog/post-detail.html', context)
    
    
   
    context_object_name= "post"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context
    
    
# def post_detail(request,slug):
#     # identified_post = Blog.objects.get(slug=slug) I commented it because it might get error so we have another good django alternative
#     identified_post = get_object_or_404(Blog,slug=slug)
#     return render(request,'blog/post-detail.html',{
#         "post":identified_post,
#         "tags": identified_post.tags.all(),
#     })