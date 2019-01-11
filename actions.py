from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import sys
import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage

import traceback as tb

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')

		print("in validateloc - Location:"+str(tracker.get_slot('location')))
		print("cuisine:"+str(tracker.get_slot('cuisine')))
		print("minbudget:"+str(tracker.get_slot('minbudget')))
		print("maxbudget:"+str(tracker.get_slot('maxbudget')))

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
               'vasai-virar city','vijayawada', 'visakhapatnam', 'warangal']
		try:
			if location is None or str(location).lower() not in tier1:
				dispatcher.utter_template("utter_wrong_city",tracker)
				location = None
		except:
			location = None

		return [SlotSet('location',location)]

class ActionValidateCuisine(Action):
	def name(self):
		return 'action_validate_cuisine'

	def run(self, dispatcher, tracker, domain):
		cuisine=tracker.get_slot('cuisine')
		freetext = tracker.get_slot('freetext')

		print("in validate cuisine - Location:"+str(tracker.get_slot('location')))
		print("cuisine:"+str(tracker.get_slot('cuisine')))
		print("minbudget:"+str(tracker.get_slot('minbudget')))
		print("maxbudget:"+str(tracker.get_slot('maxbudget')))
		print("freetext:"+str(tracker.get_slot('freetext')))
		cuisine_list = ['american','italian','chinese','mexican','north indian','south indian']
		cuisine_buttons = {1:"chinese", 2:"mexican", 3:"italian", 4:"american", 5:"south indian", 6:"north indian"}

		try:
			if  cuisine is None and freetext is not None:
				cuisine = cuisine_buttons.get(int(freetext))
			elif cuisine is None or str(cuisine).lower() not in cuisine_list:
				dispatcher.utter_template("utter_wrong_cuisine",tracker)
				cuisine = None
		except:
			cuisine = None

		return [SlotSet('cuisine',cuisine),SlotSet('freetext',None)]

class ActionValidateBudget(Action):
	def name(self):
		return 'action_validate_budget'

	def run(self, dispatcher, tracker, domain):
		minbudget = tracker.get_slot('minbudget')
		maxbudget = tracker.get_slot('maxbudget')
		freetext = tracker.get_slot('freetext')
		print("in validate budget - Location:"+str(tracker.get_slot('location')))
		print("cuisine:"+str(tracker.get_slot('cuisine')))
		print("minbudget:"+str(tracker.get_slot('minbudget')))
		print("maxbudget:"+str(tracker.get_slot('maxbudget')))
		print("freetext:"+str(tracker.get_slot('freetext')))
		try:
			if minbudget is not None and maxbudget is not None and str(minbudget).isdigit() and str(maxbudget).isdigit():
				pass
			elif minbudget is None and maxbudget is not None and str(maxbudget).isdigit():
				pass
			elif minbudget is not None and maxbudget is None and str(minbudget).isdigit():
				pass
			elif minbudget is None and maxbudget is None and str(freetext).isdigit() and len(freetext)<3:
				if str(freetext) is "1":
					maxbudget = "300"
					minbudget = None
				elif str(freetext) is "2":
					maxbudget = "700"
					minbudget = "300"
				elif str(freetext) is "3":
					maxbudget = None
					minbudget = "700"
				else:
					dispatcher.utter_template("utter_wrong_budget",tracker)
					minbudget = None
					maxbudget = None
					freetext = None
			else:
				dispatcher.utter_template("utter_wrong_budget",tracker)
				minbudget = None
				maxbudget = None
				freetext = None
		except:
			minbudget = None
			maxbudget = None
			freetext = None

		return [SlotSet('minbudget',minbudget),SlotSet('maxbudget',maxbudget),SlotSet('freetext',freetext)]

