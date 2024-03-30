from pyexpat.errors import messages
from django.shortcuts import redirect, render
from item.models import Category,Item
from .forms import SignupForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def index(request):
    # [0:6] get just 6 items
  
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    # print(categories[0].name)
    # print(items[1].image.url)
    return render(request,'core/index.html',{
        'categories':categories,
        'items':items
    })


def contact(r):
    return render(r,'core/contact.html')

def signup(request):
    #  if request.method == 'GET':
    #     form = SignupForm()
    #     return render(request, 'core/register.html', {'form': form}) 
    #  if request.method == 'POST':
    #     form = RegisterForm(request.POST) 
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         user.username = user.username.lower()
    #         user.save()
    #         # messages.success(request, 'You have singed up successfully.')
    #         login(request, user)
    #         return redirect('contact')
    #     else:
    #         return render(request, 'core/register.html', {'form': form})
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            # logen here is the name of login url
            return redirect('/login/')
    else:
        form = SignupForm()    

    return render(request,'core/signup.html',{'form':form})
