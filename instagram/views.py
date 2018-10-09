from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
from .forms import UpdateProfile


@login_required(login_url='/accounts/login/')
def index(request):
    pics = Image.get_all()
    return render(request, 'timeline.html', {'pics': pics})


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    profiles = Profile.get_user(user.id)
    pics = Image.get_by_user(user.id)
    if request.method == 'POST':
        profile_form = UpdateProfile(request.POST, request.FILES)
        if profile_form.is_valid():
            bio = request.GET.get('bio')
            pic = request.GET.get('profile_pic')
            profile = Profile(bio=bio, profile_pic=pic, user=request.user)
            profile.save()
            return HttpResponseRedirect('/profile')
    else:
        profile_form = UpdateProfile()
    return render(request, 'profile.html', {'user': user, 'profile': profiles, 'pics': pics, 'profile_form': profile_form})


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