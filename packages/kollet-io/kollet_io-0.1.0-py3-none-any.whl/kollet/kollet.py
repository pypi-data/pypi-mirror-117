"""
Kollet Merchant API Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python API wrapper for the Kollet Merchant API

:copyright: (c) 2021 by Kollet.io.
:license: MIT, see LICENSE for more details.
"""
__author__ = "Kollet.io"
__version__ = "0.0.2"

import requests
from .errors import KolletErrors

class Kollet(object):
    def __init__(self, api_key: str):
        """ 
        Instantiates an instance of :class: `Kollet`.

        :param api_key: `str`, API Key that authenticates requests to the Kollet Merchant API
        """
        self.__base_url: str = "https://api.kollet.io/v1"
        self.__api_key = api_key
        self.__endpoints = { "currencies": "currencies", "address": "address/create", "balance": "balance", 
        "estimate_fee": "estimateFee", "send": "send"}

    def __request(self, endpoint: str, payload: dict): 
        url = f'{self.__base_url}/{endpoint}'
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        raise KolletErrors("Bad Request")

    def get_currencies(self):
        """
        Get all the cryptocurrencies supported by Kollet.

        :return: JSON response

        :error: raises error :class: `KolletErrors` when response success is false or status code is 400
        """

        endpoint = self.__endpoints.get("currencies")
        payload = {"accessToken": self.__api_key}

        response = self.__request(endpoint, payload)
        if response["success"]:
            return response
        raise KolletErrors(response["message"])

    def create_address(self, currency: str, label: str, metadata: dict = {}):
        """
        Generate a payment address. This is the address that customers pay to.

        Parameters
        ----------
        :param currency: `str`, the code of the supported cryptocurrency.Visit the supported cryptocurrency 
        section to view the currencies supported and their various codes. e.g. BTC
        :param label: `str`, a unique id that is linked to the address. You can use this id to identify 
        different users or payment addresses.
        :param metadata: `dict` An optional field where you can store a JSON object. This field is attached 
        to all webhooks when we are notifying you of new changes to the status of a payment.
        
        :return: JSON response

        :error: raises error :class: `KolletErrors` when response success is false or status code is 400
        """

        endpoint = self.__endpoints.get("address")
        payload = {
            "accessToken": self.__api_key,
            "currency": currency,
            "label": label,
            "metadata": metadata
        }

        response = self.__request(endpoint, payload)
        if response["success"]:
            return response
        raise KolletErrors(response["message"])

    def get_balance(self, currency: str):
        """
        Get balance of a particular cryptocurrency.

        Parameters
        ----------
        :param currency: `str`, the code of the supported cryptocurrency.Visit the supported cryptocurrency 
        section to view the currencies supported and their various codes. e.g. BTC
        
        :return: JSON response

        :error: raises error :class: `KolletErrors` when response success is false or status code is 400
        """
        
        endpoint = self.__endpoints.get("balance")
        payload = {
            "accessToken": self.__api_key,
            "currency": currency
        }

        response = self.__request(endpoint, payload)
        if response["success"]:
            return response
        raise KolletErrors(response["message"])
    
    def estimate_network_fee(self, amount:str, currency: str, duration: str):
        """
        Get an estimated fee for sending funds on a particular cryptocurrency network.

        Parameters
        ----------
        :param amount: `str`, the amount of cryptocurrency units you want to send out.
        :param currency: `str`, the code of the supported cryptocurrency.Visit the supported cryptocurrency 
        section to view the currencies supported and their various codes. e.g. BTC
        :param duration, `str`, this is the duration code. This duration code determines how much fees you actually pay and 
        how fast you your recipient receive their funds. 
        Refer to https://docs.kollet.io/docs/kollet-merchant/docs/2.0.Network-Fee-And-Duration.md for the different durations.
        
        :return: JSON response

        :error: raises error :class: `KolletErrors` when response success is false or status code is 400
        """

        endpoint = self.__endpoints.get("estimate_fee")
        payload = {
            "accessToken": self.__api_key,
            "amount": amount,
            "currency": currency,
            "duration": duration
        }

        response = self.__request(endpoint, payload)
        if response["success"]:
            return response
        raise KolletErrors(response["message"])

    def send_coins(self, amount:str, currency: str, duration: str, recipient: str):
        """
        Get an estimated fee for sending funds on a particular cryptocurrency network.

        Parameters
        ----------
        :param amount: `str`, the amount of cryptocurrency units you want to send out.
        :param currency: `str`, the code of the supported cryptocurrency.Visit the supported cryptocurrency 
        section to view the currencies supported and their various codes. e.g. BTC
        :param duration, `str`, this is the duration code. This duration code determines how much fees you actually pay and 
        how fast you your recipient receive their funds. 
        Refer to https://docs.kollet.io/docs/kollet-merchant/docs/2.0.Network-Fee-And-Duration.md for the different durations.
        :param recipient: `str`, this is the destination. The receiving wallet address/recipient.
        
        :return: JSON response

        :error: raises error :class: `KolletErrors` when response success is false or status code is 400
        """

        endpoint = self.__endpoints.get("send")
        payload = {
            "accessToken": self.__api_key,
            "amount": amount,
            "currency": currency,
            "duration": duration,
            "recipient": recipient
        }

        response = self.__request(endpoint, payload)
        if response["success"]:
            return response
        raise KolletErrors(response["message"])