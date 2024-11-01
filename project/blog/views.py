from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.utils import translation
from django.conf import settings


def blog_detail(request, slug):
    lang_code = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'az')  
    translation.activate(lang_code) 
    
    
    
    blog = get_object_or_404(Blog, slug=slug)

    context = {'blog': blog,
               'LANGUAGE_CODE': lang_code,
               }
    return render(request, 'blog_detail.html', context)




# def blog_detail(request, slug):
#     blog = get_object_or_404(Blog, slug=slug)

#     # if blog.language == "English" and lang != "en":
#     #     return redirect('blog_detail', lang='en', slug=slug)
#     # elif blog.language == "Azerbaijan" and lang != "az":
#     #     return redirect('blog_detail', lang='az', slug=slug)

#     context = {'blog': blog}
#     return render(request, 'blog_detail.html', context)