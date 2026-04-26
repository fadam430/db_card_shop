checkout_button = document.getElementById('proceed-to-checkout');

if (checkout_button) { 
    checkout_button.addEventListener('click', function() {
        window.location.href = '/checkout/';
    });
}