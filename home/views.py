from django.shortcuts import render, HttpResponse
import joblib

model = joblib.load('static/random_forest_regressor')

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

def prediction(request):
    if request.method == "POST":
        age = int(request.POST.get('age'))
        sex = int(request.POST.get('sex'))
        bmi = int(request.POST.get('bmi'))
        children = int(request.POST.get('children'))
        smoker = int(request.POST.get('smoker'))
        region = int(request.POST.get('region'))

        pred = round(model.predict([[age, sex, bmi, children, smoker, region]])[0])
        output = {
            "output": pred
        }

        return render(request, 'prediction.html', output)
    else:
        return render(request, 'prediction.html')


