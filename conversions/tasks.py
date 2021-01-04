import requests
from starlette.exceptions import HTTPException
from starlette.applications import Starlette
from starlette.routing import Route


url = 'https://api.exchangerate-api.com/v4/latest/USD'
base_currency = 'USD'
data= requests.get(url).json()
currencies = data['rates']

        
def convert_currency(from_currency, to_currency, amount): 
    try:
        initial_amount = amount 
        if from_currency != base_currency: 
            amount = amount / currencies[from_currency] 

        # limiting the precision to 2 decimal places 
        amount = round(amount * currencies[to_currency], 2) 
        return amount
    except:
        return HTTPException(
            status_code=4040, detail="One or both of Currency codes are not found on this free plan of API"
        )

