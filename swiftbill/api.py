import requests


import uuid
from django.utils import timezone

def unique_refnum():
    # Generate a UUID as a unique identifier
    unique_id = uuid.uuid4().int & (1 << 63) - 1  # Limit to 63 bits for a smaller number

    # Get the current timestamp and convert it to a string
    current_timestamp = str(int(timezone.now().timestamp()))

    # Combine the unique identifier and timestamp
    refnum = f"{current_timestamp}{unique_id}"

    # Ensure the length is less than 100000000 (8 digits)
    if len(refnum) >= 8:
        refnum = refnum[:8]

    return refnum


def airtime_rec():
    url = "https://sandbox.giftbills.com/api/v1/airtime"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def betting_rec():
    url = "https://sandbox.giftbills.com/api/v1/betting"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None    

def data_rec():
    url = "https://sandbox.giftbills.com/api/v1/internet"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def data_type():
    url = "https://sandbox.giftbills.com/api/v1/internet/data_types"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def ninemobile_data_plan():
    url = "https://sandbox.giftbills.com/api/v1/internet/plans/9MOBILE"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None    
    
def mtn_data_plan():
    url = "https://sandbox.giftbills.com/api/v1/internet/plans/MTN"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None       
    

def airtel_data_plan():
    url = "https://sandbox.giftbills.com/api/v1/internet/plans/AIRTEL"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None      


def glo_data_plan():
    url = "https://sandbox.giftbills.com/api/v1/internet/plans/GLO"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None      

def smile_data_plan():
    url = "https://sandbox.giftbills.com/api/v1/internet/plans/SMILE4G"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None     

def spec_data_plan():
    url = "https://sandbox.giftbills.com/api/v1/internet/plans/SPECTRANET"
    headers = {
        "Authorization": "Bearer ZPCT65XED2HM8DVH0TLHYY9KIR1KGHU",
        "MerchantId": "kossybml",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None            

def pay():
    url = "https://api.paystack.co/transaction/initialize"
    secret_key = "sk_test_9af356bd919ab4dce2839c9f40a0764ab9c5521e"
    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json",
    }
    data = {
        "email": email,
        "amount": amount,
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None 