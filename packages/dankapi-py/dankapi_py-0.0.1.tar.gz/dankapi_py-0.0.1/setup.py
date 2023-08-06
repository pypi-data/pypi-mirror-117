__import__('setuptools').setup(
    name = 'dankapi_py',
    version = '0.0.1',
    description = 'An easy to use, async ready Python Wrapper for the API DankAPI (https://dankapi.github.io).',
    long_description = '''
    This is an API Wrapper for the API DankAPI @ https://dankapi.github.io. It is designed to make the API very easy to use.
    It is beginner friendly, documented, asynchronous and object oriented.

    About the API: The API is designed to show information on the famous Discord Bot Dankmemer (https://dankmemer.lol).
    The API currently shows the shop sale the bot has and the bot's economy system's items.
    ''',
    url = 'https://github.com/dankapi/dankapi_py',
    author = 'Nimit Grover',
    author_email = 'dankapi420@gmail.com',
    license = 'MIT',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ],
    keywords = 'apiwrapper dankmemer dankmemer-sale dankmemer-api api internet',
    packages = ['dankapi_py'],
    install_requires = ['aiohttp']
)