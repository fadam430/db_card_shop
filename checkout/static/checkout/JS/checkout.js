const stripePublicKey = JSON.parse(document.getElementById('id_stripe_public_key').textContent);
const clientSecret = JSON.parse(document.getElementById('id_client_secret').textContent);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

const card = elements.create('card', {
    style: {
        base: {
            color: '#000',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            fontSize: '16px',
            '::placeholder': { color: '#aab7c4' }
        },
        invalid: { color: '#dc3545', iconColor: '#dc3545' }
    }
});

card.mount('#card-element');

// Show card errors in real time
card.addEventListener('change', (e) => {
    const errorDiv = document.getElementById('card-errors');
    errorDiv.textContent = e.error ? e.error.message : '';
});

// Handle form submit
const form = document.getElementById('checkout-form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    card.update({ disabled: true });
    document.getElementById('submit-button').disabled = true;

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name.value,
                email: form.email.value,
            }
        }
    }).then((result) => {
        if (result.error) {
            document.getElementById('card-errors').textContent = result.error.message;
            card.update({ disabled: false });
            document.getElementById('submit-button').disabled = false;
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});