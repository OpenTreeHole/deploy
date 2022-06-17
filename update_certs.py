
import os

import httpx


class Client:
    def __init__(self):
        token = os.environ.get('KONG_TOKEN', '')
        if not token:
            print('KONG_TOKEN not set')

        baseurl = os.environ.get('KONG_URL', 'http://localhost:8001')
        if not baseurl:
            print('KONG_URL not set')

        self.c = httpx.Client(
            headers={'Authorization': token},
            base_url=baseurl
        )

    def get_certs(self) -> list:
        print('getting all certs')
        r = self.c.get('/certificates')
        print('done')
        return r.json()['data']

    def update_cert(self, id: str, domain: str, cert: str, key: str):
        r = self.c.put(f'/certificates/{id}', json={
            'cert': cert,
            'key': key,
            'snis': [domain, f'*.{domain}']
        })
        if r.status_code > 201:
            print('update cert failed', r.json())


if __name__ == '__main__':
    os.chdir('/etc/nginx/ssl')

    client = Client()
    certs = client.get_certs()

    for cert in certs:
        domain = cert['snis'][0].replace('*.', '')
        names = [f'{domain}.crt', f'{domain}.key']
        files = []
        print('updating cert for', domain)

        try:
            for name in names:
                with open(name) as f:
                    files.append(f.read())
        except Exception as e:
            print(e)
            print('could not read cert files of', domain)
            continue

        client.update_cert(id=cert['id'], domain=domain, cert=files[0], key=files[1])
        print('updated cert for', domain)
