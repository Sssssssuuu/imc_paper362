import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_request(combo, base_url, headers):
    url = base_url.replace('*', combo)
    retries = 3
    for _ in range(retries):
        try:
            response = requests.get(url=url, headers=headers, timeout=20)
            if response.status_code == 200:
                time.sleep(random.randint(1, 5))
                return response.content
            else:
                print(response.text)
                print(f"Request for {combo} failed with status code {response.status_code}")
                time.sleep(random.randint(1, 5))
        except Exception as e:
            print(f"Request for {combo} failed with exception: {e}")
            time.sleep(random.randint(1, 5))
    return None

def write_to_file(data_list, output_file):
    with open(output_file, 'ab') as out_file:
        for data in data_list:
            out_file.write(data)
            out_file.write(b'\n')

def batch_process(file_path, base_url, headers, output_file):
    with open(file_path, 'r') as file:
        combinations = file.read().splitlines()

    results = []
    count = 0
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_combo = {executor.submit(send_request, combo, base_url, headers): combo for combo in combinations}
        for future in as_completed(future_to_combo):
            combo = future_to_combo[future]
            data = future.result()
            if data:
                results.append(data)
                print(f"Response content for {combo} saved")
                count += 1

                if count >= 500:
                    write_to_file(results, output_file)
                    results.clear()
                    count = 0

    if results:
        write_to_file(results, output_file)


web = 'https://chat.openai.com/backend-api/gizmos/search?q=*'
headers = {
    'Accept':'',
    'Accept-Encoding':'',
    'Accept-Language':'',
    'Authorization': '',
    'Cookie': '',
    'Cache-Control':'',
    'Pragma':'',
    'Referer':'',
    'Sec-Ch-Ua':'',
    'Sec-Ch-Ua-Mobile':'',
    'Sec-Ch-Ua-Platform':'',
    'Sec-Fetch-Dest':'',
    'Sec-Fetch-Mode':'',
    'Sec-Fetch-Site':'',
    'User-Agent': ''
}

file_path = ''
output_file = ''

batch_process(file_path, web, headers, output_file)
