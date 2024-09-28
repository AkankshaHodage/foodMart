from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User, UserProfile
from django.contrib import messages,auth
from Restaurant.forms import RestaurantForm
from .utils import detecUser 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

# Create your views here.

def check_role_restaurnat(user):
    if user.role  == 1:
        return True 
    else :
        raise PermissionDenied


def check_role_customer(user):
    if user.role  == 2:
        return True 
    else :
        raise PermissionDenied
    

def registerUser(request):
    if request.user.is_authenticated:
            messages.warning(request,"You are already logged in")
            return redirect("myAccount")
        

    elif request.method == 'POST':
        # print(request.POST)
            #print('out')
        form = UserForm (request.POST)


        if form.is_valid():
            print("in if part")
            password = form.cleaned_data['password']
            
            confirm_password=form.cleaned_data['confirm_password']
            
            #form.save()
            user = form.save(commit = False)# before save it will check  allfileds are their or not
            
            user.set_password(password)
            #user.set_confirm_password(confirm_password)
            if (password==confirm_password):
                #print("in if part")
                user.role = User.CUSTOMER 
                form.save()
                messages.success(request,"Your account has been registered successfully.....!")
                return redirect("registerUser")
            else :
                #print("wrong password")
                messages.error(request,"Password and confirm_password have to be same try again........!")
                

                return redirect("registerUser")# to get the redirect here then in 1st line have to import redirect first then only it will redirect 
                # registerUser is getting form the urls name=
          
        else:
            print("in else part")
            messages.error(request,"invalid form .......!")
            return redirect("registerUser")
            

            #if dont have POST method
    form = UserForm()
    context={
                'form':form,

            }
   
    return render(request,'accounts/registerUser.html',context)

def registerRestaurant(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect("myAccount")
    
    elif request.method=='POST':
        form=UserForm(request.POST)
        r_form=RestaurantForm(request.POST,request.FILES)
         
        if form.is_valid() and r_form.is_valid():
            user=form.save(commit=False)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
           # confirm_password = form.cleaned_data['confirm_password']
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)#,confirm_password=confirm_password)
            user.role = User.RESTAURANT
            user.save()
            restaurant = r_form.save(commit=False)
            restaurant.user = user
            user_profile = UserProfile.objects.get(user=user) 
            restaurant.user_profile = user_profile
            restaurant.save()
            messages.success(request,"Your account has been registered sucessfully ....!")
            return redirect("registerRestaurant")
               

        else:
            print('invalid form')
            print(form.errors)
             

    else:
        form =UserForm()
        r_form=RestaurantForm()
    context={
            'form':form,
            'r_form': r_form,
        }

    return render(request, 'accounts/registerRestaurant.html',context)

def login(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect("myAccount")
    
    
    elif request.method =="POST":
        email = request.POST["email"]
        password =request.POST['password']
        user =auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now logged in ")
            return redirect('myAccount')

        else:
            messages.error(request,'Invalkid login credatials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'You are logged out.')
    return redirect('login')

def dashboard(request):
    return render(request,'accounts/dashboard.html')

@login_required(login_url ="login")
def myAccount(request):
    user =request.user
    redirectUrl = detecUser(user)
    return  redirect(redirectUrl)

@login_required(login_url ="login")
@user_passes_test(check_role_restaurnat)
def RestaurantDashboard(request):
    return render (request ,"accounts/RestaurantDashboard.html")

@login_required(login_url ="login")
@user_passes_test(check_role_customer)
def custDashboard(request):
    return render (request, "accounts/custDashboard.html")



    