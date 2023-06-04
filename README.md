# ABOUT CUSTOMER APP API

This app is a simple CRUD application where user can add a new customer, view their customer profile, edit and delete when needed.

I don't include any special functionality that Django provides for business logic, such as authentication and authorization. As I mentioned earlier, it is only a dead simple CRUD application.

The API from this application also can be used for the front-end as well.

# USER CASES

- User can add new customer and views the existing customer's profile
- User can edit and remove the current customer if needed

# PLANNING

- Using Django Rest Framework to request and response the customer's data
- Make all customer's data as JSON format
- Should response with the status codes (200, 201, 400, 401)
- Test the consumable API using PyTest
