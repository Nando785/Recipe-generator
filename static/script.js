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
});