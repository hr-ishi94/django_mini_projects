from django.shortcuts import render, HttpResponse
from django.contrib import messages
import requests
import datetime

# Create your views here.

def index(request):
    try:
        city_name = request.POST.get('city_name')
        
        if not city_name:
            city_name = 'Bengaluru'

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=10c9fc6bb16a962ca2abe1e9cf9549b1'
        PARAMS = {'units':'metric'}

        data = requests.get(url, PARAMS).json()
        
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        date = datetime.date.today()

        exception_occured = False
        # search Engine api key
        API_KEY = "AIzaSyCbfTja-QULgHaXWrIDXczbqeUEXYo9E-I"
        SEARCH_ENGINE_ID = "32c6dc1d3ae704d92"

        query = city_name + " 1920x1080"
        page = 1
        start = (page-1) * 10 + 1
        searchType = "image"

        city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"
        # city_url = f"customsearch.googleapis.com?key=AIzaSyCbfTja-QULgHaXWrIDXczbqeUEXYo9E-I&cx=32c6dc1d3ae704d92&q=bengaluru1920x1080&start=1&searchType=image&imgSize=xlarge"

        data = requests.get(city_url).json()
        count = 1
        search_items = data.get('items')
        print(city_url)
        image_url = search_items[0]['link']
        return render(request, 'index.html',{'temp':temp, 'description' :description , 'icon':icon ,'date': date,'city_name':city_name,'exception':exception_occured,'image_url':image_url})
        
    except:
        exception_occured = True
        messages.error(request,"City is not available")
        return render(request, 'index.html',{'exception':exception_occured})
