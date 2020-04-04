# Machine Learning Model App

This code exposes a route to perform predictions with a (previously done) machine learning model.

### Local deploy

To build the container just run the following command on the root folder of the repo:

````
docker-compose up -d
# or
docker-compose up -d --build
# to force the container rebuild
````

To see the logs use the following:

````
docker-compose logs -f
````


### Postman collection

There is a postman collection file that exemplifies the route calls. Import the [production-ml-model.postman_collection.json](production-ml-model.postman_collection.json) on your postman to see it.

## **Routes documentation**

Here is some explanation about the routes:

### **GET** /predict

Perform a invoice prediction for the given geographical point (lat, lon).

**Parameters**
* lat: The latitude of the point. Range between -90 and 90.
* lon: The longitude of the point. Range between -180 and 180.

Example: 
````
curl 
	--location 
	--request GET 'http://127.0.0.1:5000/predict?lat=-30&lon=-45'
````
