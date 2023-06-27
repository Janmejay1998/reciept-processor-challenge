# For building docker
```cmd command
docker build -t execute_reciept .
```
# For starting docker 
```cmd command
docker run -p 5000:5000 execute_reciept
```
# Using Postman Service
```
Method: POST 
URL: 'http://localhost:5000/receipts/process'
```
# Request Body Example
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
```json
{
    "id": "4e3cef93-8a60-4642-bb26-f8a9442064c2"
}
```
# Using Postman Service
```
Method: GET 
URL: 'http://localhost:5000/receipts/{id}/points'
```
# Example
```yaml
id: 4e3cef93-8a60-4642-bb26-f8a9442064c2 
```
# Response Example
```json
{
    "points": 109
}
```
