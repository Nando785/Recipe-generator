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

response = requests.get(url, headers=headers, params=querystring)

print(response.status_code)
#print(response.json())
for recipe in response:
    print("Recpie name:" + recipe['title'])


#===================================== RECIPE INFO FINDER =====================================

#ids for all resulting recipes will be parsed from the first api call and used in
#the new api call for recipe info
id = 673463

infoURL = "https://api.spoonacular.com/recipes/{id}/information"

#===== headers already declared above =====
# headers = {
#     "x-api-key" : "170112d56069460d9a732b82cc328a8e",
#     "X-RapidAPI-Host" : "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
# }

#response = requests.get(infoURL, headers=headers)

print(response.json())