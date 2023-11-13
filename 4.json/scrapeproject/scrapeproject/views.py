from django.shortcuts import render
import json

def index(request):
    # Baca data dari file JSON
    with open('../scrape/city_data.json', 'r') as json_file:
        data = json.load(json_file)

    return render(request, 'index.html', {'data': data})
