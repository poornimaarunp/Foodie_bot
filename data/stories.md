## Generated Story 255706069223404498 OK
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"minbudget": "300","maxbudget": "700"}
    - slot{"minbudget": "300"}
    - slot{"maxbudget": "700"}
    - action_validate_budget
* restaurant_search{"minbudget": "300","maxbudget": "700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
    - utter_goodbye
    - action_clear_slots
    - export

## Generated Story 1993277579540566202 OK 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_validate_budget
* restaurant_search{"minbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
    - utter_goodbye
    - action_clear_slots
    - export

## Generated Story 1993277579540566202 OK 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"freetext": "3"}
    - slot{"freetext": "3"}
    - action_validate_budget
* restaurant_search{"minbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
    - utter_goodbye
    - action_clear_slots
    - export

## Generated Story 3320800183399695936 - OK
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - action_validate_location
    - slot{"location": "delhi"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"maxbudget": "300"}
    - slot{"maxbudget": "300"}
    - action_validate_budget
* restaurant_search{"maxbudget": "300"}
    - action_restaurant
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
* goodbye
    - utter_goodbye
    - action_clear_slots
    - export

## Generated Story 4963448062290237512 - OK
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_validate_budget
* restaurant_search{"minbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
* affirm
    - utter_goodbye
    - action_clear_slots
    - export

## Generated Story 567857863456356357 - OK
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_validate_budget
* restaurant_search{"minbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
    - utter_goodbye
    - action_clear_slots
    - export
    

## Generated Story 390287473924738294 - OK
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_validate_budget
* restaurant_search{"minbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
* affirm
    - utter_goodbye
    - action_clear_slots
    - export
    
## Generated Story -3830891401256760553 - OK
* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_validate_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search
    - slot{"cuisine": "1"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_validate_budget
* restaurant_search{"minbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* send_email
    - utter_ask_emailid
* send_email
    - action_email
    - action_clear_slots
    - export


## Generated Story 5867629175671392140 - OK
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - action_validate_location
    - slot{"location": "ludhiana"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - slot{"freetext": null}
    - utter_ask_budget
* restaurant_search{"maxbudget": "700", "minbudget": "300"}
    - slot{"maxbudget": "700"}
    - slot{"minbudget": "300"}
    - action_validate_budget
* restaurant_search{"maxbudget": "700", "minbudget": "300"}
    - action_restaurant
    - slot{"location": "ludhiana"}
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "anupama1204@yahoo.com"}
    - slot{"emailid": "anupama1204@yahoo.com"}
    - action_email
    - utter_emailed_you
    - action_clear_slots
    - export

 ## Generated Story 9200166762348421103
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"minbudget": "800"}
    - slot{"minbudget": "800"}
    - action_validate_budget
* restaurant_search{"minbudget": "800"}
    - action_restaurant
    - utter_ask_email_preference
* deny
    - utter_goodbye
    - action_clear_slots
* goodbye
* greet
    - export

## Generated Story -1403372025300518616
* greet
    - utter_greet
* restaurant_search{"cuisine": "good"}
    - slot{"cuisine": "good"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search
    - action_validate_budget
    - slot{"minbudget": null}
    - slot{"maxbudget": null}
* restaurant_search
    - action_validate_budget
    - slot{"minbudget": null}
    - slot{"maxbudget": null}
* restaurant_search{"maxbudget": "700"}
    - slot{"maxbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* deny
    - utter_goodbye
* affirm
    - action_clear_slots
    - export

## Generated Story 6162803233937091025
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"freetext": "1"}
    - slot{"freetext": "1"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_budget
* restaurant_search{"freetext": "1"}
    - slot{"freetext": "1"}
    - action_validate_budget
    - slot{"minbudget": null}
    - slot{"maxbudget": "300"}
    - slot{"freetext": "1"}
    - action_restaurant
    - slot{"location": "chennai"}
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "xyz@abc.co.in"}
    - slot{"emailid": "xyz@abc.co.in"}
    - action_email
    - slot{"emailid": "xyz@abc.co.in"}
    - utter_emailed_you
    - utter_goodbye
    - action_clear_slots
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"minbudget": null}
    - slot{"maxbudget": null}
    - slot{"emailid": null}
    - slot{"freetext": null}
    - export
