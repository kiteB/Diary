from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q


def home(request):
    diaries= Diary.objects.all().order_by('-pub_date')          # pub_date 필드를 기준으로 내림차순 정렬
    paginator = Paginator(diaries, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'home.html', {'diaries': page})

def search(request):
    diaries= Diary.objects.all().order_by('-pub_date')          # pub_date 필드를 기준으로 내림차순 정렬
    search_text = request.GET.get('search_text')
    if search_text:
        diaries = diaries.filter(Q(body__icontains=search_text) | Q(title__icontains=search_text))
        paginator = Paginator(diaries, 3)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
        return render(request, 'search.html', {'diaries': page, 'search_text': search_text})
    
    return render(request, 'search.html')


def detail(request, id):
    diary = get_object_or_404(Diary, pk=id)
    return render(request, 'detail.html', {'diary': diary})


def make_diary(request):
    if request.method == 'POST':
        new_diary = Diary()
        new_diary.title = request.POST['title']
        new_diary.image = request.FILES.get('image')
        new_diary.body = request.POST['body']
        new_diary.pub_date = timezone.now()
        new_diary.weather = request.POST['weather']
        new_diary.save()
        return redirect('home')
    else:
        return render(request, 'new.html')


def delete(request, id):
    delete_diary = Diary.objects.get(id=id)
    delete_diary.delete()
    return redirect('home')
