import requests
from requests.exceptions import ConnectionError

def get_bnb_price(address):

    # url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&tag=latest"

    # for _ in range(retries):
    try:
        url = f"https://api.bscscan.com/api?module=account&action=balance&address={address}&tag=latest"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        balance_in_wei = int(data['result'])
        bnb_price_in_wei = 10 ** 18  # 1 BNB in Wei
        balance_in_bnb = balance_in_wei / bnb_price_in_wei
        return balance_in_bnb
    except ConnectionError as e:
        print(f"Connection error: {e}")
        
        # Introduce a delay before retrying
        
    
    # raise ConnectionError("Max retries exceeded")

# # Example usage without API key
# address = "0x225B6aee43dD59462Aef006e1CF5dcDfF62cD32c"
# try:
#     bnb_price = get_bnb_price(address)
#     print(f"Berilgan manzilda BNB narxi: {bnb_price}")
# except ConnectionError as ce:
#     print(f"Failed to get BNB price: {ce}")
