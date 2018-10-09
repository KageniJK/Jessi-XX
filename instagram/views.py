from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
from .forms import UpdateProfile, PostImageForm
from django.http import HttpResponseRedirect


@login_required(login_url='/accounts/login/')
def index(request):
    pics = Image.get_all()
    return render(request, 'timeline.html', {'pics': pics})


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    profiles = Profile.get_user(user.id)
    if profiles:
        profile = profiles[len(profiles)-1]
    else:
        profile = profiles
    pics = Image.get_by_user(user.id)
    if request.method == 'POST':
        profile_form = UpdateProfile(request.POST, request.FILES)
        upload_form = PostImageForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save_profile()
            return HttpResponseRedirect('/profile')
        if upload_form.is_valid():
            image = upload_form.save(commit=False)
            image.user = user
            image.save_image()
    else:
        profile_form = UpdateProfile()
        upload_form =PostImageForm()
    return render(request, 'profile.html', {'user': user, 'profile': profile, 'pics': pics, 'profile_form': profile_form,
                                            'upload_form': upload_form})


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