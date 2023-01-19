import requests, json

def get_weather():
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"

    querystring = {"lat":"57.09","lon":"65.32","units":"metric","lang":"ru"}

    headers = {
        "X-RapidAPI-Key": "6aa5d2c802msh187abc8c6ebfd21p13a5b7jsn66bc3f062e19",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    resp = response.json()
    temp = resp['data'][0]['temp']
    discription = resp['data'][0]['weather']['description']
    return [temp, discription]