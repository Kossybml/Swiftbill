import uuid
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from . models import Api_config,wallet
from .api import airtel_data_plan, airtime_rec, betting_rec, data_rec, data_type, glo_data_plan, mtn_data_plan, ninemobile_data_plan, pay, smile_data_plan, spec_data_plan, unique_refnum
import requests
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
api = Api_config.objects.get()
psk = api.PAYSTACK_SECRET_KEY 
ppk = api.PAYSTACK_PUBLIC_KEY
gapi = api.GIFTBILL_API_KEY
# refnum = unique_refnum()

def home(request):
    return render (request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "username already exist")
        else:
            if password2 == password1 :
                myuser = User.objects.create_user(username, email, password1, )
                Wallet = wallet.objects.create(user=myuser, balance=0.00)
                Wallet.save()
                messages.success(request, "Your account has been created successfully,")

            else:        
                messages.error(request, "password did not match ")

        # messages.success(request, "Your account has been created successfully,")
        # return redirect("signin")

    return render (request, "signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user )
            return redirect ("user")
        else:
            messages.error(request, "Wrong credential, don't have an account?") 
    return render (request, "signin.html")

def signout(request):
    logout(request)
    return redirect("home")

@login_required
def user(request):
    return render (request, "user.html")

@login_required
@csrf_exempt
def topup(request):
    if request.method == 'POST':
        # Handle the payment data here (e.g., create a payment record, process payment)
        email = request.POST.get('email')
        amount = request.POST.get('amount')

    # Render the payment form template
    return render(request, 'top3.html', {'your_public_key': 'pk_test_3cf9b7d117829302623eb00e1aab89b6f21fe7d2'}) 



# def topup(request):
#     url = "https://api.paystack.co/transaction/initialize"
#     if request.method == 'POST':
#         email = request.POST["email"]
#         amount = request.POST["amount"]
#         secret_key = psk
#         headers = {
#             "Authorization": f"Bearer {secret_key}",
#             "Content-Type": "application/json",
#         }
#         data = {
#             "email": email,
#             "amount": float(amount)*100,
#         }
#         response = requests.post(url, headers=headers, json=data)
#         if response.status_code == 200:
#             data = response.json()
#             red_url = data['data']['authorization_url']
#             return redirect (red_url)

#     context = {  
#     "user": request.user,
#     }
#     return render(request, "top4.html", context)


@login_required
def callback(request):
    if request.method == "POST":
        # Get the user and amount from the POST data
        user = request.user
        amount = request.POST.get("amount")

        # Save the payment information to the database
        payment = wallet(user=user, amount=amount)
        print(user)
        payment.save()

        # You can also perform any additional processing here if needed.

        # Redirect to a success page or any other page as needed
        return render (request, "user.html")

    # Handle GET requests or invalid requests
    return render (request, "callback.html")


@login_required
def betting(request):
    if request.method == "POST":
        user_bal = request.POST["user_bal"]
        amount = request.POST["amount"]
        provider= request.POST["provider"]
        cusid = request.POST["cusid"]

        print(user_bal)
        print(amount)
        print(provider)
        print(cusid)

        if amount > user_bal:
            messages.error(request, "Insufficient balance")
            return redirect("betting")
        else:
            url = 'https://sandbox.giftbills.com/api/v1/betting/topup' 
            api_key = gapi
            headers = {
                "Authorization": f"Bearer {api_key}",
                "MerchantId": "kossybml",
                'Content-Type': 'application/json',
                'Encryption': 'Signature_VDGOUHWSWW5A1695900503',
            }
            payload = {
                "amount": float(amount),
                "customerId": request.POST["cusid"],
                "provider": request.POST["provider"],                
                "reference": "swiftbill",
            }
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg = data['message']
                messages.success(request, msg)
                new_bal= float(user_bal) - float(amount)
                acct = wallet.objects.get(user=request.user)
                acct.balance = new_bal
                acct.save()
            else:
                messages.error(request, "Invalid response")
        

    bet = betting_rec()
    context={
        "bet": bet['data']
    }
    return render (request, "betting.html",context)

@login_required
def tv(request):
    return render (request, "tv.html")

@login_required
def internet(request):
    if request.method == "POST":        
        provider = request.POST["provider"]
        number = request.POST["number"]
        id = request.POST["id"]
        print(provider)
        print(number)
        print(id)
        refnum = str(uuid.uuid4())
        url = 'https://sandbox.giftbills.com/api/v1/internet/data' 
        api_key = gapi
        headers = {
            "Authorization": f"Bearer {api_key}",
            "MerchantId": "kossybml",
            'Content-Type': 'application/json',
        }
        data = {
            "provider": provider,
            "number": number,
            "plan_id": id,
            "reference": refnum
        }

        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            data = response.json()
            msg = data['message']
            messages.success(request, msg)
            
        else:
            messages.error(request, "Invalid responsee")

    data = data_rec()
    data_t = data_type()
    nmobile = ninemobile_data_plan()
    mtn = mtn_data_plan()
    airtel = airtel_data_plan()
    glo = glo_data_plan()
    spec = spec_data_plan()
    smile = smile_data_plan()

    context={
        "data": data['data'],
        "data_t": data_t['data'],
        "nmobile": nmobile['data'],
        "mtn": mtn['data'],
        "airtel": airtel['data'],
        "glo": glo['data'],
        "spec": spec['data'],
        "smile": smile['data'],
    }
    return render (request, "data.html", context)

@login_required
def airtime(request):
    if request.method == "POST":
        user_bal = request.POST["user_bal"]
        amount = request.POST["amount"]
        print(user_bal)
        print(amount)
        if amount > user_bal:
            messages.error(request, "Insufficient balance")
            return render("airtime")
        else:
            url = 'https://sandbox.giftbills.com/api/v1/airtime/topup' 
            api_key = gapi
            headers = {
                "Authorization": f"Bearer {api_key}",
                "MerchantId": "kossybml",
                'Content-Type': 'application/json',
            }
            payload = {
                "provider": request.POST["provider"],
                "number": request.POST["number"],
                "amount": float(amount),
                "reference": "swiftbill",
            }
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg = data['message']
                messages.success(request, msg)
                new_bal= float(user_bal) - float(amount)
                acct = wallet.objects.get(user=request.user)
                acct.balance = new_bal
                acct.save()
                return redirect("airtime")
            else:
                messages.error(request, "Invalid response")
        

    air = airtime_rec()
    context={
        "air": air['data']
    }
    return render (request, "airtime.html",context)

def airtimeselect(request):
    air = airtime_rec()
    context={
        "air": air['data']
    }
    return render (request, "airtimeselect.html",context)    


@login_required
def elec(request):
    return render (request, "elec.html")    

