from django.shortcuts import render
from django.http import HttpResponse




def checkCredentials(request, email, password):
	adminEmail = "admin@boulou.energy"
	adminPassword = "admin"
	# supposons que l'utilisateur est authentifie
	return True


def home(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		if checkCredentials(request, email, password):
			return render(request, 'home.html')
	else:
		return render(request, 'login.html')
	return render(request, 'home.html')
