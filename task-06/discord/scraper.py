import requests
from bs4 import BeautifulSoup

def scrape_specific_division(url, class_name1, class_name2, over1, over2, det):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        first_country = soup.find(class_=class_name1).text
        second_country = soup.find(class_=class_name2).text

        if first_country and second_country:
            
            matching = f'{first_country} VS {second_country}'
        else:
            matching = 'No matches at the moment'

    except Exception as e:
        print(f"Error while scraping: {e}")
        matching = 'An error occurred while scraping.'


    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        over_count1 = soup.find(class_=over1).text
        over_count2 = soup.find(class_=over2).text

        if over_count1 :
            prog1 = f'{first_country} - {over_count1}'
        if over_count2:
            prog2 = f'{second_country} - {over_count2}'

        else :
            prog1 = ""
            prog2 = ""

    except Exception as e:
        print(f"Error while scraping: {e}")

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        detail = soup.find(class_ = det).text

        if detail :
            ved = str(detail)

    except Exception as e:
        print(f"Error while scraping: {e}")
    
    
    
    
    print(matching)
    print(prog1)
    print(prog2)
    print(ved)



