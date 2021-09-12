# AlmaBulletin
A web app for sharing posts, updates, etc. by students and professors on a common platform. Created with Python (Flask), HTML, CSS, SQLite, it has been dockerised and deployed on Amazon EC2 Instance. 

URL: http://ec2-18-224-150-187.us-east-2.compute.amazonaws.com:5001/

Instructions to run locally:
* Clone the repository
* Make sure you have Python3 installed. Install all the modules in requirements.txt
* In __init__.py, configure your email and passwords accordingly for your smtp ports. Also change your host and port details as per your wish.
* Run 'python run.py' from the command line.
* Go to localhost:5001
* Voila! Have fun with the project.

In case you want to remove all dummy entries from the sqlite.db, recreate it again. (Check documentation for the same)

To run as a Docker image, 
* First install Docker (and Docker-compose, if using Linux). 
* Inside the project directory, from the command line first run 'docker-compose build'
* Then run 'docker-compose up' or 'docker-compose -d' for detached run.
* Go to the 'webserver-host:port' (domain-name:5001) and voila! You are good to go.
