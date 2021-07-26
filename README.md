# Symbionic-Image-API
This is a REST api created using django and django rest framework. 

The main idea of this API is to fetch the image instance from the image table (Using GET). <strong>The fetched image is modified using pillow to insert a watermark named "Symbionic Image API".  </strong>


## How to run:
1. Clone the repository into the local storage and change directory into the main directory containing the requirements.txt and manage.py files. (The name of the directory is "<strong>backend_image_api</strong>")
2. Install all the requirements: <strong> pip install -r requirements.txt </strong>
3. You can either log in as the default admin (Username/Password = admin) or create a new superuser by running: <strong> python manage.py createsuperuser </strong>
4. Once you are logged in into the admin interface, you can make changes the database and the tables if needed.
5. You can go to <strong> 127.0.0.1:8000/images </strong> to get the json response of the image model/table
6. You can open a specific image instance by giving the "id" attribute of the image in the url like: <strong> 127.0.0.1:8000/images/5 </strong>. You can open the image by clicking the image url specified in the "image" attribute of the json object.


## The following are the options available:
### 1. The user can log in as an authenticated user and then either create a category or add an Image instance to a pre-existing category.

![Screen Shot 2021-07-20 at 8 07 49 PM](https://user-images.githubusercontent.com/43778235/126339536-6476b81a-8a21-4a8f-8a3a-a317d6906c8d.png)

This is what it looks like when we try to add a Image instance into the category of "TV-Shows"
![Screen Shot 2021-07-20 at 8 09 57 PM](https://user-images.githubusercontent.com/43778235/126339956-85c9e49d-a590-4f5b-bc6c-cfad2ec6e7e0.png)


### 2. The user can go to the API root and either request a JSON response for the set of all the images from the image table or request a particular image instance

#### This is what the main API root looks like
![Screen Shot 2021-07-20 at 8 13 17 PM](https://user-images.githubusercontent.com/43778235/126340367-da554b7d-2426-4b80-aebe-d2ebe74bbf11.png)

#### To view the JSON of all the images, go to 127.0.0.1:8000/images
![Screen Shot 2021-07-20 at 8 14 56 PM](https://user-images.githubusercontent.com/43778235/126340639-b1ddd8af-acaa-4cde-8b4e-bda4b7b2d0f2.png)

#### View a particular image instance
![Screen Shot 2021-07-20 at 8 15 54 PM](https://user-images.githubusercontent.com/43778235/126340801-97ffe027-7d82-4f34-85a2-5c46712c0d02.png)

#### The rendered image looks like this (The text "Symbionic" is added to the image before it is displayed)
![Screen Shot 2021-07-20 at 8 18 02 PM](https://user-images.githubusercontent.com/43778235/126341204-4094c57f-b47b-44f1-adfe-8010e7910fbb.png)

#### Note: You can also perform POST requests from these endpoints to alter the table


### 3. The same GET and POST requests can also be made from a different client (Using Postman in this case)
#### In this case, instead of returning a HTML response, the API returns a relevant JSON object
![Screen Shot 2021-07-20 at 8 24 04 PM](https://user-images.githubusercontent.com/43778235/126342259-72d5c502-2e54-4196-933e-24c3dad32805.png)

### 4. You can also visit the HTML front-end page that fetches all the images using the API and displays them
<strong> http://127.0.0.1:8000/all/ </strong>

## So, to summarize;
#### After you've run the server:
http://127.0.0.1:8000/admin/  - admin portal, log in to this portal to view the database and delete entries. However,  you need not need to log in as admin to perform a GET request </br>
http://127.0.0.1:8000  -  API root </br>
http://127.0.0.1:8000/images/ - GET request. Returns a json response of all the images. </br>
http://127.0.0.1:8000/images/1/  GET request. Returns a single image </br>
http://127.0.0.1:8000/all/  - HTML homepage that renders all the images by calling the API</br>



