Vendor Store API

Vendor Store API is a Django REST Framework (DRF) application for managing vendors and purchase orders.

Features ------------------------------

Vendor Management: CRUD operations for managing vendors.

Purchase Order Management: CRUD operations for managing purchase orders.

User Authentication: User registration and login functionality using token authentication.

Performance Metrics: Calculation of various performance metrics for vendors.


Installation ----------------------------

step 1: Clone the repository: 
          
          git clone https://github.com/MArbabsabir336/Vendor.git

step 2: Navigate into the project directory:

          cd Vendor

step 3: Create a virtual environment:
          
          python -m venv venv

step 4: Activate the virtual environment:

  on window 
                
              venv\Scripts\activate

  on macOS and Linux  
          
          source venv/bin/activate
        
step 5:Install dependencies:

    pip install -r requirements.txt

step 6: Make Migrations:
    
    python manage.py makemigrations

step 7: Run migrations:
    
    python manage.py migrate

step 8: Run Server
    
    python manage.py runserver


API Endpoints ----------------------


POST /register/: Register a new user.

POST /login/: Login and obtain authentication token.

GET /vendors/: List all vendors.

POST /vendors/: Create a new vendor.

GET /vendors/:id/: Retrieve a specific vendor.

PUT /vendors/:id/: Update a specific vendor.

DELETE /vendors/:id/: Delete a specific vendor.

GET /purchase_orders/: List all purchase orders.

POST /purchase_orders/: Create a new purchase order.

GET /purchase_orders/:id/: Retrieve a specific purchase order.

PUT /purchase_orders/:id/: Update a specific purchase order.

DELETE /purchase_orders/:id/: Delete a specific purchase order.

GET /vendors/:id/performance/: Retrieve performance metrics for a specific vendor.

POST /purchase_orders/:id/acknowledge/: Acknowledge a purchase order.

GET /Vendors/:id/historical_performance/: Retrieve historical performance metrics for a specific vendor.


Contributors ---------


Muhammad Arbab Sabir(@MArbabsabir336)
