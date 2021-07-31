from django.contrib.auth.forms import AuthenticationForm
from authy.forms import EmployeeRegistrationForm, EmployerRegistrationForm
from django.contrib.auth.models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
@login_required(login_url="/accounts/login/")
def index(request):
    tml = "<h2>HI EMPLOYER ITS GLAD TO SEE YOU</h2>"
    return HttpResponse(tml)

@login_required(login_url="/accounts/login/")
def employee(request):
    tml = "<h2>HI EMPLOYER ITS GLAD TO SEE YOU</h2>"
    return HttpResponse(tml)


    return HttpResponse(request,'hI THERE')
def signup(request):
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         user.save()
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=user.username, password=raw_password)

    #         login(request, user)
    #         return redirect('login')
    # else:
    #     form = SignUpForm()
    return render(request, 'registration/registration_form.html')

class employer_register(CreateView):
    model = User
    form_class = EmployerRegistrationForm
    template_name = "employer_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")

class employee_register(CreateView):
    model = User
    form_class = EmployeeRegistrationForm
    template_name = "employee_register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")



@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html", {"form": AuthenticationForm})


def logout_request(request):
    logout(request)
    return redirect("login")
