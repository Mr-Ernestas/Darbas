# API Definition

#### What is API?

An ***Application Programming Interface*** (API) is a way for two or more computer programs to communicate with each other.

#### Simple example:

When you use an application on your mobile phone, the application connects to the Internet and sends data to a server. The server then retrieves that data, interprets it, performs the necessary actions and sends it back to your phone. The application then interprets that data and presents you with the information you wanted in a readable way. 

<p>&nbsp;</p>

# API Client
API Client means the software that acts as the interface between Agency's computer and the server, which is already developed or to be developed by Agency.

<p>&nbsp;</p>

# REST(RESTful) API Definition
Representational State Transfer (REST) is a software architecture that imposes conditions on how an API should work. REST was initially created as a guideline to manage communication on a complex network like the internet. You can use REST-based architecture to support high-performing and reliable communication at scale. You can easily implement and modify it, bringing visibility and cross-platform portability to any API system.
<p>&nbsp;</p>


# Enterprise API

#### Get ENT accounts using AE user

Takes in an enterprise account ID and returns the account details.

|Variable|Input |
|:------:|:----:|
|Role    |API_AE|

<p>&nbsp;</p>

![MicrosoftTeams-image (2)](https://user-images.githubusercontent.com/85736827/178970712-428945bf-5bd1-42d5-a711-5fbac60f6072.png)

<br />


<p>&nbsp;</p>


![Rest-Client-server](https://user-images.githubusercontent.com/85736827/178935149-90295356-4d6a-48e3-b701-5b743fe2dd58.png)


# HTTP Request

#### What is HTTP Request?
HTTP requests are messages sent by the client to initiate an action on the server.
<p>&nbsp;</p>

#### HTTP Request Example:

A client (browser) sends an HTTP request to the server; then the server returns a response to the client. The response contains status information about the request and may also contain the requested data.

<p>&nbsp;</p>
<p>&nbsp;</p>

# HTTP Response

#### What is HTTP Response?
It is also known as the status text. It is a human-readable text that summarizes the meaning of the status code.

#### HTTP Response Example in JSON:
![Screenshot 2022-07-14 135747](https://user-images.githubusercontent.com/85736827/178967853-73d35bfb-3393-4fcc-88ea-fef8701f02d4.png)


#### What is JSON?
It describes the existing data format.It offers clear, human-readable, and machine-readable documentation.


<p>&nbsp;</p>
<p>&nbsp;</p>

# HTTP response status codes

|Code     |Name    |Description   |
|:-------:|:------:|:---------------|
|***200***|OK      |Standard success scenario for any call|
|***400***|Bad Request|Parse Error in the URI or JSON body received|
|***401***|Unauthorized|Failure to authenticate or a session token has expired|
|***404***|Not found|Used for single ID operations to indicate that the record was not found|
|***409***|Conflict|Error returned when a clash scenario occurs. Such as attempting to add a TN already provisioned by someone else or an update that fails due to time-stamp race condition|
|***410***|Gone|Used to indicate certain scenarios where a referenced item no longer exists|
|***412***|Precondition Failed	|Error returned when a pre-condition fails for the given API call. This is used to apply a form of warning response where the given API call has failed but can be called again with a force/bypass option included to ignore the warning and continue processing.|
|***422***|Unprocessable Entity|Typical go-to error to indicate that some field value is bad, not allowed|
|***500***|Unexpected Error	|Unexpected/Internal Error|
<p>&nbsp;</p>


# Here we collect all the data necessary to fulfill the request. It contains initializing client obj, getting all necessary data to fulfill the POST request to generate a token for a user: 
![MicrosoftTeams-image (3)](https://user-images.githubusercontent.com/85736827/179182997-b01f8829-01cc-41a3-8e8a-9fc38a83471c.png)

<p>&nbsp;</p>


<p>&nbsp;</p>

# Here from received JSON data we are taking token and install it in such way that user use this token to request for authorization:

![MicrosoftTeams-image (5)](https://user-images.githubusercontent.com/85736827/179457486-1782585f-7b8b-49d8-8e05-b8d1f256f6c5.png)

<p>&nbsp;</p>
<p>&nbsp;</p>

# Here we send data to API client, which is in this Framework and receiving token:

![Screenshot 2022-07-18 092225](https://user-images.githubusercontent.com/85736827/179455013-a486989f-16b2-4ca5-ba26-53c39ab49d7c.png)





