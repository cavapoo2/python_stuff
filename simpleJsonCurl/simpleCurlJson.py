#note is used pipenv requests, then started up ipython. then did this. compare this to the c++
#version :)
import requests
r = requests.get('https://challenges.hackajob.co/swapi/api/people/?search=Luke%20Skywalker')
j = r.json()
