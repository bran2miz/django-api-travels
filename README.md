# Django REST Framework / Docker - Lab 31

## Author: Brandon Mizutani

Version: 1.0.0 (PR URL: [PR URL](https://github.com/bran2miz/django-api-travels/pull/1)

## Overview

This lab assignment required us to use Django REST Framework to create an API, then “containerize” it with Docker.

## Getting Started

### Lab 31

We had to create a project that followed the same steps as the previous lab, only this time we had to used the Django REST Framework to create an api and use Docker desktop. We had to:

- Rebuild a custom version of Things API demo project from scratch.

- Replace things_project and Thing with your own application and model.

- Your model must have at least as many fields as demo’s model.

- Your model must have one field that is a foreign key to user.

We also had to utilize docker to:

- Update Dockerfile and docker-compose.yml if needed.

## Architecture

Python, Django, Models, get_user_model, superuser, CRUD, Docker, REST.

## Change Log

03-17-22 -- Pages render as expected and assignment is complete.

## Credit and Collaborations

Eddie Ponce

Alex Payne

Connor Boyce

Roger Huba

# Permissions & Postgresql - Lab 32

## Author: Brandon Mizutani

Version: 1.0.0 (PR URL: [PR URL](https://github.com/bran2miz/django-api-travels/pull/3)

## Overview

This lab assignment required us to use Django REST Framework to create an API, then “containerize” it with Docker. We then had to adding Permissions and Postgresql Database

## Getting Started

### Lab 32

We had to create a project that followed the same steps as the previous lab, only this time we had to incorporate permissions and postgresql databases so that only users who have logged in have access to the db. We had to:

- Make a site a DRF powered API as we did in previous lab.

- Adjust project’s permissions so that only authenticated user’s have access to API.

- Add a custom permission so that only author of blog post can update or delete it.

- Add ability to switch user’s directly from browsable API.

In the Docker we had to:

- create Dockerfile based off python:3.8-slim
create docker-compose.yml to run Django app as a web service.

- enter docker-compose up --build to start your site.

- add postgres 11 as a service
Note: It is not required to include a volume so that data can persist when container is shut down.
- Go to browsable api and confirm site properly restricts users based on their permissions.

## Architecture

Python, Django, Models, get_user_model, superuser, CRUD, Docker, REST, permissions, postgresql.

## Change Log

03-19-22 -- Pages render as expected and assignment is complete.

## Credit and Collaborations

Eddie Ponce

Alex Payne

Connor Boyce

Roger Huba