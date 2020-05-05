import sys
import requests
import base64
import json
import logging

client_id = 'a21b56ebbb67498f9d697dacd78978c7'
client_secret = '24ce551bad914b2d859a7319f31b7307'

def main():
    headers = get_headers(client_id, client_secret)
    params = {
        "q": "BTS",
        "type": "artist"
    }

    try:
        req_with_param = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
    except:
        logging.error(req_with_param.text)
        sys.exit(1)

    req_with_param = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)

    if req_with_param.status_code !=200:
        logging.error(json.loads(r.text))
        if req_with_param.status_code == 429:
            retry_after = json.loads(req_with_param.headers)['Retry-Agter']
            time.sleep(int(retry_after)})
        ## access_token expired
        elif req_with_param.status_code == 401:
            headers = get_headers(client_id, client_secret)
            req_with_param = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
        else:
            sys.exit(1)
    # Get BTS' Albums

    req_with_param = requests.get("https://api.spotify.com/v1/artists/3Nrfpe0tUJi4K4DXYWgMUX/albums", headers=headers)

    raw = json.loads(r.text)

    total = raw['total']
    offset = raw['offset']
    limit = raw['limit']
    next = raw['next']

    albums = []
    albums.extend(raw['items'])

    ## 난 100개만 뽑아 오겠다
    while next:

        req_with_param = requests.get(raw['next'], headers=headers)
        raw = json.loads(r.text)
        next = raw['next']
        print(next)

        albums.extend(raw['items'])
        count = len(albums)

    print(len(albums))




def get_headers(client_id, client_secret):

    endpoint = "https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(client_id, client_secret).enode('utf-8')).decode('ascii')

    headers = {
            "Authorization": "Basic {}".format(encoded)
    }

    payload = {
            "grant_type": "client_credentials"
    }

    req = requests.post(endpoint, data=payload, headers=headers)
    access_token = json.loads(req.text)['access_token']
    headers = {
            "Authorization": "Bearer {}".format(access_token)
    }
return headers




if __name__=='__main__':
    main()

else:
    print('this script is being imported')
