import requests

API_BASE_URL = "https://linkedin-bulk-data-scraper.p.rapidapi.com/companies"
API_HEADERS = {
	"x-rapidapi-key": "fce4ae0021msha91deb7666572fcp1fecbejsn26c2945feb38",
	"x-rapidapi-host": "linkedin-bulk-data-scraper.p.rapidapi.com",
	"Content-Type": "application/json",
	"x-rapidapi-user": "usama"
}

def enrich_data(linkedin_urls):
    payload = {
        "links": linkedin_urls
    }
    print("enrich data")
    response = requests.post(API_BASE_URL, json=payload, headers=API_HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print("error")
        return None
