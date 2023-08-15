from flask import Flask, request, jsonify
from views import views
import subprocess

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

@app.route('/generate-recipes', methods=['POST'])
def generate_recipes():
    data = request.json
    selected_ingredients = data.get('ingredients', [])

    #run the RecipeGenerator.py script with selected ingredients
    script_path = 'RecipeGenerator.py' #potential error
    command = ['python', script_path] + selected_ingredients
    subprocess.run(command)

    return jsonify({'message': 'Recipe generation started successfully'})
# @app.route('/send-ingredients', methods=['POST'])
# def recieve_ingredients():
#     data = request.json
#     selected_ingredients = data.get('ingredients', [])

#     return jsonify({'message': 'Ingredients recieved successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)