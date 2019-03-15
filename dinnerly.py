import requests
import json
import config
import time

# ts = current epoch time stamp
# token, user_id
# recipies id takes individual recipe id for more information
# need a user id to get user information
# /recipes/{id} - individual recipe information
# /users/{id} - information about user
# /users/{id}/orders/current - get the list of current orders
# /users/{id}/orders/past - list of all past recipes

class Dinnerly:
    
    def __init__(self):
        self.user_id = config.user_id
        self.token = config.token
        
    # returns current epoch time for making requests
    def _get_current_timestamp(self):
        ts = time.time()
        return str(int(ts))

    def _make_request(self, url_path):
        epoch_time = self._get_current_timestamp()        
        r = requests.get("https://api.dinnerly.com/%s/?ts=%s&brand=dn&country=us&token=%s&product_type=web" % 
                         (url_path, epoch_time, self.token)).json()
        return r
    
    # order type takes either current or past for parameters
    def get_recipes(self, order_type):
        url_path = "users/%s/orders/%s" % (self.user_id, order_type)
        current_recipes = self._make_request(url_path)
        print(current_recipes['data'])
        return current_recipes['data']
    
    def get_account_information(self):
        # gets information about the account
        #url_path = "users/" + self.user_id
        url_path = "users/%s" % (self.user_id)
        user_info = self._make_request(url_path)
        print(user_info)
        return user_info

    # this actually takes any id, recipes aren't tied to an account
    def get_recipe_information(self, recipe_id):
        url_path = "/recipes/%s" % (recipe_id)
        recipe_info = self._make_request(url_path)
        print(recipe_info)
        return recipe_info
