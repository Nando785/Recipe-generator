const ingredients = document.querySelectorAll('.ingredient');

ingredients.forEach(ingredient => {
    ingredient.addEventListener('click', function () {
        const isChecked = this.getAttribute('data-checked') === 'true';
        this.setAttribute('data-checked', !isChecked);
        this.classList.toggle('checked');
    });
});