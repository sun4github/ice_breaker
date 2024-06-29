import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_ul : str, mock: bool = False) :
    """scrape information from LinkedIn profiles,
    Manually  scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/sun4github/e8ab82bd3e89e9f78dfb3110ef0f5976/raw/85a405681807a7a30fedd7e37bcc8795516f1b1b/suneelkanuri-linkedin-json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_key = os.environ['PROXYCURL_API_KEY']
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'linkedin_profile_url': linkedin_profile_ul
        }
        response = requests.get(api_endpoint,
                                params=params,
                                headers=headers,
                                timeout=10)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([],"", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")


    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            "https://www.linkedin.com/in/suneel-kanuri-2253667970/",
            True
        )
    )
