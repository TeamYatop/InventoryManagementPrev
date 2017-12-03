## ItemCreate
> 재품 생성을 위한  API

## Request
### URL
```ROOT/api/itemcreate/```

### Method
```POST```

### URL Params
```None```

### Data Params
Name | Value | Type
------------ | ------------- | -------------
item | 재품 이름 | string
color | 재품 색상 | string

## Response

### Success Response
- Code: 201
- Content:


```
{
    "pk": 1,
    "item": "ghost",
    "color": "black",
}
```

### Error Response
- Code: 400
- Reason: 키(item or color)가 없는 경우
- Content:


```
{
  "item": [
    "This field is required."
  ],
  "color": [
    "This field is required."
  ]
}
```

## Sample Call
```
$.ajax({
  url: 'ROOT/api/itemcreate/',
  type: 'POST',
  dataType: 'json',
  data: {
    item: item,
    color: color
  }
})
.done(function(response) {
  console.log(response);
})
.fail(function(response) {
  console.log(response);
});
```
