from django.shortcuts import render
from .models import College,Branch
from django.http import JsonResponse
# Create your views here.
def index(request):
    college = College.objects.all()

    return render(request, "notify/main.html", {'college': college})



def get_cols_data(request):
    qs_value = list(College.objects.values())
    return JsonResponse({"data": qs_value})


def get_json_model_data(request,branch): 
    obj_models = list(Branch.objects.filter(college__name = branch).values())
    return JsonResponse({"data": obj_models})
