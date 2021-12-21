## no_interaction
* greet
    - utter_greet
* goodbye
    - utter_goodbye

## location_not_found
* restaurant_search{"location": "Rishikesh"}
    - action_check_location
    - utter_ask_location

## location_specified
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_email_prompt
* restaurant_search{"email" : "pyemailrasa@gmail.com"}
    - slot{"email" : "pyemailrasa@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye

## worng_location_specified
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - utter_ask_location
* restaurant_search{"location": "kannur"}
    - slot{"location": "kannur"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "kannur"}
    - utter_email_prompt
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
    - utter_goodbye

## cuisine_specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_location
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "italian"}
    - utter_email_prompt
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
    - utter_goodbye

## no_search_results_cuisine_specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "nellore"}
    - slot{"location": "nellore"}
    - action_check_location
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"location": "nellore"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - utter_email_prompt
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
    - utter_goodbye

## no_search_results_location_specified
* greet
    - utter_greet
* restaurant_search{"location": "solapur"}
    - slot{"location": "solapur"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - slot{"location": "solapur"}
    - slot{"cuisine": "mexican"}
    - action_search_restaurants
    - utter_email_prompt
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "chandigarh"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_email_prompt
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
* not
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Bengaluru", "price": "mid"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Bengaluru"}
    - slot{"price": "mid"}
    - action_check_location
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - utter_email_prompt
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* restaurant_search{"location": "kamareddy"}
    - slot{"location": "kamareddy"}
    - action_check_location
    - utter_ask_location
* affirm
    - utter_goodbye

## location_specified_2
* greet
    - utter_greet
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - utter_email_prompt
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
* not
    - utter_goodbye

## location_specified_3
* greet
    - utter_greet
* restaurant_search{"location": "kamareddy"}
    - slot{"location": "kamareddy"}
    - action_check_location
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - utter_email_prompt
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
* not
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - utter_email_prompt
* restaurant_search{"email": "jjithin1910@gmail.com"}
    - slot{"email": "jjithin1910@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "Alwar"}
    - slot{"location": "Alwar"}
    - action_check_location
    - utter_ask_location
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chines"}
    - slot{"cuisine": "chines"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - slot{"location": "kanpur"}
    - utter_ask_email
* restaurant_search{"email": "pyemailrasa@gmail.com"}
    - slot{"email": "pyemailrasa@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_email_prompt
* affirm
    - utter_ask_email
* restaurant_search{"email": "jjithin1910@gmail.com"}
    - slot{"email": "jjithin1910@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chenai"}
    - slot{"location": "chenai"}
    - action_check_location
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "mid"}
    - slot{"price": "mid"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_email_prompt
* affirm
    - utter_ask_email
* restaurant_search{"email": "jjithin1910@gmail.com"}
    - slot{"email": "jjithin1910@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_goodbye

