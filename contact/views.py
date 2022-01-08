from django.shortcuts import redirect, render
from .models import Contact

def Cont(request):

    if request.method == 'POST':
        data = request.POST
        text = Contact.objects.create(name=data['name'], sub=data['sub'], text=data['message'])
        return redirect('home')

    return render(request, 'contact/cont.html')
