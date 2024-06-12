from django.shortcuts import render, redirect

from django.core.validators import validate_email

from django.contrib.auth.models import User, Group

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.core.mail import EmailMessage

from SystemConf.Back_Control_Access import is_admin

# Create your views here.

def sing_in(request):

    if request.method == "POST":

        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()

        if user:

            auth_user = authenticate(username=user.username, password=password)

            if auth_user:

                login(request, auth_user)
                return redirect('home')

            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

    return render(request, 'authentification/login.html', {})

def sing_up(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"
        
        # register
        if error == False:
            user = User(
                username = name,
                email = email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.save()

            return redirect('sing_in')

            #print("=="*5, " NEW POST: ",name,email, password, repassword, "=="*5)

    context = {
        'error':error,
        'message':message
    }
    return render(request, 'authentification/register.html', context)

# def sing_up(request):
# 	if request.method=="POST":
# 		created=True
# 		try:
# 			user=User.objects.create_user(username=request.POST.get("username"), email=request.POST.get("email"), password=request.POST.get("password"))
# 			user.first_name=request.POST.get("nom")
# 			user.is_active=False
# 			user.save()
# 			message="Votre compte a bien été crée. \n Merci d'attendre l'atendre l'activation du compte. Si cela met du temps informé votre administrateur !!!!!"
# 			login(request, user)

# 		except Exception as e:
# 			created=False
# 			data={
# 					'username':request.POST.get("username"), 
# 					'email':request.POST.get("email"), 
# 					'nom': request.POST.get("nom"),
# 					'password':request.POST.get("password"),
# 					'message':'Cet utilisateur existe déjà. '
# 				}

# 		if created:
# 			return render(request, 'authentification/waiting_page.html',{'message':message})
# 		else:
# 			return render(request,'authentification/register.html',data)
		
# 	else:

# 		return render(request,'authentification/register.html')

def log_out(request):
    logout(request)
    return redirect('sing_in')


def forgot_password(request):
    error = False
    success = False
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            print("processing forgot password")
            html = """
                <p> Hello, merci de cliquer pour modifier votre email </p>
            """

            msg = EmailMessage(
                "Modification de mot de pass!",
                html,
                "soroib0879@gmail.com",
                ["soro4827@gmail.com"],
            )

            msg.content_subtype = 'html'
            msg.send()
            
            message = "processing forgot password"
            success = True
        else:
            print("user does not exist")
            error = True
            message = "user does not exist"
    
    context = {
        'success': success,
        'error':error,
        'message':message
    }
    return render(request, "authentification/forgot_password.html", context)


def update_password(request):
    return render(request, "authentification/update_password.html", {})




@is_admin
def list_user(request):
	data=User.objects.filter(is_superuser=False)
	groupes=Group.objects.all()
	return render(request,'authentification/list.html',{'data':data,'groupes':groupes})

@is_admin
def user_state(request):
	if request.method=="POST":
		user=User.objects.get(id=request.POST.get('id_utilisateur') )
		user.is_active=request.POST.get('state')
		user.save()
	return redirect('user_list')

@is_admin
def set_profil(request):
	if request.method=="POST":
		role=request.POST.get('role')
		user=User.objects.get( id=request.POST.get('id_utilisateur') )
		is_same_role=user.groups.filter(name=role).exists()
		if not  is_same_role:
			group=user.groups.first()
			if not (group is None):
				user.groups.remove(group)
			grp=Group.objects.get(id=role)
			user.groups.add(grp)
			user.save()
						
	return redirect('user_list')



def get_role(request, user_id):
	user=User.objects.get( id=int(user_id) )
	group=user.groups.first()
	if group is None:
		role = 'AUCUN'
	else:
		role=group.name
	return JsonResponse({'role':role})#HttpResponse(data, content_type='application/json')


