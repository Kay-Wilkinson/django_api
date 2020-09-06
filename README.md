# django_api

This is a small working example of using the django rest_framework
library to build an API that lists all food menu items for a restaurant.


Run unit tests:
```
$ python manage.py test
```

Run server:
```
$ python manage.py runserver
```

API URI:

```
http://127.0.0.1:8000/food-menu-items/
```

# Roadmap

* Add more comprehensive unit tests.
    - Current unit tests only over the most basic of behaviours    
* Add Oauth2 authentication to the API
* Reformat the design arrangement of menu items. Items should be arranged
  by categories and subcategories.
* Dockerise the project
* Consider a Domain Driven Design approach for the API architecture