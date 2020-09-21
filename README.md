![alt text](hps://www.django-rest-framework.org/img/logo.png)
# Creating REST api for User using rest_framework
##### User should have the following fields
- ID
- First Name
- Last Name
- Company Name
- Age
- City
- State
- Zip
- Email
- Web

# Endpoints of the applications
1. `/api/users/` (GET)
    - Fetch all the user and display it
    - It also support search query parameter
    	1. Name - `/api/users/?name=john` search for user with their frist and last name ( it is case insensitive ).
    	2. Sort - `/api/users/?sort=-field_name` sort users on ascednding or descending order base of the field provided ('-' indecate descending order).
    	3.	limit - `/api/users/?limit=20` limt the content of the page (default=5).
    	4. page - `/api/users/?page=2` show all content of page 2.

2. `/api/users/` (POST)
    -	Create New User

3. `/api/users/<id>/` (GET)
    -	Display the details of a particular user (here id is primary key)

4. `/api/users/<id>/` (PUT)
    - Update the details of particular user

5. `/api/users/<id>/` (DELETE)
    - Delete particular user

---

# Installation Guide
1. `git clone https://github.com/007ksv/datapeace_assignment.git`
2. `pip3 install -r requirements.txt`
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. `python manage.py runserver`
