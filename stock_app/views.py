from django.shortcuts import render
import requests
import json

# Create your views here.


def home(request):
    if request.method == 'POST':
        # grabbing the name value in our search form name as = ticker
        ticker = request.POST['ticker']

        # publisher key: pk_83d15d02cdd048a1b4aeddf3841592ef
        # import requests and pip3 install requests
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_83d15d02cdd048a1b4aeddf3841592ef")

    #  Python Try Except. The try block lets you test a block of code for errors.
    #      The except block lets you handle the error.
    #  The finally block lets you execute code,
    #  regardless of the result of the try- and except blocks.

        try:
            # import json, json is already inside no need to install
            api = json.loads(api_request.content)

        except Exception as e:
            api = "Error"

        context = {'api': api}
        return render(request, 'home.html', context)

    else:
        context = {'ticker': "Enter Symbol"}
        return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')
