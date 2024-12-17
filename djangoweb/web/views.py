from django.shortcuts import render
from django.http import HttpResponse

posts = [
  {
    'author': 'haekalhilmi',
    'title': 'Sejarah Organisasi Kemahasiswaan Informatika',
    'content': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Hic libero assumenda odio atque eius veritatis minima nulla.',
    'date_post': '17th December 2024'
  },
  {
    'author': 'MMFRXX',
    'title': 'Perampasan Ruang Kreasi Mahasiswa',
    'content': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Hic libero assumenda odio atque eius veritatis minima nulla.',
    'date_post': '20th December 2024'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'home.html', context)

def about(request):
  return render(request, 'about.html', {'title' : "Tentang Kami"})