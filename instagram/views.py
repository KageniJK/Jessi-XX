from django.shortcuts import render


def index(request):
    return render(request, 'profile.html')


def search_results(request):
    if 'pic' in request.GET and request.GET['pic']:
        search_term = request.GET.get('pic')
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})