import requests

#======================================== RECIPE FINDER ========================================

#parameters customized through "ingredients_list"
ingredients = "apples,flour,sugar"
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

recipesList = requests.get(url, headers=headers, params=querystring)
data = recipesList.json();

#print(recipeList.json())

#get id and recall api to get more info
id = data[0]['id']
print(data[0]['title'])

#======================================== Parse information ========================================

class Recipe:
    id: int #id
    name: str #title
    photo: str #image
    missedIngredientCount: int #missedIngredientCount

    recipeLink: str #sourceURL
    vegetarian: bool #vegeterian
    glutenFree: bool #glutenFree
    servings: int #servings
    pricePerServing: int #pricePerServing
    cookingTime: int # readyInMinutes
    instructions: str #instructions


#===================================== RECIPE INFO FINDER =====================================

#ids for all resulting recipes will be parsed from the first api call and used in
#the new api call for recipe info

infoURL = "https://api.spoonacular.com/recipes/informationBulk"

queryStringINFO = {"ids":str(id)}

#===== headers already declared above =====
infoHeaders = {
    "x-api-key" : "170112d56069460d9a732b82cc328a8e",
    "X-RapidAPI-Host" : "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

info = requests.get(infoURL, headers=infoHeaders, params=queryStringINFO)
# infoData = info.json();

print(info.json())