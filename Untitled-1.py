import requests

def scan_file_with_virustotal(api_key, file_path):
    url = 'https://www.virustotal.com/vtapi/v2/file/scan'
    params = {'apikey': api_key}

    try:
        with open(file_path, 'rb') as file:
            files = {'file': (file.name, file)}
            response = requests.post(url, files=files, params=params)
            if response.status_code == 200:
                json_response = response.json()
                if json_response['response_code'] == 1:
                    scan_id = json_response['scan_id']
                    return scan_id
                else:
                    print(f"Scan failed: {json_response['verbose_msg']}")
            else:
                print(f"Failed to submit file: {response.status_code}")
    except IOError as e:
        print(f"Error reading file: {e}")

# Example usage:
if __name__ == "__main__":
    api_key = '4e8ac0838777839bc2d0eaf932de2da0fab7db7c77b6a14da4b93b3c40b0104e'
    file_path = input("Enter the full path to the file you want to scan: ").strip()
    scan_id = scan_file_with_virustotal(api_key, file_path)
    if scan_id:
        print(f"Scan initiated successfully. there are no virus. Scan ID: {scan_id}")