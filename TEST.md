# Dragon Ball Card Shop - Manual Test Plan

## 1. Testing Summary

This document records manual testing for the Dragon Ball Card Shop website. It covers the main customer journey, navigation, shop and cart functions, authentication, checkout, image handling, responsive behaviour, resolution testing, and Lighthouse results.

Testing should be completed after deployment and repeated after significant code or configuration changes.

**Overall test status:** Not started  
**Test date:** 05/09/2026  
**Tester:** Adam Foldesi  
**Release/version:** 1.0

### Result key

| Result | Meaning |
| --- | --- |
| Pass | Works as expected with no visible issue |
| Fail | Does not meet the expected result |
| Blocked | Cannot be tested because of another issue |
| N/A | Not applicable to this test environment |

## 2. Test Environment

| Area | Details |
| --- | --- |
| Desktop operating system | Windows 10 |
| Mobile device or emulator | Samsung S25+ |
| Browser and version | Brave last version |
| Screen resolution tested | 1980X1020 |
| Network condition | Normal  |
| Test account | admin account |
| Test payment details | details in Stripe website and the About page |

## 3. Functional Testing

Record the result and any evidence for each test. Use the validation column for a short confirmation, such as an order number, visible message, or screenshot filename.

| ID | Test action | Expected result | Result | Validation / evidence |
| --- | --- | --- | --- | --- |
| F-01 | Open the home page | The page loads without errors and the header, navigation, content, and footer are visible | Pass |  |
| F-02 | Click the logo or Home link | The user is returned to the home page | Pass |  |
| F-03 | Click **Browse Cards**, **Shop Now**, or **Explore Cards** | The cards page opens | Pass |  |
| F-04 | Click the Cards navigation link | The cards page opens and the Cards link is shown as active | Pass |  |
| F-05 | View the cards page with available products | Cards show their image or fallback, name, category, description, price, and action button | Fail | card images not displayed |
| F-06 | View the cards page with no products | A clear empty-state message is displayed instead of a blank area | Pass |  |
| F-07 | Click **Add** while signed in | The selected card is added to the bag and the user receives clear feedback | Pass |  |
| F-08 | Click **Add** while signed out | The user is directed to the login page or shown an appropriate authentication prompt | Pass |  |
| F-09 | Open the shopping bag/cart | The bag shows the selected product, quantity, price, subtotal, and available actions | Pass |  |
| F-10 | Increase and decrease item quantity | Quantity and totals update correctly | Pass |  |
| F-11 | Remove an item from the bag | The item is removed and totals update correctly | Pass |  |
| F-12 | Open the checkout page with a valid bag | Checkout loads with the correct order summary and required fields | Pass |  |
| F-13 | Submit checkout with valid details | Payment/order processing completes and a success page or confirmation is shown | Pass |  |
| F-14 | Submit checkout with missing or invalid details | Validation messages identify the fields that need correction | Pass |  |
| F-15 | Use the About navigation link | The About page opens and its content is readable | Pass |  |
| F-16 | Open the login page | Login form loads and accepts valid credentials | Pass |  |
| F-17 | Submit invalid login details | A clear error is shown and the user remains on the login page | Pass |  |
| F-18 | Log out | The user is logged out and guest actions are displayed | Pass |  |
| F-19 | Use the registration link | Registration page opens and required fields are validated | Pass |  |
| F-20 | Open product images | Images load from the configured storage location without broken-image icons | Fail | images is not load even its in the right folder and place need to find out what cose the problem |
| F-21 | Open the site favicon and static assets | CSS, JavaScript, fonts, and favicon load successfully | Pass |  |
| F-22 | Refresh each main page | The page remains available and does not lose the current valid session unexpectedly | Pass |  |
| F-23 | Use browser Back and Forward buttons | Navigation behaves predictably without duplicate submissions | Pass |  |
| F-24 | Open an unknown URL | A suitable 404 page or response is returned | Pass |  |

## 4. Form and Input Validation

| ID | Validation check | Expected result | Result | Validation / evidence |
| --- | --- | --- | --- | --- |
| V-01 | Leave each required field empty | The field is rejected with a useful validation message | Pass |  |
| V-02 | Enter an invalid email address | The email field is rejected | Pass |  |
| V-03 | Enter values containing spaces or leading/trailing whitespace | Values are handled consistently and safely | Pass |  |
| V-04 | Enter unusually long text | The application prevents invalid data or handles it without layout damage | Pass |  |
| V-05 | Enter invalid numeric values for quantity or payment-related fields | Invalid values are rejected and no incorrect total is created | Pass |  |
| V-06 | Submit a form more than once | Duplicate orders or duplicate actions are prevented where applicable | Pass |  |
| V-07 | Trigger a validation error, correct it, and resubmit | The corrected form submits successfully | Pass |  |

## 5. Resolution Testing

Check layout, text, images, navigation, buttons, forms, and footer at each resolution. Confirm that no content is clipped, overlapped, or forced outside the viewport.

