from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.
def registerUser(request):

    if request.method == 'POST':
       # print(request.POST)
        #print('out')
        form = UserForm (request.POST)
        
        if form.is_valid():
            print("in if part")
            password = form.cleaned_data['password']
            #confirm_password=form.cleaned_data['confirm_password']
            #form.save()
            user = form.save(commit = False)# before save it will check  allfileds are their or not
            user.set_password(password)
           # user.set_confirm_password(confirm_password)
            
            user.role = User.CUSTOMER 
            form.save()
            messages.success(request,"Your account has been registered successfully.....!")
            return redirect("registerUser")# to get the redirect here then in 1st line have to import redirect first then only it will redirect 
            # registerUser is getting form the urls name=
        else:
            messages.error(request,"invalid form .......!")
            return redirect("registerUser")
    else:
        #if dont have POST method
        print("in else part")
        form = UserForm()
        context={
            'form':form,

        }
    form = UserForm()
    context={
            'form':form,

        }

    return render(request,'accounts/registerUser.html',context)