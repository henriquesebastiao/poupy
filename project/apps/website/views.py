from django.shortcuts import render


def home(request):
    return render(
        request,
        'pages/website/home.html',
        context={
            'logo_name_url': 'home',
        }
    )
