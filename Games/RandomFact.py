import requests
import time
import subprocess

url = "https://facts-by-api-ninjas.p.rapidapi.com/v1/facts"

headers = {
	"X-RapidAPI-Key": "fcc00cb570mshae985c18fb44c3ep1df6c0jsnb80a79666dcd",
	"X-RapidAPI-Host": "facts-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())

time.sleep(2)
if input("Would you like to restart. [Y,N]: ") == "Y":
    subprocess.call(["python3", "main.py"])