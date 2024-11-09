
# API Documentation for Cart System

This document describes the API endpoints related to managing the user's cart, including adding products to the cart and interacting with menu items.
## **3. Get Menu List**

**URL**: `http://127.0.0.1:8000/menu/menu-cards/`

**Method**: `GET`

**Response**:
- **Success (200 OK)**:
```json
[
  {
    "id": 1,
    "name": "Item Name 1",
    "description": "Description of item 1",
    "price": 10.0,
    "image": "http://example.com/image1.jpg"
  },
  {
    "id": 2,
    "name": "Item Name 2",
    "description": "Description of item 2",
    "price": 20.0,
    "image": "http://example.com/image2.jpg"
  }
]
```

**Description**: This endpoint allows the user to get the list of all available menu items.

----

## 1. Add to Cart

**Endpoint**: `POST http://127.0.0.1:8000/cart/add-to-cart/`

This endpoint allows users to add menu items to their cart.

### Request

#### URL
`http://127.0.0.1:8000/cart/add-to-cart/`

#### Headers
- **Authorization**: `Token <your_token_here>`

#### Body (JSON)

```json
{
    "menu_item": <menu_item_id>,
    "quantity": <quantity>
}
```

- **menu_item**: The ID of the menu item to be added to the cart. This is a required field.
- **quantity**: The number of items to add to the cart (default is 1 if not provided).

#### Example Request

```json
{
    "menu_item": 1,
    "quantity": 2
}
```

### Response

#### Success Response
- **Status Code**: `201 Created`
- **Body**:

```json
{
    "message": "Item added to cart successfully."
}
```

#### Error Response (Invalid Product ID)
- **Status Code**: `404 Not Found`
- **Body**:

```json
{
    "error": "Menu item not found."
}
```

#### Error Response (Missing Menu Item)
- **Status Code**: `400 Bad Request`
- **Body**:

```json
{
    "error": "Menu item is required."
}
```

#### Error Response (Invalid Quantity)
- **Status Code**: `400 Bad Request`
- **Body**:

```json
{
    "error": "Invalid quantity."
}
```

---

## 2. View Cart

**Endpoint**: `GET http://127.0.0.1:8000/cart/cart/`

This endpoint retrieves the user's current cart, including the items and their quantities.

### Request

#### URL
`http://127.0.0.1:8000/cart/cart/`

#### Headers
- **Authorization**: `Token <your_token_here>`

#### Response

#### Success Response
- **Status Code**: `200 OK`
- **Body**:

```json
{
    "cart_items": [
        {
            "id": 2,
            "menu_item": {
                "id": 1,
                "name": "text",
                "description": "text",
                "price": "3.00",
                "image": "/media/menu_images/photo_5864229624928650547_y.jpg"
            },
            "quantity": 1,
            "total_price": 3.0
        },
        {
            "id": 3,
            "menu_item": {
                "id": 2,
                "name": "text",
                "description": "text",
                "price": "34.00",
                "image": "/media/menu_images/photo_5864229624928650547_y_EarAnev.jpg"
            },
            "quantity": 2,
            "total_price": 68.0
        }
    ],
    "total_items": 3,
    "total_cart_price": 71.0
}
```

#### Error Response (Unauthorized)
- **Status Code**: `401 Unauthorized`
- **Body**:

```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

 

## **3. Remove Item from Cart**

**URL**: `http://127.0.0.1:8000/cart/remove/<int:item_id>/`

**Method**: `DELETE`

**Headers**:
- `Authorization`: `Bearer <Your-Token>`

**Response**:
- **Success (204 No Content)**:
```json
{
  "message": "Item removed from cart successfully."
}
```
- **Error (404 Not Found)**:
```json
{
  "error": "Cart item not found."
}
```

**Description**: This endpoint allows a user to remove an item from their cart by providing the `item_id` of the cart item.
