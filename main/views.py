from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def masters(request):
    return render(request, 'masters.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        service = request.POST.get('service', '')
        master = request.POST.get('master', '')
        date = request.POST.get('date', '')
        comment = request.POST.get('comment', '')
        
        try:
            appointment = Appointment(
                name=name,
                phone=phone,
                service=service,
                master=master if master else '',
                date=date if date else None,
                comment=comment if comment else ''
            )
            appointment.save()
            print(f"✅ Заявка сохранена: {name} - {phone}")  # Для отладки
            messages.success(request, '✨ Спасибо за заявку! Наш администратор свяжется с вами в ближайшее время.')
        except Exception as e:
            print(f"❌ Ошибка сохранения: {e}")  # Для отладки
            messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте позже.')
        
        return redirect('contacts')
    
    return render(request, 'contacts.html') 