const ingredients = document.querySelectorAll('.ingredient');
const submitButton = document.querySelector('.submit_button');

//add ingredient button selecting functionality
ingredients.forEach(ingredient => {
    ingredient.addEventListener('click', function () {
        const isChecked = this.getAttribute('data-checked') === 'true';
        this.setAttribute('data-checked', !isChecked);
        this.classList.toggle('checked');
    });
});

submitButton.addEventListener('click', function () {
    const isChecked = this.getAttribute('data-checked') === 'true';
    this.setAttribute('data-checked', !isChecked);
    // this.classList.toggle('submit_button.checked');
    submitButton.classList.toggle('checked');

    const selectedIngredients = [];
    //grab all ingredient buttons
    const ingredientButtons = document.querySelectorAll('.ingredient');

    ingredientButtons.forEach(ingredient => {
        //if ingredient is checked, add div word into list
        if(ingredient.classList.contains('checked')){
            selectedIngredients.push(ingredient.textContent);
        }
    });

    // Send selected ingredients to the Flask route
    fetch('/generate-recipes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ ingredients: selectedIngredients })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        console.log(data.message); // Log the response message

        const recipeResults = document.querySelector('.recipe_results');

        //clear previous results
        recipeResults.innerHTML = '';

        //loop through the data and create a new div for each recipe
        const recipeDiv = document.createElement('div');
            recipeDiv.classList.add('recipe_item');
            recipeDiv.textContent = "Test";
            recipeResults.appendChild(recipeDiv);
        // data.recipes.forEach(recipe => {
        //     const recipeDiv = document.createElement('div');
        //     recipeDiv.classList.add('recipe_item');
        //     recipeDiv.textContent = "Title: ${recipe.title}, Likes: ${recipe.likes}";
        //     recipeResults.appendChild(recipeDiv);
        // });
    })
    .catch(error => {
        console.error('Error:', error);
    });
});