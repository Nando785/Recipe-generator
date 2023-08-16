import requests, sys

ingredients = sys.argv[1:]
response = requests.post('http://127.0.0.1:8000/send-ingredients', json={'ingredients': ingredients})

if response.status_code == 200:
    print('Ingredients sent successfully')
else:
    print('Failed to send ingredients')

#======================================== RECIPE FINDER ========================================

#parameters customized through "ingredients_list" in frontend
numberOfRecipes = 2
ignorePantry = True
ranking = 2

url = "https://api.spoonacular.com/recipes/findByIngredients"

querystring = {"ingredients":ingredients, 
               "number":numberOfRecipes,
               "ignorePantry":ignorePantry,
               "ranking":ranking}

headers = {
    "x-api-key" : "170112d56069460d9a732b82cc328a8e",
    "X-RapidAPI-Host" : "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

#callAPI and convert result into json/dictionary
recipesList = requests.get(url, headers=headers, params=querystring)
#data = recipesList.json();

# print(data)
#++++++++++++++++++++++++++++++++++++++++++++ VV Temporary commenting VV ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# #======================================== Parse information ========================================
# #ids for all resulting recipes will be parsed from the first api call and used in
# #the new api call for recipe info

# idList = []
# for index in data:
#     idList.append(index["id"])

# #===================================== RECIPE INFO FINDER =====================================

# infoURL = "https://api.spoonacular.com/recipes/informationBulk"

# queryStringINFO = {}

# #Convert the idList integers to strings and join them with commas
# ids_string = ",".join(map(str, idList))

# #add ids into queryStringINFO dictionary
# queryStringINFO["ids"] = ids_string

# #headers already declared above
# info = requests.get(infoURL, headers=headers, params=queryStringINFO)

# #convert result into json/dictionary
# infoData = info.json();


# #=========================== Gather all resulting info and combine into list ===========================
# #all neccessary info is in "data" and "infoData"

# class Recipe:
#     #== info from first API call ==
#     id: int #id
#     name: str #title
#     photo: str #image
#     missedIngredientCount: int #missedIngredientCount

#     #== info from second API call ==
#     recipeLink: str #sourceURL
#     vegetarian: bool #vegeterian
#     glutenFree: bool #glutenFree
#     servings: int #servings
#     pricePerServing: int #pricePerServing
#     cookingTime: int # readyInMinutes
#     instructions: str #instructions

# finalRecipes = []

# #append recipe to each index in finalRecipes list, adding info from resulting API returns
# for index in data:
#     finalRecipes.append()

# print(finalRecipes[0])