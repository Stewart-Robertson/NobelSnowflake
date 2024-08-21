import requests
import pandas as pd
from pprint import pprint

'''In future, have a python file written
to handle response codes that can be imported
into each API project'''

def fetch_laureates():
    response = requests.get('https://api.nobelprize.org/2.1/laureates')
    data = response.json()
    '''Initial exploration of data:
    pprint(data)
    pprint(data['laureates'])
    df = pd.DataFrame(data['laureates'])
    df.to_excel('testDF.xlsx')'''
    
    # Initialise a list that will contain selected laureate data to be exported as a DataFrame
    Laureates = []

    # Select out chosen data from the data dictionary and append to Laureates list
    for laureate in data['laureates']:
        name = laureate['fullName']['en']

        if 'birth' in laureate and 'place' in laureate['birth'] and 'country' in laureate['birth']['place']:
            birth_country = laureate['birth']['place']['country']['en']
        else:
            birth_country = "Unknown"

        if 'affiliations' in laureate['nobelPrizes'][0]:
            for np in laureate['nobelPrizes']:
                affiliation = (np['affiliations'][0]['name']['en'])
        else:
            affiliation = "No affiliation"

        year_won = laureate['nobelPrizes'][0]['awardYear']
        category = laureate['nobelPrizes'][0]['category']['en']
        win_reason = laureate['nobelPrizes'][0]['motivation']['en']

        Laureates.append(
            [name, 
            birth_country, 
            affiliation, 
            year_won, 
            category, 
            win_reason]
        )

    #print(Laureates)

    # Create a DataFrame from the chosen data and export to Excel
    summary_df = pd.DataFrame(
        data=Laureates, 
        columns=['RECIPIENT_NAME',
                'BIRTH_COUNTRY',
                'AFFILIATED_INSTITUTE',
                'YEAR_PRIZE_AWARDED',
                'PRIZE_CATEGORY',
                'MOTIVATION']
    )
    return summary_df

if __name__ == "__main__":
    summary_df = fetch_laureates()
    summary_df.to_excel('summaryDF.xlsx', index=False)