from random import randint
rand = randint
from fastapi import FastAPI
app = FastAPI()

suggestions = {
    "food": [
        {
            "name": "Street hot dog",
            "price": "$",
            "location": "Harbourfront"
        },
        {
            "name": "Egg sandwich",
            "price": "$",
            "location": "Kensington Market"
        },
        {
            "name": "Oat milk latte",
            "price": "$$",
            "location": "Queen Street West"
        },
        {
            "name": "Fresh churro",
            "price": "$",
            "location": "Distillery District"
        },
        {
            "name": "Butter tart",
            "price": "$",
            "location": "Cabbagetown"
        },
        {
            "name": "Matcha latte",
            "price": "$$",
            "location": "Bloor Street West"
        },
        {
            "name": "Slice of pizza",
            "price": "$",
            "location": "Ossington Avenue"
        },
        {
            "name": "Fish tacos",
            "price": "$$",
            "location": "Toronto Islands"
        }
    ],
    "activity": [
        {
            "name": "Waterfront walk",
            "price": "free",
            "location": "Harbourfront"
        },
        {
            "name": "Thrift shopping",
            "price": "free",
            "location": "Kensington Market"
        },
        {
            "name": "Cafe journaling",
            "price": "free",
            "location": "Queen Street West"
        },
        {
            "name": "Watch street performers",
            "price": "free",
            "location": "Distillery District"
        },
        {
            "name": "Historic neighbourhood walk",
            "price": "free",
            "location": "Cabbagetown"
        },
        {
            "name": "Browse indie bookstores",
            "price": "free",
            "location": "Bloor Street West"
        },
        {
            "name": "Park hangout",
            "price": "free",
            "location": "Trinity Bellwoods"
        }
    ]
}




@app.get("/ping")
def health_check():
    return {"ok": True}

@app.get("/suggestion/{genre}")
def suggestion(genre: str):
    random_num = rand(0, 3)
    print(random_num)
    sugg_list = list(suggestions.keys())
    print(sugg_list)
    for i in sugg_list:
        if i == genre:
            gen_type = i
            print(suggestions[gen_type][random_num])
            return suggestions[gen_type][random_num]
    
    
@app.get("/")


