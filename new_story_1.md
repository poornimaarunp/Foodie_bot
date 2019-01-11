## Generated Story 9178781714626814500
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_validate_budget
    - slot{"minbudget": "700"}
    - slot{"maxbudget": null}
    - slot{"freetext": null}
    - action_restaurant
    - slot{"location": "chennai"}
    - utter_ask_email_preference
* affirm
    - utter_ask_emailid
* send_email{"emailid": "test@gmail.com"}
    - slot{"emailid": "test@gmail.com"}
    - action_email
    - slot{"emailid": "test@gmail.com"}
    - utter_emailed_you
* affirm
    - utter_goodbye
    - action_clear_slots
    - slot{"location": null}
    - slot{"cuisine": null}
    - slot{"minbudget": null}
    - slot{"maxbudget": null}
    - slot{"emailid": null}
    - slot{"freetext": null}
    - export
