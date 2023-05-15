# JDA Restaurant

JDA Restaurant is an application for users/customers of JDA restaurant that could be used to book a table in the restaurant.

----

## Features

In this section, I will be going through the different parts of the website and I will provide descriptions for each feature and what the feature do. 

### Current Features

- _Make Reservation_
    - User can make a reservation by inputting their name, email, phone, date, time and the number of people.
    - User can only access the "Reserve" tab once they have logged in.

- _Display Reservation_
    - Once a user has successfully made a reservation, their reservation details will then be available in the "My Reservation" page which can be access from the navigation bar tab.
    - User can only access the "My Reservation" page once they have logged in.

- _Update Reservation_
    - User can update their reservation by clicking the "Change" button in the My Reservation page.

- _Delete Reservation_
    - User can delete their reservation by clicking the "Delete" button in the My Reservation page.

- _Admin Page_
    - Admin user can login into the admin page by adding /admin at the end of the jda restaurant url and by using the Username: adminuser and Password: jda123
    - Admin user can create, edit and delete a booking, table, user, etc. from the admin page.
    
- _Register User_
    - This is the page where a user can register and once they have completed their registration, user can then make a reservation
    - Sign up page will ask user for their username, email (optional) and password and user must input a valid username, email and password.
    - A user can only access this page by clicking the "Register" tab from the navigation bar and "Sign Up" button in the Login page or Index page.

- _Login User_
    - User can log in into the system through the log in page.
    - Log in page will ask for user's username and password, to login. User has to input their correct username and password they used when registering.
    - If a user is not yet logged in, the Login page can be access by a user in the "Login" tab from navigation bar or the "signin" link from the index page.
    - The log in page won't be available if the customer has already logged in.

- _Logout User_
    - A user can click the logout button from the navigation bar to logout.
    - Logout button is only available when a user is logged in.


### Future Development Plans
    - To add validations, for instance to make sure that user could not select past dates when making a booking or tables that are already booked should not be selected again, etc.
    - To update or fix the frontend to make the application look better.

### Known Issues

- Validations
    - Some functionalities does not have validations.

- Frontend/CSS
    - Frontend is not properly done and CSS is not reflecting in the frontend

- Missing functionalities
    - Other functionalities has not been applied or is not working

## Deployment

As I am using python and django for this project, this project is deployed in Heroku. The steps to deploy are as follows:
- Create new app in Heroku
- Set a unique name for the app and choose the region I am currently in
- In the settings tab, add the config vars and buildpacks required.
- In the deploy tab, connect Heroku app to github repository of where the project is stored
- Click on deploy

JDA Restaurant can be accessed through - https://jda-restaurant.herokuapp.com/

----

## Technologies Used

### IDE
- [GitPod](https://gitpod.io/)

### Languages and Frameworks/Resources
- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
- [HTML5](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [Bootstrap5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [JavaScript](https://www.javascript.com/)

### Project Management and Deployment
- [GitHub](https://github.com/)
- [Heroku](https://heroku.com/)

### Other
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [Fontawesome 6](https://fontawesome.com/)
- [Slack](https://slack.com/intl/en-ie/)
- [W3Schools](https://www.w3schools.com/)

----

## Credits

### Content
- To get more idea about the battle ship game I looked at the following:
    - [CodeInstitute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/a706dbb65b2d467a84e1bf67266851b1/)
    - [Python Django Project - Restaurant Table Reservation | Python Django Sqlite](https://www.youtube.com/watch?v=JlrT87wTrms&ab_channel=PankajPanjwani)
    - [StackOverFlow](https://stackoverflow.com/)
