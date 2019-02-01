#http://open-notify.org/Open-Notify-API/ISS-Location-Now/

#http://docs.python-requests.org/en/master/
import requests

r = requests.get("http://api.open-notify.org/iss-now.json")

print(r.status_code, r.text, r.json())

my_data = r.json()

print(my_data['iss_position']['latitude'], ", ", my_data['iss_position']['longitude'])






