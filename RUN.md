# For building docker
1. Execute the following command
```cmd command
docker build -t execute_reciept .
```
# For starting docker 
2. Now Execute this after previous command execution
```cmd command
docker run -p 5000:5000 execute_reciept
```
# Using Postman Service
```
Method: POST 
URL: 'http://localhost:5000/receipts/process'
```
# Request Body Example
Pass any Json body in the body tab from Postman dashboard
```json
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
```
# Response Example
Now you will get id which will be used in later steps
```json
{
    "id": "4e3cef93-8a60-4642-bb26-f8a9442064c2"
}
```
# Using Postman Service
Use the generated id which you obtained from previous Postman Json body execution
```
Method: GET 
URL: 'http://localhost:5000/receipts/{id}/points'
```
# Example
```yaml
id: 4e3cef93-8a60-4642-bb26-f8a9442064c2 
```
# Response Example
Hence!! You will get the points based on the set of rules mentioned in task!!
```json
{
    "points": 109
}
```
