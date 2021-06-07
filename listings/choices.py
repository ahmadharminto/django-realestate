from django.db.models import Avg, Max, Min, Sum
import listings.models as Models

def getAvailableStates(as_list_of_tuple=False):
    state_list = {
        'AL': 'Alabama',
        'AK': 'Alaska',
        'AZ': 'Arizona',
        'AR': 'Arkansas',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'DC': 'District',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'IA': 'Iowa',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'ME': 'Maine',
        'MD': 'Maryland',
        'MA': 'Massachusetts',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MS': 'Mississippi',
        'MO': 'Missouri',
        'MT': 'Montana',
        'NE': 'Nebraska',
        'NV': 'Nevada',
        'NH': 'New',
        'NJ': 'New',
        'NM': 'New',
        'NY': 'New',
        'NC': 'North',
        'ND': 'North',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode',
        'SC': 'South',
        'SD': 'South',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VT': 'Vermont',
        'VA': 'Virginia',
        'WA': 'Washington',
        'WV': 'West',
        'WI': 'Wisconsin',
        'WY': 'Wyoming',
    }
    if (as_list_of_tuple):
        return [(k, v) for k, v in state_list.items()]
        
    return state_list

def getMaxPrice():
    value = Models.Listing \
        .objects \
        .all() \
        .aggregate(Max('price'))
    return value.get('price__max')

def getMaxBedroom():
    value = Models.Listing \
        .objects \
        .all() \
        .aggregate(Max('bedrooms'))
    return value.get('bedrooms__max')