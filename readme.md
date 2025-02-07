**Solana Python Starters [Abandoned]**
==========================

**Overview**
------------

This project is a Python application that interacts with the Solana blockchain. It includes APIs for connecting to the Solana network, reading balances, and sending transactions.

**Requirements**
---------------

* Python 3.11.8
* Solana SDK
* FastAPI
* Uvicorn
* SQLAlchemy
* Asyncpg

**Project Structure**
---------------------

* `apis`: Contains API routers for blockchain interactions
	+ `blockchain_test.py`: API for testing blockchain connections and transactions
	+ `check_balance.py`: API for checking Solana account balances
* `database.py`: Defines the database connection and schema
* `main.py`: The main application file, which sets up the FastAPI app and includes API routers
* `requirements.txt`: Lists project dependencies
* `dependencies.txt`: Lists project dependencies with descriptions

**Usage**
-----

1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `uvicorn main:app --reload --host 127.0.0.1 --port 5000`
3. Use the APIs:
	+ `GET /create-table`: Creates a table in the database
	+ `GET /`: Returns a hello message
	+ `GET /check-balance`: Checks the balance of a Solana account (see `apis/check_balance.py` for usage)

**API Documentation**
--------------------

### Blockchain Test API

* `GET /test`: Tests the blockchain connection and sends a transaction

### Check Balance API

* `GET /check-balance`: Checks the balance of a Solana account
	+ Query parameter: `public_key` (required)

**Database Schema**
-------------------

The database schema is defined in `database.py`. The schema includes a single table, `users`, with the following columns:

* `id`: Serial primary key
* `name`: VARCHAR(255)
* `email`: VARCHAR(255) UNIQUE
* `password`: VARCHAR(255)

**Contributing**
--------------

Contributions are welcome! Please submit pull requests with clear descriptions of changes.

**License**
-------

This project is licensed under the MIT License. See `LICENSE` for details.
