from django.shortcuts import render

# Create your views here.
def matvey_page(request):
    return render(request, 'matvey.html')