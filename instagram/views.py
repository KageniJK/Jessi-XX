from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
from .forms import UpdateProfile


@login_required(login_url='/accounts/login/')
def index(request):
    user = request.user
    profile = Profile.get_user(user.id)
    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            profile = Profile(bio=bio, user=user)
            profile.save()

            HttpResponseRedirect('home')
    else:
        form = UpdateProfile()
    return render(request, 'profile.html', {'user': user, 'profile': profile, 'form': form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'pic' in request.GET and request.GET['pic']:
        search_term = request.GET.get('pic')
        search_pics = Image.search_images(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})