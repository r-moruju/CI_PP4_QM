# Quick MOT 


**Developer: Razvan Moruju**

💻 [Visit live website](https://quick-mot.herokuapp.com/)

![Mockup image](docs/home-page.png)

## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
      - [Diagram](#diagram)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Testing](#testing)
    - [Manual testing of user stories](#manual-testing-of-user-stories)
    - [Performing tests on various devices](#performing-tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Configuration](#configuration)
    - [Heroku](#heroku)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
  - [Credits](#credits)

  ### About

The Quick MOT is an application where users can book their car MOT test.

### User Goals

- Be able to book a MOT test
- Be able to amend MOT test date
- View the their upcoming MOT booking dates

### Site Owner Goals

- Provide an online solution for users to book a MOT test
- Create visually appealing design
- Provide fully responsive application with straightforward navigation

## User Experience

### Target Audience
- People who want to get their cars MOT test done
- People who want to book a MOT test in advance
- People who want to keep track of their upcoming MOT test 


### User Requirements and Expectations

- Straightforward navigation
- Easy to use
- A responsive application that allows the user to access it on any device
- Visually appealing design for all screen size
- Links and functions that work as expected
- Accessibility

##### Back to [top](#table-of-contents)

## User Stories

### Users

1.	I want to see the home page with explanation of the app
2.	I want to be able to easily navigate around the application to different pages
3.	I want to create my account to be able to book MOT tests
4.	I want to be able to edit my current booking date
5.	I want to delete my booking if no longer needed
6.	I want to see feedback messages so that I know that my booking was created, edited or deleted
7.	As a returning user, I want to log in to the app to see my current bookings
8.  I want to be able to log out from my account


### Site Owner
9.	I want only the logged-in users to be able to create a booking
10.	I want users to be able to create a booking on any day that suits their needs
11.	I want users to be able to rate our service
12.	I want my site to be fully responsive


##### Back to [top](#table-of-contents)

## Design

The application is based on a Bootstrap theme (Small Business)[https://startbootstrap.com/template/small-business]

### Structure

#### Website pages

Simplicity, clarity and ease of navigation between pages were the key aspects for design of this website's structure.

At the top of the page there is a recognisable type of navigation bar with website name on the left side and the navigation links to the right which collapses to hamburger icon on smaller screen sizes.

- The website consists of the following sections:
  - Home page with an overview of the content and aim of the website.
  - Add car reg number allowing user to enter a car registration number.
  - View car details where user can see details about the car and confirm if is the right car.
  - Add booking where users can select a booking data.
  - Edit booking where user cand change the booking date.
  - Login page for returning user to log in.
  - Register page allowing a new user to sign up.
  - Logout page allowing user to log out of the website.

#### Database

- The backend consists of Python built with the Django framework with a database of a Postgres for the deployed version

The following models were created to represent the database model structure for the website:

##### User Model
- The User model contains information about the user. It is part of the Django allauth library

##### Car Model
- The Car model contains various fields populated by the API with car information
- Contains 'booked' boolean field to check if the car is currently booked
- The model has a many to one relationship with User so User can have multiple cars

##### Booking Model
- The Booking model contains 'date' and 'create_on' fields
- Has ForeignKey for User and Car
- The model has a many to one relationship with User so User can have multiple bookings

##### Site Model
- A simple model designed to store average rating
- Can only be accessed from admin panel for one time creation

##### Rating Model
- Designed to store User rating for the Site

#### Diagram

<details><summary>My own diagram created on https://lucid.co/</summary>
<img src="docs/my-diagram.png">
</details>
<details><summary>Exported database diagrams (ERD) from Django</summary>
<img src="docs/diagram.png">
</details>

## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python 3.10.9
- Django 3.2.16

### Libraries & Tools

- [Bootstrap](https://getbootstrap.com/). This project uses the Bootstrap library for UI components
- [Cloudinary](https://cloudinary.com/) to store static files
- [Favicon.io](https://favicon.io) for making the site favicon
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/) was used for debugging of the code and checking site for responsiveness
- [Font Awesome](https://fontawesome.com/) - Icons from Font Awesome were used throughout the site
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Heroku](https://www.heroku.com/) was used to deploy the project into live environment
- [ElephantSQL](https://www.elephantsql.com/) – to host a Postgres database
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/) - code editor used to write this project
- [Vehicle Enquiry Service (VES) API](https://developer-portal.driver-vehicle-licensing.api.gov.uk/). To access vehicle details.

##### Back to [top](#table-of-contents)

## Features

### Logo and Navigation Bar
- Featured and consistent on the all pages
- The nav bar contains links to Home page, Login page or Logout page.
  - Logged-in users will see their name in the nav bar
  - Not logged in users will have option to log in and register
- The nav bar is fully responsive and changes to a toggler (hamburger menu) on smaller size screens
- User stories covered: 2, 12

<details><summary>See feature images</summary>

![Logo and navbar](docs/features/nav-bar-full.png)
![Logo and navbar](docs/features/nav-bar-full-out.png)
![Logo and navbar](docs/features/nav-bar-burger.png)
![Logo and navbar](docs/features/nav-bar-burger-expand.png)
</details>

### Home page
- Home page includes nav bar, main body and a footer
- Home page Heading Row includes description of the website and what its users can find and expect.
- User stories covered: 1

<details><summary>See feature images</summary>

![Home page](docs/features/home.png)
</details>

### Sign up / Register
- New users can create an account
- The user must provide a valid username, password and password confirmation. Email address is optional
- User cannot register the same details twice for an account
- Once register the users are immediately logged in and taken to the home page
- User stories covered: 3

<details><summary>See feature images</summary>

![Register](docs/features/register.png)
</details>

### Login
- Returning users can login to their account
- The user must have an account in the system and they must enter the correct username and password
- Both fields are mandatory
- Once logged in the user will be navigated to the home page
- User stories covered: 7, 10

<details><summary>See feature images</summary>

![Login](docs/features/login.png)
</details>

### Logout
- Confirmation screen for Logged in user to logout from their account 
- User stories covered: 8

<details><summary>See feature images</summary>

![Logout](docs/features/logout.png)
</details>

### Add car-reg/confirm-car/select-date
- Succession of screens where user can create a booking 
- User stories covered: 9, 10

<details><summary>See feature images</summary>

![Add car-reg/confirm-car/select-date](docs/features/car-reg.png)
![Add car-reg/confirm-car/select-date](docs/features/car-confirm.png)
![Add car-reg/confirm-car/select-date](docs/features/select-date.png)
</details>

### Edit Booking
- Screen where user can change booking date 
- User stories covered: 4

<details><summary>See feature images</summary>

![Edit Booking](docs/features/change-date.png)
</details>

### Delete Booking
- Button for deleting a booking
- A js confirm message is used, for user to confirm the deletion 
- User stories covered: 5

<details><summary>See feature images</summary>

![Delete Booking](docs/features/delete-1.png)
![Delete Booking](docs/features/delete-2.png)
</details>

### Bookings Carousel
- Bootstrap card where current bookings are displayed for logged in users.  
- User stories covered: 7

<details><summary>See feature images</summary>

![Bookings Carousel](docs/features/delete-1.png)
</details>

### Feedback Messages
- Django messages displayed to user, to confirm different app operations.
- User stories covered: 6

<details><summary>See feature images</summary>

![Feedback Messages](docs/features/delete-success.png)
![Feedback Messages](docs/features/booked-success.png)
![Feedback Messages](docs/features/change-success.png)
</details>

### Rating
- Bootstrap card where user can give a rating and see average rating.  
- User stories covered: 11

<details><summary>See feature images</summary>

![rating](docs/features/rating.png)
</details>

## Testing

### Manual testing of user stories

1. I want to see the home page with explanation of the app

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to https://quick-mot.herokuapp.com/ | Home page main body loads with application description | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/home.png">
</details>


2. I want to be able to easily navigate around the application to different pages

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click on 'Home' link on the navigation bar | Loads home page | Works as expected |
Click on 'Register' link on the navigation bar | Loads Sign UP page | Works as expected |
Click on 'Login' link on the navigation bar | Loads Login page | Works as expected |
Click on 'Logout' link on the navigation bar | Loads Logout page | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/home-link.png">
<img src="docs/testing/register-link.png">
<img src="docs/testing/register.png">
<img src="docs/testing/login-link.png">
<img src="docs/testing/login.png">
<img src="docs/testing/logout-link.png">
<img src="docs/testing/logout.png">
</details>

3. I want to create my account to be able to book MOT tests

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click 'Register' from the menu | Loads Registration page | Works as expected |
Fill up the form | Returns errors if input fails validation | Works as expected |
Click 'Sign UP' button at the bottom of the form | User is logged-in, taken to home page and presented with a confirmation message | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/register-link.png">
<img src="docs/testing/register.png">
<img src="docs/testing/register-form-error.png">
<img src="docs/testing/register-message.png">
</details>

4. I want to be able to edit my current booking date

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
From the 'Your Bookings' card click 'Change Date' | Loads Change date page | Works as expected |
Edit the date and click on 'Confirm' button | Loads home page and displays confirmation message | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/change-date-button.png">
<img src="docs/testing/change-date-page.png">
<img src="docs/testing/change-date-message.png">
</details>


5. I want to delete my booking if no longer needed

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
From the 'Your Bookings' card click 'Cancel' | The confirmation message appears | Works as expected |
Click 'Ok' button to confirm deletion | Loads home page and displays confirmation message | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/cancel.png">
<img src="docs/testing/cancel-confirm.png">
<img src="docs/testing/cancel-message.png">
</details>

6. I want to see feedback messages so that I know that my booking was created, edited or deleted

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
After each backend operation | The feedback message appears | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/cancel-message.png">
<img src="docs/testing/change-date-message.png">
<img src="docs/testing/register-message.png">
<img src="docs/testing/booked-success.png">
</details>

7. As a returning user, I want to log in to the app to see my current bookings

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click 'Login' from nav bar | Loads Login page | Works as expected |
Enter login credentials and click 'Sign In' | Loads home page, and 'Your Bookings' card gets populated with your bookings | Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/testing/login-link.png">
<img src="docs/testing/login.png">
<img src="docs/testing/bookings-card.png">
</details>

8. I want to be able to log out from my account

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Click 'Logout' from nav bar | Loads Logout page | Works as expected |
Click 'Sign Out' button | Loads home page, and show feedback message | Works as expected |
<details><summary>Screenshot</summary>
<img src="docs/testing/logout-link.png">
<img src="docs/testing/logout.png">
<img src="docs/testing/signout-message.png">
</details>

9. I want only the logged-in users to be able to create a booking

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
On the home page | For not logged-in users displays an 'Register' button, insted of an 'Book MOT Test' button | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/not-login-user.png">
<img src="docs/testing/not-not-login.png">
</details>

10. I want users to be able to create a booking on any day that suits their needs

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
On the home page click on 'Book MOT Test' button | Loads 'add_car_reg' page | Works as expected |
Add car registration and click 'Submit' | Loads 'confirm_car' page | Works as expected |
Click 'Confirm' | Loads 'add_booking' page | Works as expected |
Select date and click 'Confirm' | Loads home page, show feedback message, 'Your Bookings' card gets populated with the new booking | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/not-not-login.png">
<img src="docs/testing/add-car-reg.png">
<img src="docs/testing/confirm-car.png">
<img src="docs/testing/add-booking.png">
<img src="docs/testing/booked-success.png">
<img src="docs/testing/bookings-card.png">
</details>

11. I want users to be able to rate our service

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
User can give a rating on the 'Service Rating' card | Average rating gets calculated and saved | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/rating-card.png">
<img src="docs/testing/up-rating.png">
</details>


12. I want my site to be fully responsive

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Change device screen size using chrome dev tools | The web functionality remains the same on various screen sizes | Works as expected |

<details><summary>Screenshot</summary>
<img src="docs/testing/tablet.png">
<img src="docs/testing/desktop.png">
<img src="docs/testing/phone.png">
</details>

### Performing tests on various devices

The website was tested using Google Chrome Developer Tools Toggle Device Toolbar to simulate viewports of different devices.

### Browser compatibility

- Testing has been carried out on the following browsers:
  - Googe Chrome
  - Firefox Browser
  - Microsoft Edge

##### Back to [top](#table-of-contents)

## Configuration

### Heroku
This application has been deployed from GitHub to Heroku by following the steps:

1. Create or log in to your account at heroku.com
2. Create a new app, add a unique app name (this project is named "quick-mot") and choose your region
3. Click on create app
4. Go to "Settings" tab
5. Under Config Vars store any sensitive data you saved in env.py file. Also add another config var with key 'PORT' and value '8000'.
6. Go to "Deploy" tab and select "GitHub" in "Deployment method"
7. To link up your Heroku app to our Github repository code enter your repository name, click 'Search' and then 'Connect' when it shows below
8. Choose the branch you want to buid your app from
9. If prefered, click on "Enable Automatic Deploys", which keeps the app up to date with your GitHub repository
10. Wait for the app to build. Once ready you will see the “App was successfully deployed” message and a 'View' button to take you to your deployed link.

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open commandline interface on your computer
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard 
  ```
  $ git clone https://github.com/r-moruju/CI_PP4_QM.git
  ```
7. Press Enter to create your local clone

##### Back to [top](#table-of-contents)

## Credits

### Code

How to implement a rating mechanism in Django : https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c