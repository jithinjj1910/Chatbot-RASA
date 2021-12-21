from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
import zomatopy
import json

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = ''
response = ''

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		count = 0
		config={ "user_key":"9d6c4fde8b9be13c54c593d5355aa7ed"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'italian':55,'mexican':73,'american':1,'south indian':85,'north indian':50}
		price_dict = {'low':1,'mid':2,'high':3}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5000)
		d = json.loads(results)
		response="Showing you Top Rated Restaurants"
		if d['results_found'] == 0:
			response= "No restaurant Found"
			dispatcher.utter_message(response)
		else:
			for restaurant in sorted(d['restaurants'], key = lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse = True):
				if((price_dict.get(price) == 1) and (restaurant['restaurant']['average_cost_for_two'] < 300) and (count < 10)):
					response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"."
					response=response+" And the average price for two people is: "+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
					count = count + 1
				elif((price_dict.get(price) == 2) and (restaurant['restaurant']['average_cost_for_two'] >= 300) and (restaurant['restaurant']['average_cost_for_two'] <= 700) and (count < 10)):
					response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"."
					response=response+" And the average price for two people is: "+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
					count = count + 1
				elif((price_dict.get(price) == 3) and (restaurant['restaurant']['average_cost_for_two'] > 700) and (count < 10)):
					response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"."
					response=response+" And the average price for two people is: "+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
					count = count + 1
				if (count==5):
					dispatcher.utter_message(response)
		if(count<5 and count>0):
			dispatcher.utter_message(response)
		if(count==0):
			response = "Sorry, No results found for your criteria. Would you like to search for some other restaurants?"
			dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ActionSendEmail(Action):

	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		count = 0
		config={ "user_key":"9d6c4fde8b9be13c54c593d5355aa7ed"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		email = tracker.get_slot('email')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'italian':55,'mexican':73,'american':1,'south indian':85,'north indian':50}
		price_dict = {'low':1,'mid':2,'high':3}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5000)
		d = json.loads(results)
		message="Showing you Top Rated Restaurants: \n"
		if d['results_found'] == 0:
			message= "No restaurant Found"
			dispatcher.utter_message(message)
		else:
			for restaurant in sorted(d['restaurants'], key = lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse = True):
				if((price_dict.get(price) == 1) and (restaurant['restaurant']['average_cost_for_two'] < 300) and (count < 10)):
					message=message+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"."
					message=message+" And the average price for two people is: "+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
					count = count + 1
				elif((price_dict.get(price) == 2) and (restaurant['restaurant']['average_cost_for_two'] >= 300) and (restaurant['restaurant']['average_cost_for_two'] <= 700) and (count < 10)):
					message=message+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"."
					message=message+" And the average price for two people is: "+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
					count = count + 1
				elif((price_dict.get(price) == 3) and (restaurant['restaurant']['average_cost_for_two'] > 700) and (count < 10)):
					message=message+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"."
					message=message+" And the average price for two people is: "+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
					count = count + 1

		res = "The details of the restaurant you enquired are \n \n"
		res = res + message
		#the mail addresses and password
		sender_address = "pyemailrasa@gmail.com"
		sender_pass = "python12345678"
		receiver_address = email

		#setup MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = "Foodie Restaurant Search Results"

		#the body and the attachments for the mail
		message.attach(MIMEText(res, 'plain'))
		#create a SMTP session for sending the email
		session = smtplib.SMTP('smtp.gmail.com', 587)
		session.starttls()
		session.login(sender_address, sender_pass)
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, res)
		session.quit()
		dispatcher.utter_message("Email Sent!!! Please check your Inbox")
		return[AllSlotsReset()]

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc =  tracker.get_slot('location')

		cities = ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Agra', 'Ajmer', 'Aligarh', 
                  'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 
                  'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 
                  'Dindigul', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 
                  'Hamirpur', 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 
                  'Kakinada', 'Kannur', 'Kanpur', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 
                  'Mathura', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Patna', 'Pondicherry', 'Purulia', 
                  'Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 
                  'Thanjavur', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 
                  'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']

		cities_lower = [x.lower() for x in cities]
		if loc.lower() not in cities_lower:
			dispatcher.utter_message("We do not operate in that area yet. Please choose some other location")
		return






