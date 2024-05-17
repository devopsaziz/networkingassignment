import requests
import time
from tabulate import tabulate

# List of subdomains to check
subdomains = ['awesomeweb', 'www.google.com']

def check_status(subdomains):
    results = []
    for subdomain in subdomains:
        try:
            response = requests.get(f"http://{subdomain}")
            if response.status_code == 200:
                status = "UP"
            else:
                status = "DOWN"
        except requests.ConnectionError:
            status = "DOWN"
        results.append([subdomain, status])
    return results

def display_results(results):
    headers = ["Subdomain", "Status"]
    print(tabulate(results, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    while True:
        results = check_status(subdomains)
        display_results(results)
        time.sleep(60)  # Check status every minute