| Resolution | Device type | Layout result | Result | Validation / screenshot |
| --- | --- | --- | --- | --- |
| 320 x 568 | Small mobile | in browser dev tools | Pass | no picture validation |
| 375 x 667 | Mobile | in browser dev tools | Pass | no picture validation |
| 390 x 844 | Modern mobile | samsung s25+ | Pass | no picture validation |
| 768 x 1024 | Tablet portrait |in browser dev tools | Pass | no picture validation |
| 1024 x 768 | Tablet landscape / small desktop | in browser dev tools | Pass | no picture validation |
| 1280 x 720 | Desktop | in browser dev tools | Pass | no picture validation |
| 1366 x 768 | Common desktop | in browser dev tools | Pass | no picture validation |
| 1920 x 1080 | Large desktop | asus rog laptop | Pass | no picture validation |

### Resolution checklist

- [ ] Navigation collapses and expands correctly on small screens.
- [ ] Card columns resize without overlapping or unexpected horizontal scrolling.
- [ ] Product images keep a consistent, usable aspect ratio.
- [ ] Buttons remain visible, clickable, and fully readable.
- [ ] Text fits within its containers and does not overlap other content.
- [ ] Checkout fields and order summaries remain usable.
- [ ] Footer content remains accessible at all tested sizes.

## 6. Mobile Version Testing

Test using at one Android device.

| ID | Mobile test | Expected result | Result | Validation / evidence |
| --- | --- | --- | --- | --- |
| M-01 | Load the home page on mobile | Page loads correctly without horizontal scrolling | Pass |  |
| M-02 | Open and close the mobile navigation menu | Menu opens, links are readable, and it closes after selecting a link | Pass |  |
| M-03 | Tap the card action button | The button responds on the first tap and gives clear feedback | Pass |  |
| M-04 | Scroll through the cards page | Cards and images load correctly while scrolling | Pass |  |
| M-05 | Use the bag and checkout on mobile | Cart totals, fields, buttons, and order summary are usable | Pass |  |
| M-06 | Rotate the device | Layout adapts correctly between portrait and landscape | Pass |  |
| M-07 | Use mobile keyboard in forms | Focused fields remain visible and the keyboard does not hide the submit action | Pass |  |
| M-08 | Test on a slower connection | Loading states and errors are understandable; the page remains usable | Pass |  |
| M-09 | Tap links and buttons near the screen edge | Controls have enough touch area and do not trigger an adjacent action | Pass |  |
| M-10 | Check image loading on mobile data | Images load at an acceptable speed without breaking the layout | Fail | images still need to check the problem |

## 7. Accessibility and Usability Checks

| ID | Check | Expected result | Result | Validation / evidence |
| --- | --- | --- | --- | --- |
| A-01 | Navigate using only the keyboard | All interactive controls can receive focus and be used | Pass |  |
| A-02 | Check visible focus indicators | The focused control is clearly visible | Pass |  |
| A-03 | Inspect image alternative text | Meaningful images have useful alt text; decorative images are handled appropriately | Pass |  |
| A-04 | Check heading order and page titles | Headings and titles describe the current page clearly | Pass |  |
| A-05 | Check color contrast and readable text | Text and controls remain legible | Pass |  |
| A-06 | Test error messages | Errors are clear and associated with the relevant field or action | Pass |  |

## 8. Lighthouse Testing


### Lighthouse screenshots

Add screenshots or links to the reports below. Include the URL and date for each capture.

**Home - Mobile**  
Screenshot: [home](/media/lighthouse/homapagemobile.PNG)  
Notes: Mobile lighthouse has a very bad score. I don't know it the website problem or was something bad in the lighthouse. Other pages not get this bed score.
**Home - Desktop**  
Screenshot: [home](/media/lighthouse/homapagedesktop.PNG) 
Notes: This get better score than mobile version. This page its still has problem some javascript loading and picture loading problem.

**Cards - Mobile**  
Screenshot: [cards](/media/lighthouse/cardpagemobile.PNG)  
Notes: no extra comment here card size right 

**Cards - Desktop**  
Screenshot: [cards](/media/lighthouse/cardpagedesktop.PNG)  
Notes: cards and animations of the working images not shown. 

**About - Mobile**  
Screenshot: [about](/media/lighthouse/aboutpagemobil.PNG)  
Notes: this working well no any issues this page 

**About - Desktop**  
Screenshot: [about](/media/lighthouse/aboutpagedesktop.PNG)  
Notes: no any issues

## 9. Significant Issues Log

Record issues that affect functionality, data, security, accessibility, performance, or the customer journey. Priorities issues before release.

| Issue  | Date | Test | Description and steps to reproduce | Severity | Expected / actual result | Status | Screenshot or reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| no images shown in card shop page | 07/09/2026 | open the page and no images shown | I try to change name of the folder where is the files. I checked the aws s3 bucket images shown there as well. Somehow in he website is not shown. | Critical |  | Open  | no screenshot needed |


## 10. Final Test Summary

| Category | Passed | Failed | Blocked | N/A | Notes |
| --- | ---: | ---: | ---: | ---: | --- |
| Functional testing | Pass |  |  |  |  |
| Validation testing | Pass |  |  |  |  |
| Resolution testing | Pass |  |  |  |  |
| Mobile testing | Pass |  |  |  |  |
| Accessibility checks | Pass |  |  |  |  |
| Lighthouse testing | Pass |  |  |  | but mobil version in the home page is bit weird numbers |

**Release recommendation:**  Approved with known issues  
**Outstanding significant issues:** in card shop don't show the cards images  

