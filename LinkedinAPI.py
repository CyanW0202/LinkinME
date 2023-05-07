
# This is a sample Python script.
# 5/6/23: parse the json() dictionary to extract data.

import http.server
import socketserver



# This is a sample Python script.
# translated from this Taiwanese tutorial : https://ithelp.ithome.com.tw/m/articles/10311618
# addtional scripts of Linked in API added @ 4/30/23
# tutorial from https://nubela.co/blog/ultimate-guide-to-linkedin-api_people-profile-api_with-python-examples/
# and https://www.jcchouinard.com/authenticate-to-linkedin-api-using-oauth2/

# This is a sample Python script.


def open_url(url):
    '''
    Function to Open URL.
    Used to open the authorization link
    '''
    import webbrowser
    print(url)
    webbrowser.open(url)


def parse_redirect_uri(redirect_response):
    '''
    Parse redirect response into components.
    Extract the authorized token from the redirect uri.
    '''
    from urllib.parse import urlparse, parse_qs

    url = urlparse(redirect_response)
    url = parse_qs(url.query)
    return url['code'][0]

def authorize():
    '''
        generate an authorization URL to send your user to LinkedIn
        permit your application to download their profile.
        Once authorized, it'll redirect to the redirect URI given.
    '''
    authURL = 'https://www.linkedin.com/oauth/v2/authorization'
    tokenURL = 'https://www.linkedin.com/oauth/v2/accessToken'
    params = {
        'response_type': 'code',
        'client_id': LkID,
        'redirect_uri': reD_URI,
        'state': secrets.token_hex(8).upper(),
        'scope': 'r_liteprofile,r_emailaddress'
    }
    response = requests.Request('GET', authURL, params=params).prepare().url
    #response the auth url that generated.
    open_url(response)
    redirect_response = input('Paste the full redirect URL here:')
    auth_code = parse_redirect_uri(redirect_response)

    #authorization code
    data = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': reD_URI,
        'client_id': LkID,
        'client_secret': LkSecret,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    access_token2 = requests.post(tokenURL, params=data, headers=headers).json()['access_token']
    print("ACCESS_CODE"+auth_code)

    #Test if the token works
    LI_PROFILE_API_ENDPOINT = 'https://api.linkedin.com/v2/me'
    r = requests.get(LI_PROFILE_API_ENDPOINT, headers={'Authorization': 'Bearer ' +access_token2})
    print(r.json())
    access_token1 = access_token2

def getLinkedInInfo():
    import json
    LI_PROFILE_API_ENDPOINT = 'https://api.linkedin.com/v2/me'
    r = requests.get(LI_PROFILE_API_ENDPOINT, headers={'Authorization': 'Bearer ' + access_token1})
    t = r.json()
    print(t.get('status'))
    #first_name = t['firstName'][0]['localized'][0]['en_US']
    #print(first_name)
    #return first_name



#Linkedin Credentials:
LkID = "86ilsuvjkuw54h"
LkSecret = "5MeLwkO9elLbOuOV"
reD_URI = "http://localhost:8888"
LKtoken = ""
access_token1 = "AQUxdTA9sZ7HjZ3xRUt6s6bANAOTBqonzZRxeLHUFzV8BxZGTogq3pjYus68yM_MCZZVgH4lIqUF6amO5Gz7--8v3EZhd4uvqgu7YkORNJYB1L-pDBLpAEtyk_YPoSPIjziP-WR3eKxIQWdToQuytxjHDQ-R4q8sgg7tK3UBfuoEkuXVCDLvEwPLt_c9yJRSjNcWKHNh2g6gcjpEynyGJu8uAexjUK90_1RtNU0-QeEdkjvYjABCL1JoLpA_UjJpVUdJP9oR_k-uXNdvfcJZiWEv-TOj28kpFfNDYqKY_uXnplpf8dBX6SC6Evf48wWELOjou-hfzo7zAQICM0goxywA8faGBQ"

# %%
# lib that we would use:
import os
import openai
import requests
import json
import secrets
import string

# openAI stuffs:
openai.api_key = "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"
url = 'https://api.openai.com/v1/chat/completions'
chat = True
prompt = ""
print("your linked in profile url:\n")
promptt = {"summaries this person's experiences in engineering? please list them as bullet points.", \
           "What characteristics or experience in the profile support this analysis respectively? list them in bullet points."}

# main
authorize()
getLinkedInInfo()

while chat:
    # test the LinkedIn API

    '''
    for x in promptt:
        prompt += x + input(":")+'\n'
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
            # "n": 10,
            # "temperature: 0.7
        }

        headers = {
            "Authorization": f"Bearer {openai.api_key}",
            "Content-Type": "application/json"
        }

        r = requests.post(url, data=json.dumps(payload), headers=headers)
        try:
            # analyze the response: from r.content, extract the json content
            res = analyze_res(r.content)

            prompt += res + '\n'

            print(res)
        except:
            print("ERROR:", r.content)
    '''
    chat = False
