from typing import Any
import requests
import urllib.parse
import haversine as hs

def input(address1,address2,weight,unit,by):
    weight=float(weight)
    UNITS = {
        "KG": 1,
        "POUNDS": 2.20462,
        "OUNCE":35.274,
        "TONNE":0.001,
        "GRAM":1000,
        "IMPERIALTON":0.000984207,
        "USTON":0.0011023118399,
        "STONE":0.15747311999999660803
    }
    for name,value in UNITS.items():
        if name==unit:
            to_kg=value

    url1 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address1) +'?format=json'
    url2 = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address2) +'?format=json'

    response1 = requests.get(url1).json()
    response2 = requests.get(url2).json()
    if response1 == [] :
        print("From location not found")
    elif response2 == [] :
        print("To location not found")
    else:
        lat1=float(response1[0]["lat"])
        long1=float(response1[0]["lon"])
        lat2=float(response2[0]["lat"])
        long2=float(response2[0]["lon"])
        loc1=(lat1,long1)
        loc2=(lat2,long2)
        # import pdb;pdb.set_trace()
        dist=hs.haversine(loc1,loc2)
        return price_calculator(dist,to_kg,weight,by)
   
def price_calculator(dist,to_kg,weight,by):
    if dist < 100:
        price=0.03
    elif dist < 1000:
        if by=="road":
            price=0.01
        elif by=="water":
            price=0.005
        else:
            price=0.0052
    else:
        if by=="air":
            price=0.009
        else:
            price=0.005
    time=time_calculator(by,dist)
    total_amount=dist*(weight/to_kg)*price
    data=f"Price: ${total_amount} \nTransported by: {by} \nEstimated time: {time} days"
    return data
    # print(f"${total_amount} transported by: {by} estimated time: {time} days")

def time_calculator(by,dist):
    if by == "road":
        time=int(dist*0.03)
    elif by == "water":
        time=int(dist*0.02)
    else:
        time=int(dist*0.001)
    if time == 0:
        time=1
    return time
  

# if __name__ == '__main__':
#     price_calculator()