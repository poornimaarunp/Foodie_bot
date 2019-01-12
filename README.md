# Foodie_bot

## Problem Statement
An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. You have been hired as the lead data scientist for creating this product.
 
The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. 

## Training the model
Run the command 
`python ./nlu_model.py`

The trained model gets stored under the folder 
`/models/nlu/`

## Test the trained model
Run the command to expose the model through an API 
`python ./App_nlu.py`

Use the below curl command to pass the query and hit the API
`curl -X POST \
  http://localhost:5000/nlu_parsing \
  -H 'content-type: application/json' \
  -d '{
	"utterance": "find me some chinese restaurants"
}'`

The response from the api would be as below
`{
    "intent_ranking": [
        {
            "name": "restaurant_search",
            "confidence": 0.7775803330936192
        },
        {
            "name": "affirm",
            "confidence": 0.15557676964868206
        },
        {
            "name": "greet",
            "confidence": 0.04667012448111812
        },
        {
            "name": "goodbye",
            "confidence": 0.02017277277658057
        }
    ],
    "text": "find me some chinese restaurants",
    "intent": {
        "name": "restaurant_search",
        "confidence": 0.7775803330936192
    },
    "entities": [
        {
            "entity": "cuisine",
            "start": 13,
            "value": "chinese",
            "processors": [
                "ner_synonyms"
            ],
            "confidence": 0.9108371301308732,
            "end": 20,
            "extractor": "ner_crf"
        }
    ]
}`

## Training Dialogue management model
To train the dialogue management model, Run the command 
`python ./train_init.py`

## Run the bot
To run the bot from command line, Run the command 
`python ./dialogue_management_model.py`


