from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse_lazy
from .models import med
from django.contrib.auth.models import User
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm

class IndexView(generic.ListView):
    template_name = 'pharma/index.html'
    context_object_name = 'med_list'

    def get_queryset(self):
        return med.objects.all()

class CreateView(generic.edit.CreateView):
    template_name = 'pharma/create.html'
    model = med
    fields = ['medName','price', 'quantity']
    success_url = reverse_lazy('pharma:index')
	
def ViewPostView(request, pk):
    Med = get_object_or_404(med, pk=pk)
    return render(request, 'pharma/view.html', {'Med': Med})

class UpdateView(generic.edit.UpdateView):
    template_name = 'pharma/update.html'
    model = med
    fields = ['medName','price', 'quantity']
    success_url = reverse_lazy('pharma:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'pharma/delete.html'
    model = med
    success_url = reverse_lazy('pharma:index')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)   
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("pharma:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="pharma/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("pharma:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="pharma/login.html", context={"login_form":form})