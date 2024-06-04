









# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from .forms import SignatureForm
# from .models import model
# import numpy as np
# from PIL import Image
# import cv2

# def preprocess_image(image):
#     image = cv2.resize(image, (70, 70))
#     image = image / 255.0
#     image = np.expand_dims(image, axis=0)
#     return image

# def detect_signature(request):
#     if request.method == 'POST':
#         form = SignatureForm(request.POST, request.FILES)
#         if form.is_valid():
#             signature = form.cleaned_data['signature']
#             image = Image.open(signature)
#             image = np.array(image)

#             preprocessed_image = preprocess_image(image)
#             prediction = model.predict(preprocessed_image)
#             predicted_class = np.argmax(prediction, axis=1)[0]
#             prediction_result = "Fake Signature" if predicted_class == 1 else "Real Signature"
            
#             return JsonResponse({'prediction': prediction_result})
#         else:
#             return JsonResponse({'error': 'Invalid form data'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid request method'}, status=405)

# def home(request):
#     return render(request, 'index.html')

# def contactus(request):
#     return render(request, 'Contact.html')

# def about(request):
#     return render(request, 'About.html')

# def services(request):
#     return render(request, 'Services.html', {'form': SignatureForm()})

# def resources(request):
#     return render(request, 'Resources.html')

# def signup(request):
#     return render(request, 'Sign_Up.html')

# def login(request):
#     return render(request, 'Sign_in.html')















from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import SignatureForm
from .models import model
import numpy as np
from PIL import Image
import cv2

def preprocess_image(image):
    image = cv2.resize(image, (70, 70))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def detect_signature(request):
    if request.method == 'POST':
        form = SignatureForm(request.POST, request.FILES)
        if form.is_valid():
            signature = form.cleaned_data['signature']
            image = Image.open(signature)
            image = np.array(image)

            preprocessed_image = preprocess_image(image)
            prediction = model.predict(preprocessed_image)
            predicted_class = np.argmax(prediction, axis=1)[0]
            prediction_result = "Fake Signature" if predicted_class == 1 else "Real Signature"
            
            return JsonResponse({'prediction': prediction_result})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def home(request):
    return render(request, 'index.html')

def contactus(request):
    return render(request, 'Contact.html')

def about(request):
    return render(request, 'About.html')

def services(request):
    return render(request, 'Services.html', {'form': SignatureForm()})

def resources(request):
    return render(request, 'Resources.html')

def signup(request):
    return render(request, 'Sign_Up.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email == 'hello@gmail.com' and password == '1234':
            return redirect('mainPage')  # Redirect to 'home' which renders 'index.html'
        if email == 'test@gmail.com' and password == 'tester1':
            return redirect('mainPage')  # Redirect to 'home' which renders 'index.html'
        else:
            error_message = 'Invalid username or password'
            return render(request, 'Sign_in.html', {'error_message': error_message})
    
    return render(request, 'Sign_in.html')
