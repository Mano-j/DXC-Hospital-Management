# Hospital-Management-WebApp

## Requirements
The following are the requirements for running the Hospital Mangement Application.

### Python 3.7
Python is required to run the Django framework.
- For Windows:
    You can download it from [here](https://www.python.org/downloads/windows/ "Python for Windows")
    
- For Linux/MacOS
    Python comes installed out of the box with the OS.

### Django v2.2

The application is built on the Django framework to handle all of the application's backend tasks.<br><br>
You can install the Django framework by simply running `pip install django`.<br><br>
You can refer to [this article](https://www.makeuseof.com/tag/install-pip-for-python/ "Installing pip") to know how to install pip

### Python packages required

The one extra python package required is `django-crispy-forms`.
You can install it via `pip` too as shown below.
```
pip install django-crispy-forms
```

## Running the application

Running the Hospital Management application is fairly straight forward.
- Open a terminal/cmd window and navigate to the project folder.
- run the following:
```
python manage.py runserver 8080
```
- Once the server fires up, go to a browser and enter `localhost:8080/` or `127.0.0.1:8080/` in the address bar.
- Welcome to the Hospital Management Application!

## Database

The database used with the current version of the application is SQLite for portability. <br>Kindly skip the MYSQL integration section if you're not going to use this in production. SQLite will do fine for now.

When deploying to a production environment, it has to be ensured that the DB is changed to something that is suited for it. We have tested with MySQL and recommend it for this application.
Please refer the following guides for installation of MySQL
    - [Windows](https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html "Install MySQL on Windows")
    - [macOS](https://dev.mysql.com/doc/refman/8.0/en/osx-installation.html "Install MySQL on macOS")
    - [Linux](https://www.digitalocean.com/community/tutorials/how-to-install-the-latest-mysql-on-ubuntu-18-04#step-2-%E2%80%94-installing-mysql "Install MySQL on Linux(Ubuntu 18.04)")

#### Steps to integrate MySQL with the Hospital Management application:

1. Install the `mysqlclient` python package via pip.
    ```
    pip install mysqlclient
    ```
2. Create a new database called `hospital` in MySQL.
    ```
    mysql> CREATE DATABASE hospital
    ```
3. Create a new user by running the following command.
    ```
    mysql> CREATE USER 'hospadmin'@'localhost' IDENTIFIED BY 'password';
    ```
   Ensure you give`hospadmin` all privileges to the `hospital` database.
   ```
   mysql> GRANT ALL PRIVILEGES ON hospital TO 'hospadmin'@'localhost';
   ```
4. Now navigate to `settings.py` inside HospManagement directory in the project directory. There scroll to line 94 where you'll find the `DATABASES` section.
    Here, comment the first two lines inside the `default` block and uncomment the rest of the lines in it which specifies that the connection backend is MySQL, name of the db, username, password and the host url of your MySQL database.
    Note: Leave it as localhost if the MySQL database has been setup locally. In case it is set up in a remote server, please execute all the above steps in the remote server and replace `localhost` with the address to your remote MySQL server.
    
You can find detailed tutorials for performing the integration of MySQL with Django [here for Linux](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database "Integrate MySQL DB with Django in Linux(Ubuntu 18.04)") and [here for Windows](https://medium.com/@bencleary/django-mysql-for-windows-528272b3169b "Integrate MySQL DB with Django in Windows")

## Features
### Homepage
- The receptionist can add the patient details in the index page. 
- The details of the patients assigned with doctor for the current session is shown in the index page. This is shown only for the current day as to look clean.
- These details are updated after the page is refreshed or another patient is submitted.

### Assigining Doctors (Automatic)
- The background scheduling process schedules the patients to the doctors based in their availability. If the doctors are not available the are put into an waiting queue.
- The patients in the queue are alloted doctors once a doctor finishes his scheduled appointment with the current patient he is handling.
- The patients allotment is done with priority assigned to the patients based on their health status.
- Depending on the type of the case (Emergency, Urgent, Normal) the patients in the queue are alloted doctors.
- The heirarchy of priority is Emergency > Urgent > Normal cases.

### Direct Doctor assignment (Manual)
- The receptionist can assign a patient to a doctor of their preference based on their past experience with the doctor or from the word of a trusted friend.
- This feature is also under development and as of now when patient details are submitted via this form it is fed into automatic scheduling background process.

### Doctor Login page
- The doctors can login into their accounts and view the details of past and current patients. 
- There is an button in their page which allows them to turn off the patient assignment to them. This feature can be used when the doctor is having his lunch or unavailble for service due to his personal reasons.

### Staff Login Page
- Authorised hospital staffs can login into this page and view all the details of the patient assigninment.
- This feature is currently under development and cannot be used as of now.

### Admin Login page
- From this page the hospital admin can perform Create, Read, Update, Delete ( CRUD ) operations.
- The admin can add/delete/modify both Doctor and Patient details from here.
- He/She can add new doctors in the Doctor details section.
- Login access for new doctors can be created in the users section.
- If a doctor leaves the organisation the admin can remove his details from the DB.

### Security
- All passwords of user accounts are hashed using SHA256 and stored. Authentication works by comparing the stored hash with the generated hash from the entered password at the time of login.
- Because of the passwords being stored only in their hashed format, user privacy is maintained as the admin also cannot see the password of other users. However, he can change them.
