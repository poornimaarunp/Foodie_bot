from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import sys

class ActionSearchRestaurants(Action):
	response = ""
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain, maxcount=5):
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		minbudget = tracker.get_slot('minbudget')
		maxbudget = tracker.get_slot('maxbudget')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		search = True
		count=0
		start=0
		response=""
		while search:
			results=zomato.restaurant_search_paginated("", lat, lon, str(cuisines_dict.get(cuisine.lower())), start, 20)
			d = json.loads(results)
			if d['results_found'] == 0:
				response= "no results"
			else:
				for restaurant in d['restaurants']:
					try:
						price = restaurant['restaurant']['average_cost_for_two']
						rating = restaurant['restaurant']['user_rating']['aggregate_rating']
						if minbudget is not None and maxbudget is not None and price <= int(maxbudget) and price >= int(minbudget):
							response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with budget Rs."+str(price)+" and "+str(rating)+" rating \n"
							#dispatcher.utter_message("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with budget Rs."+str(price)+"\n")
							count = count + 1
						elif minbudget is None and maxbudget is not None and price <= int(maxbudget):
							response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with budget Rs."+str(price)+" and "+str(rating)+" rating \n"
							#dispatcher.utter_message("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with budget Rs."+str(price)+"\n")
							count = count + 1
						elif minbudget is not None and maxbudget is None and price >= int(minbudget):
							response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with budget Rs."+str(price)+" and "+str(rating)+" rating \n"
							#dispatcher.utter_message("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with budget Rs."+str(price)+"\n")
							count = count + 1
						else: 
							#print('dint go inside any loop '+str(price))
							pass

						if count >= maxcount:
							search=False
							break
					except:
						#print("Oops!",sys.exc_info(),"occured.")
						pass
			
			if start<500:
				start=start + 20
			else:
				search=False
		dispatcher.utter_message("-----\n"+response)
		self.response = response
		#dispatcher.utter_message("-----\n")
		return [SlotSet('location',loc)]

