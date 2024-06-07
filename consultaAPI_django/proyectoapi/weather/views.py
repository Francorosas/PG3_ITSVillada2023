from django.shortcuts import render
import requests
from django.conf import settings

def consultar_clima(request):
    query = request.GET.get('q', '')

    datos_clima = []

    if query:
        url = f"http://api.weatherapi.com/v1/current.json?key={settings.WEATHER_API_KEY}&q={query}"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            clima_ciudad = {
                'ciudad': datos['location']['name'],
                'país': datos['location']['country'],
                'temperatura': datos['current']['temp_c'],
                'condición': datos['current']['condition']['text'],
                'humedad': datos['current']['humidity'],
                'viento_kph': datos['current']['wind_kph']
            }
            datos_clima.append(clima_ciudad)

    return render(request, 'weather/consultar_clima.html', {'datos_clima': datos_clima, 'query': query})