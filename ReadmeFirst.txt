This contains all the rules and instructions of running all the applications in these assignment.

******* SETTING UP THE ENVIRONMENT **************
You will need to install Nodejs, npm, bower, polymer-cli and Python on your local machine.
1. Download Nodejs and set it up in the system. Ensure that the path environment variable or system environment variables point to the folder where npm has been installed 
e.g C:\Users\MCR\AppData\Roaming\npm
2. Download Python latest stable version and install it. Ensure the path environment variable or system environment variable points to the folder where python has been installed 
e.g C:\Python27
NOTE Setting up the environment variables will ensure that we can run the relevant commands node, polymer, python from the commandline without a problem. If you setup an environment variable and 
the command prompt is open you will need to close and open it again for the changes to take effect.
3. Install the rest of the applications as follows
	1. Install Bower with npm; type npm install -g bower on the commandline without the quotes and press enter
	2. Install Polymer-cli with npm;  type "npm install -g polymer-cli" on the commandline without the quotes and press enter
	3. Install latest Polymer 2.0 release with bower; type "bower install Polymer/polymer#^2.0.0" without the quotes on commandline and press enter


Section A Question 1.
1. Unzip the project files and copy "Section A Q1" folder to a location of choice
2. Navigate to the Section A Q1 folder from the commandline and type "bower install" to install necessary Polymer dependencies which will be read from the bower.json file
2. Once successfully installed type "polymer serve". This will run the application on a local server that will enable you view the results through the browser.
3. Go to the browser and type http://localhost:8081/ you should be able to see the sorted dictionary.
4. The source code is in src/data-display.html

Question 3
Please find the example scripts in the Section A Question 3 folder.
run the scripts as follows
1. Navigate to Section A Q3 on the commandline and once inside there type python followed by the filename to see results e.g. python hashing.py

Section B Question 1
1. Unzip the folder "Section B Q1" folder to a location of choice. Inside the folder you will find a client and a server folder. The client folder contains the client interface and login
controls. The server folder contains implementation of a server in Nodejs which adds new users and facilitates login/logout of users into the system.
2. Copy both folders to a location of choice in the machine.
3. Navigate to the server folder on the commandline and type "npm install" which installs all the dependencies and packages and then "node server.js" which runs the server application. Server application will be ready for login and creating of a new user.
4. Navigate to the client folder and on the commandline type "bower install" which installs necessary Polymer dependencies and thereafter type "polymer serve" which makes the client side of the application ready for opening. You will now be able to open the application by typing localhost:8081 on your browser.
5. Try to login to the application using any credentials. Create an account and try to login with the credentials created into the system.
