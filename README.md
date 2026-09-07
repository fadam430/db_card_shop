
# **Dragon Ball Card Shop**: Buy and sell your Dragon Ball cards

[Dragon Ball Card Shop link](https://db-card-shop-5ba6aba51d41.herokuapp.com/)

A Full Stack e-commerce platform dedicated to helping collectors discover,
buy, and sell Dragon Ball trading cards. Users can browse the card catalogue,
manage items in their shopping bag, and complete purchases through a secure
checkout process.

## Table of Contents

> 1. [Overview](#overview)
> 2. [Terminology](#terminology)
> 3. [UX](#ux)
>    1. [Strategy](#strategy)
>    2. [Scope](#scope)
>    3. [Structure](#structure)
>    4. [Skeleton](#skeleton)
>    5. [Surface](#surface)
> 4. [Features](#features)
>    1. [Existing Features](#existing-features)
>    2. [Future Feature Considerations](#future-feature-considerations)
> 5. [Technologies Used](#technologies-used)
> 6. [Testing](#testing)
> 7. [Deployment](#deployment)
> 8. [Credits](#credits)
> 9. [Acknowledgements](#acknowledgements)
> 10. [Disclaimer](#disclaimer)

---

# 1. Overview

**Dragon Ball Card Shop** is a Full Stack e-commerce web application built with
Django and Stripe. It allows users to browse Dragon Ball trading cards, view
product details, add cards to a shopping bag, and complete secure purchases.
The platform also supports user authentication, responsive browsing across
devices, AWS S3 image storage, and Stripe payment processing.

The project was developed using **Python** (Django), **HTML**, **CSS**, and
**JavaScript**. It uses an **AWS S3 bucket** for image storage and **Stripe**
for payment processing.

# 2. Terminology

| Term | Meaning |
| --- | --- |
| Card catalogue | The collection of Dragon Ball cards available to browse |
| Card | A product listed in the shop with a name, category, description, price, quantity, and image |
| Shopping bag | The temporary collection of cards selected for purchase |
| Checkout | The process of entering delivery details and completing payment |
| Administrator | An authorized user who manages cards, categories, prices, stock, and images |
| S3 | Amazon Simple Storage Service used to store uploaded media and static files |

# 3. UX

## Strategy

The website is designed for Dragon Ball collectors who want a straightforward
way to discover and purchase cards online. The user experience focuses on
clear product presentation, simple navigation, visible pricing, and a short
path from browsing to checkout.

## Scope

The application provides:

- A welcoming home page with clear routes to the card catalogue.
- A responsive catalogue of available Dragon Ball cards.
- Product images, categories, descriptions, prices, and stock information.
- User registration, login, and logout functionality.
- Shopping bag management and order totals.
- Checkout and Stripe payment processing.
- Administrative management of cards, categories, prices, quantities, and images.

## Structure

The main navigation provides access to:

- **Home:** Introduction to the shop and featured content.
- **Cards:** The complete card catalogue.
- **About:** Information about the shop.
- **Shopping bag:** Selected products and order totals.
- **Account:** Login, registration, and logout options.

The layout uses a consistent header, navigation bar, main content area, and
footer across the website. Calls to action guide users from the home page to
the catalogue and from the catalogue to the shopping bag.

## Skeleton

### Wireframe

- Home [Link](/media/wireframes/wireframe_02_Home.pdf)
- Card List [Link](/media/wireframes/wireframe_03_Cards_List.pdf)
- Card Detail [Link](/media/wireframes/wireframe_04_Card_Detail.pdf)
- Shopping bag [Link](/media/wireframes/wireframe_05_Shopping_Bag.pdf)
- Checkout [Link](/media/wireframes/wireframe_06_Checkout.pdf)
- Checkout Success [Link](/media/wireframes/wireframe_07_Checkout_Success.pdf)
- Login [Link](/media/wireframes/wireframe_08_Login.pdf)
- Signup [Link](/media/wireframes/wireframe_09_Signup.pdf)


## Surface

The visual design uses a bold Dragon Ball-inspired style with strong primary
colors, clear contrast, card-focused layouts, and responsive Bootstrap
components. Product images are given visual priority, while buttons and
navigation links use consistent styling to make the main actions easy to find.

# 4. Features

## Existing Features

### Customer features

- Browse all cards from the Cards page.
- View card images, names, categories, descriptions, and prices.
- Add cards to the shopping bag when signed in.
- Review, update, and remove items from the shopping bag.
- Continue to checkout with an order summary.
- Submit delivery and payment details.
- Receive an order confirmation after successful checkout.
- Register, log in, and log out of a customer account.
- Use the responsive navigation on desktop, tablet, and mobile screens.

### Administration features

- Manage card products through the Django admin area.
- Create and manage card categories.
- Update card prices and quantities.
- Upload and preview card images.
- Manage orders and order line items.

## Future Feature Considerations

- Search and filter cards by name, category, rarity, and price.
- Customer reviews and ratings.
- Wishlist functionality.
- User profile pages with order history.
- Card condition and grading information.
- Stock alerts and low-inventory notifications.
- Seller accounts for customer card listings.
- Pagination for larger card collections.
- Improved product detail pages with multiple images.

# 5. Technologies Used

## Languages and frameworks

- **Python** and **Django** for the application and backend logic.
- **HTML5** for page structure and templates.
- **CSS3** for styling and responsive presentation.
- **JavaScript** for client-side interaction.
- **Bootstrap** for responsive layout and reusable components.

## Services and packages

- **PostgreSQL** for production database storage.
- **SQLite** for local development where applicable.
- **Amazon S3** for media and static file storage.
- **Stripe** for payment processing.
- **Django Allauth** for account management.
- **django-crispy-forms** for form presentation.
- **Pillow** for image handling.
- **Gunicorn** as the production web server.
- **Heroku** for application hosting.

# 6. Testing

Manual testing covers the customer journey, navigation, card catalogue,
shopping bag, checkout, authentication, form validation, image loading,
resolution testing, mobile behavior, accessibility, and Lighthouse results.

The complete testing plan is available in [TEST.md](TEST.md).

# 7. Deployment

## How this project was deployed

This project was deployed to Heroku via the following steps:

### Initial Deployment

-   Navigate to [Heroku](https://www.heroku.com/).
-   [Log in](https://id.heroku.com/login) or [Sign
    Up](https://signup.heroku.com/) for an account.
    -   If Creating an account, select **Python** as the Primary development
        language.
    -   Activate the account via the confirmation email.
    -   Accept the Terms of Service.
-   Click on **Create new app**.
-   Enter a suitable **App Name** and **Region**.
-   Click **Create App**.
-   Under the **Deploy** tab, under the heading **Deployment Method**, click the
    **GitHub** icon, and proceed to click the button which states **Connect to
    GitHub**.
-   Enter your credentials for **GitHub.**
-   Search for the repository required (in this instance, **fasting_site**), and click
    **Connect.**

### Running this project locally

#### Cloning the Repository

1.  Visit the project’s [GitHub Repository](https://github.com/fadam430/db_card_shop).
2.  Click the "Code" dropdown box above the repository's file explorer.
3.  Under the "Clone" heading, click the "HTTPS" sub-heading.
4.  Click the clipboard icon, or manually copy the text presented:
    `https://github.com/fadam430/db_card_shop.git`
5.  Open your preferred IDE (VSCode, Atom, PyCharm, etc).
6.  Ensure your IDE has support for Git, or has the relevant Git extension.
7.  Open the terminal, and create a directory where you would like the
    Repository to be stored.
8.  Type git clone and paste the previously copied text
    (`https://github.com/fadam430/db_card_shop.git`) and press enter.
    -   If you would like to clone only the dev branch, please type git clone -b
        dev before the previously copied link to the repository.
9.  The Repository will then be cloned to your selected directory.

#### Manually Downloading the Repository

1.  Visit the project’s [GitHub Repository](https://github.com/fadam430/db_card_shop).
    -   Ensure you have selected the appropriate branch.
2.  Click the "Code" dropdown box above the repository's file explorer.
3.  Click the "Download ZIP" option; this will download a copy of the selected
    branch's repository as a zip file.
4.  Locate the ZIP file downloaded to your computer, and extract the ZIP to a
    designated folder which you would like the repository to be stored.

#### Opening the Repository

1.  Open your preferred IDE (VSCode, Atom, PyCharm, etc).
2.  Navigate to the chosen directory where the Repository was Cloned/Extracted.
3.  **Optional:** Create a new Python [Virtual
    Environment](https://docs.python.org/3/tutorial/venv.html)
4.  Type `pip install requirements.txt` to install all the required packages.
    -   If you intend to further develop the project, please use
        `requirements-dev.txt` as it includes additional packages specifically
        intended for a development environment, however, please do not use this
        for production.
5.  Type ` python manage.py migrate` in the terminal to migrate the database.
6.  Type `python manage.py loaddata codex.json` in the terminal to set up the
    immutable Codex dictionary.
7.  You will now be hosting the repository from your IDE.

---

# 8. Credits

## Readme
- CIRPG README structure and format served as the template for this documentation

## Content
- Dragon Ball Card Shop from my childhood memories when I collected many dragon ball cards and we just sell and swap between each others.

## Media
- All images downloaded this website.
- Images [here](https://mnacardz.com/)

## Code
- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/
- django-allauth Documentation: https://django-allauth.readthedocs.io/

---

# 9. Acknowledgements

I would like to thank you my Tutor Kevin 

# 10. Disclaimer

Dragon Ball Card Shop is an independent e-commerce project created for
educational and demonstration purposes. Product descriptions, images, prices,
and availability are provided for illustrative purposes and may change without
notice. Payment processing is handled through Stripe, and the project does not
store full payment card details.

Dragon Ball and related names, characters, and artwork are the property of
their respective rights holders. This project is not affiliated with or
endorsed by the official Dragon Ball brand or its rights holders.
