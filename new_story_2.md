## Generated Story 8610499701351916020
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chennai"}
    - action_validate_location
    - slot{"location": "chennai"}
    - action_validate_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"freetext": null}
    - utter_ask_budget
* restaurant_search{"minbudget": "700"}
    - slot{"minbudget": "700"}
    - action_restaurant
    - slot{"location": "chennai"}
    - utter_ask_email_preference
* send_email{"emailid": "ahbcdj@dkj.com"}
    - slot{"emailid": "ahbcdj@dkj.com"}
    - action_email
    - slot{"emailid": "ahbcdj@dkj.com"}
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
