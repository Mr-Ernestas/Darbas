# Enterprise API

#### Get ENT accounts using AE user

Takes in an enterprise account ID and returns the account details.

|Variable|Input |
|:------:|:----:|
|Role    |API_AE|
|Method  |GET   |
|Service |GET ENT ACCOUNTS|
<p>&nbsp;</p>

![MicrosoftTeams-image](https://user-images.githubusercontent.com/85736827/178256986-b1773bea-6f25-45b1-aab3-2d16dc5fb577.png)
<br />

<p>&nbsp;</p>
<p>&nbsp;</p>

# API Description

#### What is API?

An application programming interface (API) is a way for two or more computer programs to communicate with each other.

#### Simple example:

When you use an application on your mobile phone, the application connects to the Internet and sends data to a server. The server then retrieves that data, interprets it, performs the necessary actions and sends it back to your phone. The application then interprets that data and presents you with the information you wanted in a readable way. 
<p>&nbsp;</p>
<p>&nbsp;</p>

# HTTP response status codes

|Code |  Description   |
|:----|:---------------|
|**200**|This is the standard “OK” status code for a successful HTTP request. The <br />response that is returned is dependent on the request. For example, for a GET request, the <br />response will be included in the message body. For a PUT/POST request, the response will <br />include the resource that contains the result of the action.|
|**201**|This is the status code that confirms that the request was successful and,<br />as a result, a new resource was created. Typically, this is the status code that is sent after a<br />POST/PUT request.|
|**204**|This status code confirms that the server has fulfilled the request but does<br />not need to return information. Examples of this status code include delete requests or if a<br />request was sent via a form and the response should not cause the form to be refreshed or for<br />a new page to load.|
|**304**|The is status code used for browser caching. If the response has not been<br />modified, the client/user can continue to use the same response/cached version. For example,<br />a browser can request if a resource has been modified since a specific time. If it hasn’t, the<br />status code 304 is sent. If it has been modified, a status code 200 is sent, along with the<br />resource.|
|**400**|The server cannot understand and process a request due to a client error.<br />Missing data, domain validation, and invalid formatting are some examples that cause the<br />status code 400 to be sent.|
|**401**|This status code request occurs when authentication is required but has<br />failed or not been provided.|
|**403**|Very similar to status code 401, a status code 403 happens when a valid<br />request was sent, but the server refuses to accept it. This happens if a client/user requires the<br />necessary permission or they may need an account to access the resource. Unlike a status<br />code 401, authentication will not apply here.|
|**404**|The most common status code the average user will see. A status code 404<br />occurs when the request is valid, but the resource cannot be found on the server. Even though<br />these are grouped in the Client Errors “bucket,” they are often due to improper URL redirection.|
|**409**| A status code 409 is sent when a request conflicts with the current state of<br />the resource. This is usually an issue with simultaneous updates, or versions, that conflict with<br />one another.|
|**410**|  Resource requested is no longer available and will not be available again.|
|**500**| Another one of the more commonly seen status codes by users, the 500<br />series codes are similar to the 400 series codes in that they are true error codes. The status<br />code 500 happens when the server cannot fulfill a request due to an unexpected issue. Web<br />developers typically have to comb through the server logs to determine where the exact issue is<br />coming from.|

