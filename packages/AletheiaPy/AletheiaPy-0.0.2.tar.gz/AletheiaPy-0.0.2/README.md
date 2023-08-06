# AletheiaPy

AletheiaPy is a Python wrapper of Aletheia API, which provides access to financial data.

## Installation

Run the following to install:

```python
pip install AletheiaPy
```

## Usage

Note that an API key is required to use the client.

```python
from AletheiaPy import Client

# Initialize Client
key = "333acb16de254844ab64783232d2ba66" # Example from Aletheia's website
Aletheia = Client(key)

# Get a stock summary for a security
Aletheia.StockData("FB")
```