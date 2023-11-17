from django.shortcuts import render


def app(request):
    return render(
        request,
        'pages/app/home.html',
        context={
            'logo_name_url': 'app',
        }
    )
