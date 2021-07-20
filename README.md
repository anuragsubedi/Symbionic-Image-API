# Symbionic-Image-API
This is a REST api created using django and django rest framework. 

The main idea of this API is to fetch the image instance from the image table (Using GET). The fetched image is modified using pillow to insert a watermark named "Symbionic".  

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