class ActionSearchRestaurants(Action):
	response = ""
	def name(self):
		return 'action_restaurant'

	def run(self, dispatcher, tracker, domain, maxcount=5):
		#config={ "user_key":"41ddf20238cafa7413e2ae7c9c6ce83d"} #mykey
		config={ "user_key":"4b15397292c01e6dbf85074d0952d14b"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		minbudget = tracker.get_slot('minbudget')
		maxbudget = tracker.get_slot('maxbudget')
		print("in search - Location:"+str(tracker.get_slot('location')))
		print("cuisine:"+str(tracker.get_slot('cuisine')))
		print("minbudget:"+str(tracker.get_slot('minbudget')))
		print("maxbudget:"+str(tracker.get_slot('maxbudget')))
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
		search = True
		count=0
		start=0
		response=""
		dispatcher.utter_message("Looking for restaurants based on your preference ... ")
		while search:
			results=zomato.restaurant_search_paginated("", lat, lon, str(cuisines_dict.get(cuisine)), start, 20)
			d = json.loads(results)
			if d['results_found'] == 0:
				#response= "no results"
				pass
			else:
				for restaurant in d['restaurants']:
					try:
						price = restaurant['restaurant']['average_cost_for_two']
						# rating = restaurant['restaurant']['user_rating']['aggregate_rating']
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


class ActionSendEmail(Action):
	def name(self):
		return 'action_email'

	def run(self, dispatcher, tracker, domain):
		mailid = tracker.get_slot('emailid')
		# dispatcher.utter_message("email id parsed = "+mailid)
		if(mailid == None):
			while (True):
				dispatcher.utter_template("utter_invalid_emailid", tracker)
				# dispatcher.utter_message("inside while loop mailid entered :"+mailid)
				# r"^[\w\.\+\-]+\@[\w]+[\.[a-z]]{2,5}$"
				# r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
				if(bool(re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", mailid))):
					break
		# dispatcher.utter_message("final emailid"+mailid)
		SlotSet('emailid',mailid)

		dispatcher.utter_message("Sending email ... ")
		smtpServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		emailContent = MIMEMultipart('alternative')
		# messageBody = "<h3>restaurant search results from chatbot</h3>"
		zc = ZomatoClient()
		messageBody = zc.restaurantResultForEmail(dispatcher, tracker, domain,10)
		emailContent['Subject'] = 'Zomato restaurant search results'
		emailContent['From'] = 'chatbotemailer123@gmail.com'
		emailContent['To'] = mailid
		emailContent.attach(MIMEText(messageBody,'html'))
		smtpServer.ehlo()
		smtpServer.login('chatbotemailer123@gmail.com','learn.123')
		smtpServer.send_message(emailContent)
		smtpServer.quit()
		# dispatcher.utter_message("Sent email successfully to "+mailid)
		return [SlotSet('emailid',mailid)]

class ZomatoClient:

	def restaurantResultForEmail(self,dispatcher, tracker, domain,maxcount):
		config={ "user_key":"4b15397292c01e6dbf85074d0952d14b"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		minbudget = tracker.get_slot('minbudget')
		maxbudget = tracker.get_slot('maxbudget')
		messageBody = ""
		try:
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			cuisines_dict={'american':1,'chinese':25,'mexican':73,'italian':55,'north indian':50,'south indian':85}
			search = True
			count=0
			start=0
			messageBody = "<h3>restaurant search results </h3>"
			messageBody = messageBody + "You recently searched for restaurants in "+loc+" serving "+cuisine+" cuisine. Please refer to the details below.<br/>"
			messageBody = messageBody + "<table  border=\" 5px solid black\" >"
			messageBody = messageBody + "<tr> <th>Restaurant</th> <th>Address</th>  <th>Average price for two</th> </tr>"
			messageBody = messageBody + ""
			while search:
				results=zomato.restaurant_search_paginated("", lat, lon, str(cuisines_dict.get(cuisine)), start, 20)
				d = json.loads(results)
				if d['results_found'] == 0:
					pass
				else:
					for restaurant in d['restaurants']:
						try:
							price = restaurant['restaurant']['average_cost_for_two']
							if minbudget is not None and maxbudget is not None and price <= int(maxbudget) and price >= int(minbudget):
								messageBody = messageBody + " <tr> <td>"+ restaurant['restaurant']['name']+ "</td> <td>"+ restaurant['restaurant']['location']['address']+"</td> <td>"+str(price)+"</td> </tr>"
								count = count + 1
							elif minbudget is None and maxbudget is not None and price <= int(maxbudget):
								messageBody = messageBody + " <tr> <td>"+ restaurant['restaurant']['name']+ "</td> <td>"+ restaurant['restaurant']['location']['address']+"</td> <td>"+str(price)+"</td> </tr>"
								count = count + 1
							elif minbudget is not None and maxbudget is None and price >= int(minbudget):
								messageBody = messageBody + " <tr> <td>"+ restaurant['restaurant']['name']+ "</td> <td>"+ restaurant['restaurant']['location']['address']+"</td> <td>"+str(price)+"</td> </tr>"
								count = count + 1
							else:
								pass

							if count >= maxcount:
								search=False
								break
						except:
							pass

				if start<500:
					start=start + 20
				else:
					search=False
			messageBody = messageBody + "</table>"
			messageBody = messageBody + "<h4> Bon Appetit! </h4>"
		except:
			messageBody = messageBody + "<p>Error while trying to populate results for email. </p>"
		return messageBody

class ActionClearSlots(Action):
	def name(self):
		return 'action_clear_slots'

	def run(self, dispatcher, tracker, domain):
		return [SlotSet('location',None),
				SlotSet('cuisine',None),
				SlotSet('minbudget',None),
				SlotSet('maxbudget',None),
				SlotSet('emailid',None),
				SlotSet('freetext',None)]
