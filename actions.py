from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		loc=tracker.get_slot('location')
		cuisine=tracker.get_slot('cuisine')
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
		while loc not in tier1:
			dispatcher.utter_template("utter_wrong_city",tracker)
			SlotSet('location',None)
			loc = input("Select from the another city in which we operate: ")    
			break
			SlotSet('location',loc)                
		return [SlotSet('location',loc)]

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
			SlotSet('cuisine',cusine)
		return [SlotSet('cuisine',cuisine)]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6ce88a5ec1419e335afa1c7f92f4b739"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north_indian':50,'south_indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		SlotSet('location',None)
		SlotSet('cuisine',None)
		return [SlotSet('location',None),SlotSet('cuisine',None)]
