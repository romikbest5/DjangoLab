from django.shortcuts import render


def main(request):
    pattern = 'Main.html'
    context = {

    }
    return render(request, pattern, context)
