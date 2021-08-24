# AWS assignment

## APIs
#### root
[invoke api](https://iz2l444w63.execute-api.ap-southeast-1.amazonaws.com/test/)


#### all book
[invoke api](https://iz2l444w63.execute-api.ap-southeast-1.amazonaws.com/test/)

response:
```
{
    "statusCode": 200,
    "body": "Welcome to Loc's api"
}
```

#### add book
[invoke api](https://iz2l444w63.execute-api.ap-southeast-1.amazonaws.com/test/)

POST method
```
{
    "author" : "test",
    "title" : "test"
}
```

#### get book
[invoke api](https://iz2l444w63.execute-api.ap-southeast-1.amazonaws.com/test/book)

GET method
```
query param: id
```

#### delete book
[invoke api](https://iz2l444w63.execute-api.ap-southeast-1.amazonaws.com/test/delete-book)
POST method
```
{
    "id" : "test"
}
```

### edit book
[invoke api](https://iz2l444w63.execute-api.ap-southeast-1.amazonaws.com/test/edit-book)
POST method
```
{
    "id" : "test"
    "author" : "test",
    "title" : "test"
}
```