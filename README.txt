Daniel Garcia

ssh garciad@cis3210.socs.uoguelph.ca
flask run --host=0.0.0.0 --port=000000
mysql -h dursley.socs.uoguelph.ca -u garciad -p
	

Lab 1:
- Got Flask working and connected to the cis3210.socs.uoguelph.ca servers with unique port number
- Added some Bootstrap and jQuery libraries to add functionality to the page
- Added button functionality in which whenever it is clicked, Links the Cat appears with animations which is styled by Bootstrap

Lab 2:
- In Python code, imported the library request from flask
	- Made a new route with the url /users and methods GET, POST, DELETE, and PUT
	- Made if statements depending on the type of method being activated 
- In HTML
	- Made four different buttons for the each variant methods
- In JavaScript
	- Used jQuery.ajax() to the buttons on the client side to demonstrate that the request methods work

Lab 3:
- My application runs queries from databases using flask and jQuery.ajax()
	- To do so we use dursley.socs.uoguelph.ca as our host for the database 
	- I have an two input boxes that asks for username and password
		- These values are sent through request forms into flask
	- We have varios buttons that does tasks with the database:
		- Login (post and create/check):
			- Clicking on login button creates the username and password if it doesn't exists already
			- It also checks if the password from the input box matches the password in the database
		- Delete:
			- Deletes the users and passwords in the database
		- Update (put):
			- Updates the password of the user in the input box and sends the updated password to database
		- Get:
			- returns a string indicating a GET method

Lab 4:
- It did not say to submit a README.txt for lab 4 but I'll do one briefly:
	- Created a login button and successfully saves user session
	- Also enables a logout button and clears the user session
	- If user password is incorrect then puts the user back to login page
	

Lab 6:
- Used the API: http://api.openweathermap.org
- APP ID (API key): 0000000000000000000
- API returned a JSON of weather data. Then parsed it to get the most recent data.
	- Sent that data in JSON form to Javascript, dynamically in HTML
- Made a button that whenever it is clicked then javascript would extract the JSON data and place it in the specific HTML id tags. 

Lab 8:
- Used the API: http://api.openweathermap.org
- APP ID (API key): 0000000000000000000 
- API returned a JSON of weather data. Then parsed it to get the most recent data.
	- Sent that data in JSON form to Javascript, dynamically in HTML
- Made input box for city
	- User inputs what city weather they want to see and is displayed in a text box
	
Lab 9:
- Added more database functionality:
	- To save the cities that the user inputs to the text box and saving it to mysql
	- In addition, added the ability to delete the city through href link 
	- Made the page more visually pleasing
	
Lab 10:
- Finished the visual appearence of the webpage
- Google Chrome does not officially support Bootstrap so some bootstrap functions may not work in Google Chrome
- Overall the intended use of the webpage works as planned
