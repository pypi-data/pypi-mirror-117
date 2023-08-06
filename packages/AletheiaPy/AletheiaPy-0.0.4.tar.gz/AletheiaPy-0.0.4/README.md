# AletheiaPy

AletheiaPy is a Python wrapper of [Aletheia API](https://aletheiaapi.com/), which provides access to financial data.

## Installation

Run the following to install:

```python
pip install AletheiaPy
```

## Usage

Note that an API key is required to use the client. AletheiaPy essentially follows [Aletheia API's usage](https://aletheiaapi.com/docs/). Note that AletheiaPy currently supports GET requests only.

```python
from Aletheia import Client

# Initialize Client
key = "333acb16de254844ab64783232d2ba66" # Example from Aletheia's website
theia = Client(key)

# Get a stock summary for a security
theia.StockData("FB")
```