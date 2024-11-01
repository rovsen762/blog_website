

# def index(request):
#     language = request.COOKIES.get('selected_language', 'Azerbaijan')
#     blogs = Blog.objects.filter(language=language).order_by('-created_at')[:6]

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             form = ContactForm() 
#     else:
#         form = ContactForm() 

#     context = {
#         'blogs': blogs,
#         'form': form,
#         'selected_language': language,
#     }
    
#     response = render(request, 'index.html', context)
#     if 'selected_language' not in request.COOKIES:
#         response.set_cookie('selected_language', 'Azerbaijan')
#     if 'selected_language' in request.GET:
#         response.set_cookie('selected_language', request.GET['selected_language'])
        
    
#     return response

from blog.models import Blog
from django.shortcuts import redirect,render
from django.utils import translation
from django.conf import settings
from django.http import JsonResponse
from .models import Contact
import json
from .forms import ContactForm
 


def set_language(request, lang_code):
    
    translation.activate(lang_code)
    request.session['django_language'] = lang_code

    if lang_code == 'az':
        response = redirect('/az/')
    else:
        response = redirect('/en/')

    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response



def index(request):
    lang_code = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'en')  
    translation.activate(lang_code)

    current_path = request.path 

    if lang_code == 'az' and not current_path.startswith('/az/'):
        return redirect('/az/')
    elif lang_code == 'en' and not current_path.startswith('/en/'):
        return redirect('/en/')

    
    language_mapping = {
        'az': 'Azerbaijan',
        'en': 'English'
    }

    language = language_mapping.get(lang_code, 'English')  

    blogs = Blog.objects.filter(language=language, is_active=True).order_by('-created_at')[:6]
    context = {
        'blogs': blogs,
        'LANGUAGE_CODE': lang_code,
    }
    
    return render(request, 'index.html', context)




def save_contact(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        form = ContactForm(data)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Contact saved successfully'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



from django.shortcuts import redirect

def error_404_handler(request, exception):
    return redirect('index')