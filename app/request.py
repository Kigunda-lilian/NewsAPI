import urllib.request,json
from .model import News

#getting API key
api_key=None

#getting the news base url
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config ['API_BASE_URL']   
    
def fetch_news():
    
    fetch_news_url=base_url.format(api_key)
    
    with urllib.request.urlopen(fetch_news_url) as url:
        our_news_data =url.read()
        our_news_response =json.loads(our_news_data)_
        
        our_results=None
        
        if our_news_response['articles']:
            our_results_list =our_news_response['articles']
            #print (our_results_list)
            our_results = process_news_results(our_results_list)
            
            
            
    return our_results
def process_news_results(results_list):
    
    our_results =[]
    for results_item in results_list:
        title= results_item.get('title')
        description= results_item.get('description')
        urlToImage= results_item.get('urlToImage')
        content= results_item.get('content')
        publishedAt = results_item('publishedAt')
        
        
        results_object = News(title,description,urlToImage,content,publishedAt) 
        our_results.append(results_object)    


    return our_results


