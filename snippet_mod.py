#!/usr/bin/env /usr/local/bin/python3

import requests
import os 
import json

def login():
#    key = 'q2Jl1xH35JCXw0l8EiaGzsQOFiOsEIrYiAcb1dvMs_wwYH0vtge2lucfk9XqFf19'
# using token vmc_all_token    
 #   key = 'gEn7MVKluzNs8ictSP8cxBWr5_h6FPKVHFNEECilFgc4_kdCVWwmhU2OP8_xCasF'
# using token vmc_admin_token - note this is invalid because I don't have admin role in org
    key = 'vkG1evIub8paZdLYw3jx5_J2eASvOF4T4l0cK6TgfevxZsxrVDM_eaU3KpCHcOKi'
# using token vmc_admin_res
#    key = 'TXmZOB8mlAQ3Ymo08HrelhiPyTbmmygnYUenjNDFTXbmfmH5uyV2IPSqrU1lTWjg'
# using token vmc_nsxAdmin
#    key = 'u2Rdr_w3uBnpm7zyQIsbmjURPBI5bLRcBrrgewtp9XoqZFQ_E-gHE1KZujOl9IJ4'
# using the nsxaudit_token
    baseurl = 'https://console.cloud.vmware.com/csp/gateway'
    uri = '/am/api/auth/api-tokens/authorize'
    headers = {'Content-Type':'application/json'}
    payload = {'refresh_token': key}
    r = requests.post(f'{baseurl}{uri}', headers = headers, params = payload)
    if r.status_code != 200:
        print(f'Unsuccessful Login Attmept. Error code {r.status_code}')
    else:
        print('Login successful. ')
        auth_json = r.json()['access_token']
        auth_Header = {'Content-Type':'application/json','csp-auth-token':auth_json}
        return auth_Header
      
auth_header = login()
orgList = requests.get('https://vmc.vmware.com/vmc/api/orgs', headers = auth_header)
#orgList is a datatype List
#olf = open("orglistfile.txt", "a")
#pyorgList = json.loads(orgList.json())
#olf.write(pyorgList)
#for olist in orgList:
#	olf.write(olist)
#olf.write(orgList.json())
#print(orgList.json())
#olf.close()
#orgID = orgList.json()[0]['id']
orgID = '84e84f83-bb0e-4e12-9fe0-aaf3a4efcd87'
print("Get info for Org: " + orgID)
#sddclist = requests.get('https://vmc.vmware.com/vmc/api/orgs/{orgID}/sddcs', headers = auth_header)
#print(sddclist)
#¢orgdump = requests.get('https://vmc.vmware.com/vmc/api/orgs{orgID}', headers = auth_header)
#orgdump = requests.get(f'https://console.cloud.vmware.com/csp/gateway/am/api/orgs{orgID}', headers = auth_header)
#print(orgdump)
sddcList = requests.get(f'https://vmc.vmware.com/vmc/api/orgs/{orgID}/sddcs', headers = auth_header)
if sddcList.status_code != 200:
    print('API Error')
else:
    for sddc in sddcList.json():
        print("SDDC Name: " + sddc['name'])
        print("SDDC Create Date: " + sddc['created'])
        print("SDDC Provider: " + sddc['provider'])
        print("SDDC Region: " + sddc['resource_config']['region'])
        print()