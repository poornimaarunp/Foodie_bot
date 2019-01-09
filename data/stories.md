## Generated Story 255706069223404498
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
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
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
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
    - utter_goodbye

## Generated Story 3320800183399695936
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
    - utter_ask_budget
* restaurant_search{"maxbudget": "300"}
    - slot{"maxbudget": "300"}
    - action_restaurant
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_restaurant
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "yugadeepa.c@gmail.com"}
    - action_email
    - utter_emailed_you
* affirm
    - utter_goodbye
    - export

## Generated Story -7060460724450246491
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search
    - action_validate_location
    - slot{"location": null}
* restaurant_search
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - action_validate_location
    - slot{"location": null}
* restaurant_search
    - action_validate_location
    - slot{"location": null}
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - utter_ask_budget
* restaurant_search{"maxbudget": "700"}
    - slot{"maxbudget": "700"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_email_preference
* deny
    - utter_goodbye
    - export
