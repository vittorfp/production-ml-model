# Machine Learning Model App

This code exposes a route to perform predictions with a (previously done) machine learning model.

The Flask application accesses a Postgres instance to obtain the necessary data give the prediction.

___
### Local deploy

The app is served through docker containers. The configurations are in the ``docker-compose.yml``
file. Three containers will be set-up when the app is running:

- The application: Running on port 5000 by default.
- The Postgres Server,
- The PG Admin web interface: Running on port 80 by default.

If necessary some parameters can be set using environment variables (see ``docker-compose.yml``).  
	 
To run the app, just type the following command on the root folder of the repo:

```bash
docker-compose up -d

# or the following to force the container rebuild
docker-compose up -d --build
```

To see the logs use the following:

```bash
docker-compose logs -f
```
___
### Tests

Automated tests were made to check sanity of the model in a wide range of inputs.
The database connection is mocked (into a dummy output), so, there is no need to be with a database
instance running. 

Test cases:
- ##### Application tests

	- **Input completeness**: Checks if all the expected inputs were sent. If not, checks if the application has thrown 
	the correct errors.
	
	- **Input boundary**: Checks if the input is inside some sane bounds (for latitude and longitude).
	If the given point is outside the sane boundaries, checks if the application has thrown the correct
	errors.
	
	- **Output completeness**: Checks if in a successful run all the expected outputs were returned. 

- ##### Algorithm tests

	- **City boundary**: Checks if the given point is inside the boundaries of Campinas. Checks if the 
	application has correctly thrown an exception when a point outside the city is given.
	
	- **Model outputs**: Checks if the output values of the application are the expected. Takes data from
	the training set of the model and its predicted output. 
	Checks if the outputs of the application are the same as the ones from the training set.
	


##### Running the tests

To run the tests use the following command inside the repository root folder:

```bash
python3 -m pytest app/tests/
```
___
### Postman collection

There is a postman collection file that exemplifies the route calls. Import the [production-ml-model.postman_collection.json](production-ml-model.postman_collection.json) on your postman to see it.

___
### **Routes documentation**

Here is some explanation about the routes:

#### **GET** /predict

Perform a invoice prediction for the given geographical point (lat, lon).

**Parameters**
* lat: The latitude of the point. Range between -90 and 90.
* lon: The longitude of the point. Range between -180 and 180.

Example: 
```bash
curl 
	--location 
	--request GET 'http://127.0.0.1:5000/predict?lat=-30&lng=-45'
```

#### **GET** /health

Simple dummy route to check app status. Returns success when the app is up and serving routes correctly.

Example: 
```bash
curl 
	--location 
	--request GET 'http://127.0.0.1:5000/health'
```

