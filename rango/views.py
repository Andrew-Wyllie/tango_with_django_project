from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import UserForm
from rango.forms import UserProfileForm


def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {}
	context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
	context_dict['categories'] = category_list
	
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.fliter(category=category)
		context_dict['page'] = pages
		context_dict['category']
	except Category.DoesNotExist:
		context_dict['category']
		context_dict['pages']

	return render(request, 'rango/category.html', context=context_dict)
	
def add_category(request):
	form = CategoryForm()

	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return redirect('/rango/')
		else:
			print(form.errors)
	return render(request, 'rango/add_category.html', {'form': form})

def register(request):

	registered = False

	if request.method == 'POST':

		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:

				profile.picture = request.FILES['picture']
				profile.save()
				registered = True

		else:

			print(user_form.errors, profile_form.errors)
	
	else:

		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'rango/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

@login_required
def restricted(request):
	return HttpResponce("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
logout(request)

return redirect(reverse('rango:index'))