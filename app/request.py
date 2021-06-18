import urllib.request,json
from .models import quote
from app import app

Quote = quote.Quote

#Getting the quote base url
base_url = app.config["QUOTES_API_BASE_URL"]

def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response:
            quote_results_list = get_quotes_response
            quote_results = process_results(quote_results_list)


    return quote_results



def process_results(quote_list):
    '''
    Function  that processes the quotes result and transform them to a list of Objects

    Args:
        quote_list: A list of dictionaries that contain quote details

    Returns :
        quote_results: A list of quote objects
    '''
    quote_results = []
    for quote_item in quote_list:
        id = quote_item.get('id')
        author = quote_item.get('author')
        quote = quote_item.get('quote') 

        quote_object = Quote(id,author,quote)
        quote_results.append(quote_object)

    return quote_results