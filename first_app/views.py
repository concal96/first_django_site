from django.shortcuts import render
from django.http import HttpResponseRedirect
#import new user form
from first_app.forms import NewUserForm
# Create your views here.

def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'first_app/index.html',context_dict)

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: Invalid Form')

    return render(request,'first_app/users.html',{'form':form})

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative_url_templates.html')
