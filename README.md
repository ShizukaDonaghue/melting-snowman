# The Melting Snowman Game
## Deployed Website

## Repository

## UX & Design

## Features

## Technologies Used

## Testing

## Deployment
This application has been deployed using [Heroku](https://dashboard.heroku.com/).
The steps for deploying the application is as follows:

Preparation:
1. In order for input method to work correctly in the terminal, add a new line character at the end of each text inside the input method so that the input request will be displayed in the terminal.
2. If there are dependencies to run the application on [Heroku](https://dashboard.heroku.com/), run "pip3 freeze > requirements.txt" command which will update "requirements.txt" file to include those dependencies. 
3. Push all updates to GitHub.

Deployment to Heroku:
1. Log into [Heroku](https://dashboard.heroku.com/) website.
2. Click on "New" and then select "Create new app."
<img src="docs/heroku-create-new-app.png" width="500">
3. Assign a name for the application, select the region and click on "Create app.
<img src="docs/heroku-create-app-name.png" width="500">
4. Go to "Settings" and click on "Reveal config Vars."
<img src="docs/heroku-settings-config.png" width="500">
5. Add config vars necessary to run the application. For this application, key "PORT" and value "8000" are required.  
<img src="docs/heroku-config-var.png" width="500">
6. Scroll down to "Buildpacks" and click on "Add buildpack."
<img src="docs/heroku-buildpack.png" width="500">
7. Add buildpacks required to run the application. For this application, "Python" and 
<img src="docs/heroku-add-python.png" width="500">
<img src="docs/heroku-add-nodejs.png" width="500">  
"Nodejs" are required. Add "Python" first and then "Nodejs" so that they are added in this order.  
<img src="docs/heroku-buildpacks-order.png" width="500">
8. Select "Deploy" from the menu at the top. 
9. Under "Deployment method," select "GitHub."
10. Under "Connect to GitHub," search for the repository to connect to.
11. Once the respository is found, click on "Connect."
<img src="docs/heroku-deploy.png" width="500">
12. Select either "Enable Automatic Deploys" which will deploy a new version of the application every time changes are pushed to GitHub or opt for "Manual Deploy."
<img src="docs/heroku-auto-or-manual-deploy.png" width="500">
13. Once the application is deployed, scroll back to the top and click on "Open app."  
<img src="docs/heroku-open-app.png" width="500">







## Credits
* Placeholder for displaying correctly guesssed letters

## Acknowledgements



