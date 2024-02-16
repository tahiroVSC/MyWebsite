from django.shortcuts import render
from apps.contact.models import Contact
from apps.telegram_bot.views import get_text



# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact.objects.create(name=name, email=email, subject=subject, message=message, phone=phone)
        get_text(f"""
отправлен запрос на обратную связь 
                 
Имя {name}
Email {email}
Номер телефона {phone}
Обьект {subject}
Сщщбщиение {message}
""")
    return render(request, 'contact/contact.html', locals())