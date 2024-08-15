import requests

websites = [
    "https://www.google.com",
    "https://www.abcd.com",
    "https://www.facebook.com",
    "https://www.yourwebhilhiit4958985hfffjlfjjjf,gn,,nsite.com"
]


def check_websites(website_list):
    results = {}
    for website in website_list:
        try:
            response = requests.get(website, timeout=5)
            if response.status_code == 200:
                results[website] = "UP"
            else:
                results[website] = "DOWN"
        except requests.exceptions.RequestException:
            results[website] = "DOWN"
    return results


def display_results(results):
    print(f"{'Website':<30} {'Status':<10}")
    print("-" * 40)
    for website, status in results.items():
        print(f"{website:<30} {status:<10}")

if __name__ == "__main__":
    website_statuses = check_websites(websites)
    display_results(website_statuses)
