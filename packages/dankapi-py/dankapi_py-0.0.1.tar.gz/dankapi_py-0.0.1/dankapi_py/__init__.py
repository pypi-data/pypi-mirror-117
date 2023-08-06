'''
An easy to use, async ready Python Wrapper for the API DankAPI (https://dankapi.github.io).
========

GitHub: https://github.com/dankapi/dankapi_py
API: https://dankapi.github.io
Documentation: https://dankapi.github.io/docs/wrappers/dankapi_py

MIT License
========
Copyright 2021-present ImNimboss

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies
or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from aiohttp import request as _request
from json import (loads as _loads, dumps as _dumps)
from typing import (List as _List, Optional as _Optional)

__title__: str = 'dankapi_py'
__author__: str = 'ImNimboss'
__license__: str = 'MIT'
__copyright__: str = 'Copyright (c) 2021 - Present ImNimboss'
__version__: str = '0.0.1'
__links__: dict = {
    'GitHub': 'https://github.com/dankapi/dankapi_py',
    'API': 'https://dankapi.github.io',
    'Documentation': 'https://dankapi.github.io/docs/wrappers/dankapi_py'
}

class BadStatusCode(Exception):
    '''
    An error that's raised when an abnormal status code is encountered while requesting from the API.\n
    Attributes:\n
        `status_code`: int
    '''
    def __init__(self, status_code: int):
        self.status_code = status_code
        if status_code == 429: message = ' You are being ratelimited.'
        elif status_code == 408: message = ' Requesting from the API timed out.'
        elif status_code >= 500: message = ' This is an internal server error.'
        else: message = ''
        super().__init__(f'An abnormal status code of {status_code} was encountered while requesting from the API.{message}')

class DankSale:
    '''
    A read only class that represents a Dankmemer Sale. You can obtain an object of this class from `await get_current_danksale()`.\n
    Attributes:\n
        `name`: str - The name of the item currently on sale.
        `description`: str - The description of the item currently on sale.
        `item_picture`: str - The url of the logo/picture of the item currently on sale.
        `discounted_price`: int - The price of the item currently on sale after applying sale discounts.
        `discount_percent`: int - The percentage of the difference between the discounted_price and the original_price.
        `original_price`: int - The original price of the item currently on sale, without any discounts.
        `last_updated_utc`: str - The time in UTC when the item was last updated in the API. This is usually approximately the time on which the item came on sale. Format - "Day, Month Date Year, Hour:Minutes:Seconds AM/PM UTC": for example "Sat, August 14 2021, 06:58:16 AM UTC".
        `last_updated_utc_epoch`: int - The time in UTC when the item was last updated, in number of seconds since January 1, 1970, midnight @ UTC (look up "epoch unix time" for more details).
    '''
    def __init__(self, jsondata: dict) -> None:
        for key in jsondata: setattr(self, key, jsondata[key])

    def __repr__(self) -> str:
        return f'<name="{self.name}" ' \
            f'description="{self.description}" ' \
            f'item_picture="{self.item_picture}" ' \
            f'discounted_price={self.discounted_price} '\
            f'discount_percent={self.discount_percent} '\
            f'original_price={self.original_price} '\
            f'last_updated_utc="{self.last_updated_utc}" '\
            f'last_updated_utc_epoch={self.last_updated_utc_epoch}>'

    def __str__(self) -> str:
        return f'Name - {self.name}\n' \
            f'Description - {self.description}\n' \
            f'Item Picture - {self.item_picture}\n' \
            f'Discounted Price - {self.discounted_price}\n' \
            f'Discount Percent - {self.discount_percent}\n' \
            f'Original Price - {self.original_price}\n' \
            f'Last Updated - {self.last_updated_utc} ({self.last_updated_utc_epoch})\n'

    def __eq__(self, other):
        return isinstance(other, DankSale) and self.last_updated_utc_epoch == other.last_updated_utc_epoch

    def to_dict(self) -> dict:
        '''
        Returns a dict representation of the class's main attributes.\n
        Format - {'name': self.name, 'description': self.description, ...} for name, description, item_picture, discounted_price, discount_percent, original_price, last_updated_utc and last_updated_utc_epoch.
        '''
        return {
            'name': self.name,
            'description': self.description,
            'item_picture': self.item_picture,
            'discounted_price': self.discounted_price,
            'discount_percent': self.discount_percent,
            'original_price': self.original_price,
            'last_updated_utc': self.last_updated_utc,
            'last_updated_utc_epoch': self.last_updated_utc_epoch
        }

    def to_json(self) -> str:
        '''
        Returns a json-formatted string of `to_dict()`
        '''
        return _dumps(self.to_dict())

class DankItem:
    '''
    A read only class that represents a Dankmemer Item. You can obtain an object of this class from `await get_all_items()` or `await get_item(str)`.\n
    Attributes:\n
        `name`: str - The name of the item.
        `description`: str - The description of the item.
        `icon_url`: str - The url of the logo/picture of the item currently on sale.
        `buy_price`: Optional[int] - The buying price of the item. Can be None if it isn't purchasable.
        `sell_price`: Optional[int] - The selling price of the item. Can be None if it isn't sellable.
        `trade`: str - The trade price of the item. Format - {low-price}{unit} - {high-price}{unit}, example: 990k - 1.5m.
    '''
    def __init__(self, name: str, jsondata: dict) -> None:
        self.name = name
        for attr in jsondata:
            setattr(self, attr, jsondata[attr])
        try:
            self.list_of_items
        except AttributeError:
            self.list_of_items = None

    def __repr__(self) -> str:
        return f'<name="{self.name}" ' \
            f'description="{self.description}" ' \
            f'icon_url="{self.icon_url}" ' \
            f'buy_price={self.buy_price} ' \
            f'sell_price={self.sell_price} '\
            f'trade="{self.trade}">'

    def __str__(self) -> str:
        return f'Name - {self.name}\n' \
            f'Description - {self.description}\n' \
            f'Icon url - {self.icon_url}\n' \
            f'Buy price - {self.buy_price}\n' \
            f'Sell price - {self.sell_price}\n' \
            f'Trade - {self.trade}'

    def __eq__(self, other):
        return isinstance(other, DankItem) and self.name == other.name

    def to_dict(self) -> dict:
        '''
        Returns a dict representation of the class's main attributes.\n
        Format - {'name': self.name, 'description': self.description, ...} for name, description, icon_url, buy_price, sell_price and trade.
        '''
        return {
            'name': self.name,
            'description': self.description,
            'icon_url': self.icon_url,
            'buy_price': self.buy_price,
            'sell_price': self.sell_price,
            'trade': self.trade
        }

    def to_json(self) -> str:
        '''
        Returns a json-formatted string of `to_dict()`
        '''
        return _dumps(self.to_dict())

async def get_current_danksale() -> DankSale:
    '''
    Fetches the current Dankmemer Sale from the API and returns it in the form of class `dankapi_py.DankSale`.\n
    Return type - `dankapi_py.DankSale`\n
    Raises - `dankapi_py.BadStatusCode` if an abnormal status code is encountered while requesting from the API, but this is rare.
    '''
    async with _request('GET', 'https://raw.githubusercontent.com/dankapi/danksale/main/sale.json') as response:
        if response.status > 300 or response.status < 200: raise BadStatusCode(response.status)
        return DankSale(_loads(await response.text()))

async def get_all_items() -> _List[DankItem]:
    '''
    Fetches all the Dankmemer items from the API and returns them as a list of `dankapi_py.DankItem` objects.\n
    Return type - `List[dankapi_py.DankItem]`\n
    Raises - `dankapi_py.BadStatusCode` if an abnormal status code is encountered while requesting from the API, but this is rare.
    '''
    async with _request('GET', 'https://dankapi.github.io/items.json') as response:
        if response.status > 300 or response.status < 200: raise BadStatusCode(response.status)
        jsondata = await response.json()
        items = []
        for data in jsondata: items.append(DankItem(data, jsondata[data]))
        return items

async def filter_items(
        *,
        name: str = None,
        buy_price: int = 'ARGUMENT NOT GIVEN',
        sell_price: int = 'ARGUMENT NOT GIVEN',
        description: str = None,
        type: str = None,
        trade_range: list = None,
        icon_url: str = None,
        item_list: _Optional[list] = 'ARGUMENT NOT GIVEN'
    ) -> _List[DankItem]:
    '''
    Requests all the items from the API then filters all items with the given parameters.\n
    For example if you executed "await dankapi_py.filter_items(name = 'Apple')" it would return a list of all items with the name "Apple".\n
    If you executed "await dankapi_py.filter_items(name = 'Foo', description = 'bar')" then it would return all the items with the name "Foo" AND the description "bar".\n
    You can filter items with these keyword arguments:\n
        `name: str`
        `buy_price: int or None`
        `sell_price: int or None`
        `description: str`
        `type: str`
        `trade_range: list`
        `icon_url: str`
        `item_list: list or None`
    Return type - `List[dankapi_py.DankItem]`\n
    Raises - `dankapi_py.BadStatusCode` if an abnormal status code is encountered while requesting from the API, but this is rare.
    '''
    async with _request('GET', 'https://dankapi.github.io/items.json') as response:
        if response.status > 300 or response.status < 200: raise BadStatusCode(response.status)
        list_of_items = []
        jsondata = await response.json()
        for key in jsondata:
            jsondata[key]['list_of_items'] = jsondata[key].get('list_of_items')
        for key in jsondata:
            list_of_items.append({'name': key} | jsondata[key])
    
    if name: list_of_items = [item for item in list_of_items if item['name'] == name]
    if not buy_price == 'ARGUMENT NOT GIVEN': list_of_items = [item for item in list_of_items if item['buy_price'] == buy_price]
    if not sell_price == 'ARGUMENT NOT GIVEN': list_of_items = [item for item in list_of_items if item['sell_price'] == sell_price]
    if description: list_of_items = [item for item in list_of_items if item['description'] == description]
    if type: list_of_items = [item for item in list_of_items if item['type'] == type]
    if trade_range: list_of_items = [item for item in list_of_items if item['trade_range'] == trade_range]
    if icon_url: list_of_items = [item for item in list_of_items if item['icon_url'] == icon_url]
    if not item_list == 'ARGUMENT NOT GIVEN': list_of_items = [item for item in list_of_items if item['list_of_items'] == item_list]
    dankitem_list = []
    for item in list_of_items:
        dankitem_list.append(DankItem(item['name'], jsondata[item['name']]))
    return dankitem_list