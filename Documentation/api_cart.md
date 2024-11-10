# API Documentation - Cart and Menu Management

## Overview
This API allows users to interact with a shopping cart and menu items, either while logged in or as guests. Users can add, view, and remove items from their cart.

## Endpoints

---

### 1. Menu Items
Retrieve a list of available menu items.

#### **GET** `http://127.0.0.1:8000/menu/menu-cards/`

- **Description**: Retrieves a list of all menu items.
- **Method**: `GET`
- **Response**:
  - **Status**: `200 OK`
  - **Data**:
    ```json
    [
      {
        "id": 1,
        "name": "Pizza",
        "description": "Delicious cheese pizza",
        "price": 12.99,
        "image": "URL_to_image"
      },
      
    ]
    ```

---

### 2. View Cart
Retrieve cart items for the current user or guest session.

#### **GET** `http://127.0.0.1:8000/cart/cart/`

- **Description**: Fetches all items in the user's or guest's cart.
- **Method**: `GET`
- **Response**:
  - **Status**: `200 OK`
  - **Data**:
    ```json
    {
      "cart_items": [
        {
          "id": 1,
          "menu_item": {
            "id": 1,
            "name": "Pizza",
            "description": "Delicious cheese pizza",
            "price": 12.99,
            "image": "URL_to_image"
          },
          "quantity": 2,
          "total_price": 25.98
        },
      
      ],
      "total_items": 3,
      "total_cart_price": 50.97
    }
    ```

---

### 3. Add Item to Cart
Add a menu item to the cart for the current user or guest session.

#### **POST** `http://127.0.0.1:8000/cart/add-to-cart/`

- **Description**: Adds a specified item to the cart.
- **Method**: `POST`
- **Request Body**:
  - `menu_item` (integer): ID of the menu item to add.
  - `quantity` (integer, optional): Quantity of the item (default is 1).
  - **Example**:
    ```json
    {
      "menu_item": 1,
      "quantity": 2
    }
    ```
- **Response**:
  - **Status**: `201 Created`
  - **Data**:
    ```json
    {
      "message": "Item added to cart successfully.",
      "quantity": 2
    }
    ```

---

### 4. Remove Item from Cart
Remove an item from the cart by its cart ID.

#### **DELETE** `http://127.0.0.1:8000/cart/remove/<item_id>/`

- **Description**: Removes a specified item from the cart.
- **Method**: `DELETE`
- **URL Parameter**:
  - `item_id` (integer): ID of the cart item to remove.
- **Response**:
  - **Status**: `204 No Content`
  - **Data**:
    ```json
    {
      "message": "Item removed from cart successfully."
    }
    ```

---

## Models

### 1. Menu Model
Fields in each menu item:
- `id`: unique identifier.
- `name`: name of the menu item.
- `description`: description of the item.
- `price`: price of the item.
- `image`: URL to the image of the item.

### 2. Cart Model
Fields in each cart item:
- `user`: reference to the user (nullable for guests).
- `session_id`: unique session identifier (used for guests).
- `menu_item`: the item being added.
- `quantity`: number of units for this item.
- `total_price`: calculated field (quantity * price).

---

## Notes
- **Authentication**: Endpoints can be used by both authenticated users and guests.
- **Session Management**: Guests are tracked using `session_id`.
