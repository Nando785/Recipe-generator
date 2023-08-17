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
    script_path = 'RecipeGenerator.py' 
    command = ['python', script_path] + selected_ingredients
    #subprocess.run(command)

    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        #debug: pring script output
        print(result)

        #return jsonify({'message': 'Recipe generatoin started successfully'})
        return jsonify({'recipes': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True, port=8000)