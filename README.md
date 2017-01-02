# FB CHAT BOT
This repo is basically to learn and test fb bot and google cloud apis development

##Getting Started
This tutorial will teach you how to create facbook bot integrate it with google cloud api and deploy it over heroku
###Pre-requisites

This tutorial assumes you have a working knowledge of python and have python 2.7.xx installed on your system
It also requires github binary installed on your system

###Step 1: Clone git hub repostiory
```
git clone https://github.com/sameepsi/fbbot_vision.git
```
###Step 2: Setup Heroku environment

1.Install [Heroku](https://devcenter.heroku.com/articles/heroku-cli/)

2.Goto the git repo path you just cloned and run

3.pip install -r requirements.txt

4.Create heroku login credentials and then run following command

5.heroku login

6.heroku create- it will create a new application for you 

7.git push heroku master

8.heroku open

9.Copy the url in the browser tab just opened and keep it safe for now.

###STEP 3: Setup facebook app

1.Create a [facebook page](https://www.facebook.com/pages/create/)

2.Create a [facebook app](https://developers.facebook.com/quickstarts/?platform=web)- Click on "skip and create" and create a facebook app
for you page

![create fb image](https://github.com/sameepsi/fbbot_vision/blob/master/images/create_fb_app.png.png)

3.In next dialog scroll down and click on get started next to "Messenger Platform"

![setup messenger](https://github.com/sameepsi/fbbot_vision/blob/master/images/setup-fb-messenger-app.png)

4.Generate a page access token- Now you’re in the Messenger settings for your Facebook App. Using the Page you created earlier (or an existing Page), click through
the auth flow and you’ll receive a Page Access Token for your app.

![auth-token](https://github.com/sameepsi/fbbot_vision/blob/master/images/page-access-token-generation.png)

5.Click on the Page Access Token to copy it to your clipboard.

6.Login into your [heroku dashboard](https://dashboard.heroku.com/apps) and click on the app you just created.

7.Goto settings and click on "Reveal Config Vars"

![heroku-app-env-vars](https://github.com/sameepsi/fbbot_vision/blob/master/images/config.png)

8.Enter- key="PAGE_ACCESS_TOKEN" and value="$The value you copied in step 4"

9.Enter -key="VERIFY_TOKEN" and value="any random value". Keep this random value with you- It will help in verifying webhook

###STEP 4: Setup webhook

1.Goto your developer dashboard on [facebook](https://developers.facebook.com/) and select your app

2.Click on "Add Product" in left menu panel

3.Click on "Get Started" next to webhooks

4.Click on New Subscription->Page

![page sub](https://github.com/sameepsi/fbbot_vision/blob/master/images/webhoob.png)

5.Fill following details

* CALLBACK URL-The Heroku (or other) URL that we setup earlier
* Verification Token- The value of the key that we setup in heroku with key "VERIFY_TOKEN"
* Subscriotion field- messages

6. Subscribe specific page to the webhook just configured

![page subs](https://github.com/sameepsi/fbbot_vision/blob/master/images/subscribe-to-page.png)

###STEP 5: Setup Google Cloud Platform

1.Sign-up for google-cloud-platform- Don't worry they won't charge you anything for doing this

2.Click on create project- And create the project with the name of your choice

![create-google-project](https://github.com/sameepsi/fbbot_vision/blob/master/images/google-cloud.png)

3.Now you need to enable the Vision API- To do so go to the main menu on the top left in the cloud console and click on API Manager

![API MANAGER](https://github.com/sameepsi/fbbot_vision/blob/master/images/APIMANAGER.png)

4.In the search bar, enter 'Cloud Vision' and it will display the Google Cloud Vision API in the list.

5.Select it and then click on Enable

5.Create service account to access REST API from outside

6.From the API Manager menu click on Credentials and then on Create Credentials.

7.Select Service Account Key from the options.

8.Then from the drop down options select new service account and click on create

![service-account-create](https://github.com/sameepsi/fbbot_vision/blob/master/images/service-account.png)

9.Enter the service account name and select the ROLE as PROJECT OWNER

10.Click on Create. It will download a JSON File, make sure that you save it at some safe place.

11.Goto heroku dashboard->Your app->Settings->Reveal Config vars

12.Enter key='GOOGLE_CLOUD_CREDENTIALS' value='$Copy the content of json file downloaded in previous step and paste it here'

Now you are ready to test your app.

Make sure the user who will be chatting with your bot is added with tester role in your facebook app's dashboard. This needs to be done since 
your facebook app is not reviewed so far.

Your suggestions and contributions and heartly welcome

Happy Chatting!!!
