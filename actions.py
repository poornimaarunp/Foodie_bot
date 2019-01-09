from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import sys

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		tier1=['ahmedabad','bangalore','chennai','delhi','hyderabad','kolkata','mumbai','pune','agra','ajmer'
               ,'aligarh','amravati','amritsar','asansol','aurangabad','bareilly', 'belgaum', 'bhavnagar', 'bhiwandi','bhopal',
               'bhubaneswar', 'bikaner','bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 
               'durg-bhilai nagar', 'durgapur','erode','faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gurgaon',
               'guwahati','gwalior','hubli-dharwad','indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 
               'jhansi', 'jodhpur','kannur', 'kanpur','kakinada', 'kochi', 'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode',
               'kurnool', 'lucknow','ludhiana', 'madurai','malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore',
               'nagpur', 'nanded','nashik', 'nellore', 'noida','palakkad', 'patna', 'pondicherry', 'prayagraj', 'raipur', 'rajkot',
               'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli','siliguri', 'solapur', 'srinagar', 'sultanpur', 'surat',
               'thiruvananthapuram','thrissur', 'tiruchirappalli', 'tirunelveli','tiruppur', 'ujjain', 'bijapur', 'vadodara', 'varanasi',
               'vasai-virar city','vijayawada', 'visakhapatnam', 'warangal','bombay','madras','calcutta','gautam budh nagar',
               'new delhi','hydrabad','bengaluru','bengalore','ahemdabad'] 
		
		if location not in tier1:
			dispatcher.utter_template("utter_wrong_city",tracker)
			location=None
		
		return [SlotSet('location',location)]

class ActionValidateCuisine(Action):
	def name(self):
		return 'action_validate_cuisine'

	def run(self, dispatcher, tracker, domain):
		cuisine=tracker.get_slot('cuisine')
		cuisine_list = ['american','italian','chinese','mexican','north indian','south indian']
		while cuisine not in cuisine_list:      
			dispatcher.utter_template("utter_wrong_cuisine",tracker) 
			SlotSet('cuisine',None)
			cuisine = input("Select from the available options:  ")    
			break
			SlotSet('cuisine',cuisine)
		return [SlotSet('cuisine',cuisine)]

class ActionSearchRestaurants(Action):
	response = ""
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain, maxcount=5):
		#config={ "user_key":"41ddf20238cafa7413e2ae7c9c6ce83d"} #mykey
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
		cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north_indian':50,'south_indian':85}
		search = True
		count=0
		start=0
		response=""
		while search:
			results=zomato.restaurant_search_paginated("", lat, lon, str(cuisines_dict.get(cuisine.lower())), start, 20)
			d = json.loads(results)
			if d['results_found'] == 0:
				#response= "no results"
				pass
			else:
				for restaurant in d['restaurants']:
					try:
						price = restaurant['restaurant']['average_cost_for_two']
						rating = restaurant['restaurant']['user_rating']['aggregate_rating']
						if minbudget is not None and maxbudget is not None and price <= int(maxbudget) and price >= int(minbudget):
							response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+". And the average price for two people here is: Rs."+str(price)+"\n"
							#dispatcher.utter_message("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with budget Rs."+str(price)+"\n")
							count = count + 1
						elif minbudget is None and maxbudget is not None and price <= int(maxbudget):
							response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+". And the average price for two people here is: Rs."+str(price)+"\n"
							#dispatcher.utter_message("Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" with budget Rs."+str(price)+"\n")
							count = count + 1
						elif minbudget is not None and maxbudget is None and price >= int(minbudget):
							response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+". And the average price for two people here is: Rs."+str(price)+"\n"
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
		if len(response) > 1: dispatcher.utter_message("Showing you top rated restaurants:\n"+response)
		else: dispatcher.utter_message("Sorry, we couldnt find restaurants that match your search.")
		self.response = response
		#dispatcher.utter_message("-----\n")
		return [SlotSet('location',loc)]

