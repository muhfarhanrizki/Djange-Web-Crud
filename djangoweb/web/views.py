from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
  return render(request, 'blog/about.html', {'title' : "Tentang Kami"})

class PostListView(LoginRequiredMixin, ListView):
  model = Post
  template_name = 'blog/home.html'
  context_object_name = 'posts'
  ordering = ["-date_posted"]
  

class PostDetailView(LoginRequiredMixin, DetailView):
  model = Post
  template_name = 'blog/post_detail.html'
  
class PostCreateView(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_form.html'
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
  
  
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_form.html'
    
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
    
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False
  
class PostDeleteView(DeleteView):
  model = Post
  template_name = 'blog/post_confirm_delete.html'
  success_url = '/'
  
  
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False