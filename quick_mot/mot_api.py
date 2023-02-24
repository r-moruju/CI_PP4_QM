"""
Get DVLA API cars information
"""

import os
import requests
if os.path.isfile('env.py'):
    import env

MOT_API_KEY = os.environ.get("MOT_API_KEY")


def get_car_data(reg_nr):

    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

    payload = "{\n\t\"registrationNumber\":" + " \"{}\"".format(reg_nr) + "\n}"
    headers = {
        'x-api-key': MOT_API_KEY,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    car_data = response.json()
    return car_data
