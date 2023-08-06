# Kollet Python API Wrapper
Python API wrapper for the Kollet Merchant API

## Features
- Get all the cryptocurrencies supported by Kollet.
- Generate a payment address. This is the address that customers pay to.
- Get a balance of a particular cryptocurrency.
- Get an estimated fee for sending funds on a particular cryptocurrency network.
- Send out funds to another wallet address on a particular cryptocurrency network.

## 📦 Installation
```
$ python -m pip install kollet-io
```
or 
```
pip install kollet-io
```

## 📝 Configuring and using module
To access the API, you will need an accessToken or API Key from the merchant [dashboard]("https://app.kollet.io/developer/integrations").

# Quick start Guide
```python

from kollet.kollet import Kollet

client = Kollet(api_key="YOUR_API_KEY")

```

# Example use

Get all available currencies

```python

response = client.get_currencies()
print(response)

```

Create payment address
- Takes the currency, label and optional meta data (type dict) as arguments
 
```python

response = client.create_address('btc', 'kollet')
print(response)

```

Get balance of a particular cryptocurrency
- Accepts code of supported cryptocurrency e.g. btc

```python

response = client.get_balance("btc")
print(response)

```


Get an estimated fee for sending funds on a particular cryptocurrency network.
- Accepts amount to send, currency code and duration

```python

response = client.estimate_network_fee("0.000536", "btc", "FASTEST")
print(response)

```


Send out funds to other wallet address on a particular cryptocurrency network.
- Takes amount to send, currency code, duration and destination address

```python

response = client.send_coins("0.000536", "btc", "FASTEST", "RECIPIENT_ADDRESS")
print(response)

```