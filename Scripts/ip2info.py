import ipinfo
import time
import pprint

access_token = '54f5760d00cee4'
handler = ipinfo.getHandler(access_token) 

ip_address = input("[+] ENTER TARGET IP ADRESS: ")
time.sleep(0.5)


details = handler.getDetails(ip_address)

print("[+]IP DETAILS...")

print("[+]CITY")
print(details.city)

print("[+]COORDINATES")
print(details.loc)
print(f' Latitude: {details.latitude} ')
print(f' Longitude: {details.longitude} ')

print("[+]HOST")
print(f'https://{details.hostname}')

print("[+]COUNTRY INFO")
print(details.country)
print(details.country_name)

print("[+] POSTAL")
print(f' Postal Code: {details.postal} ')

print("[+] Timezone")
print(details.timezone)

print("[+] ORGINIZATION")
print(details.org)

# USING pprint.pprint(details.all) RETURNS THE JSON DATA OF ALL INFO