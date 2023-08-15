const ingredients = document.querySelectorAll('.ingredient');
const submitButton = document.querySelector('.submit_button');

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
    const ingredientButtons = document.querySelectorAll('.ingredient');

    ingredientButtons.forEach(ingredient => {
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
            console.log(data.message); // Log the response message
        })
        .catch(error => {
            console.error('Error:', error);
        });
});