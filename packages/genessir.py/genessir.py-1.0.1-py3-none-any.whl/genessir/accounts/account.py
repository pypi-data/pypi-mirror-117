"""
The MIT License (MIT)

Copyright (c) 2021-present Dolfies

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import asyncio
import datetime
import hashlib
import logging
import os
from os.path import split as path_split
import random
import tempfile

from genessir.errors import LoginFailure
from genessir.user import BaseUser as ClientUser # Temporary workaround until I make a custom class...
import genessir.utils

from .http import AuthClient
#from .user import ClientUser

log = logging.getLogger(__name__)

class Account:
    """Represents a Discord account."""

    def __init__(self, *, loop=None, **options):
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.use_cache = options.get('use_cache', True)
        self._closed = False

        self.clear()

        connector = options.pop('connector', None)
        proxy = options.pop('proxy', None)
        proxy_auth = options.pop('proxy_auth', None)
        unsync_clock = options.pop('assume_unsync_clock', True)
        captcha_handler = options.pop('captcha_handler', None)
        self.http = AuthClient(connector, proxy=proxy, proxy_auth=proxy_auth, unsync_clock=unsync_clock, loop=self.loop, captcha_handler=captcha_handler)

    def clear(self):
        self.token = None
        self.email = None
        self.password = None
        self.phone = None
        self.user = None

    def _generate_dob(self):
        min = datetime.date(1970, 1, 1)
        max = datetime.date(2008, 1, 1)
        delta = (max - min).days
        return min + datetime.timedelta(days=random.randrange(delta))

    def _get_cache_filename(self, email):
        filename = hashlib.md5(email.encode('utf-8')).hexdigest()
        return os.path.join(tempfile.gettempdir(), 'genessir.py', filename)

    def _get_cache_token(self, email):
        try:
            log.info('Attempting to login via cache...')
            cache_file = self._get_cache_filename(email)
            with open(cache_file, 'r') as f:
                log.info('Token found in cache')
                return f.read()
        except OSError:
            log.info('Token not found in cache')
            return

    def _update_cache(self):
        try:
            cache_file = self._get_cache_filename(self.email)
            os.makedirs(os.path.dirname(cache_file), exist_ok=True)
            with os.fdopen(os.open(cache_file, os.O_WRONLY | os.O_CREAT, 0o0600), 'w') as f:
                log.info('Updating token cache...')
                f.write(self.token)
        except OSError:
            log.warn('Error updating the token cache')
            pass

    def _clear_cache(self, email):
        try:
            cache_file = self._get_cache_filename(email)
            if os.path.exists(cache_file):
                os.remove(cache_file)
        except OSError:
            log.warn('Error clearing the token cache')
            pass

    def _ready(self, token, data, *, password=None):
        self.token = token
        self.email = data['email']
        self.phone = data['phone']
        self.password = password
        self.user = ClientUser(state=None, data=data)

    async def _token_login(self, token, **kwargs):
        if kwargs.get('undelete', False):
            raise TypeError('Cannot undelete account without credentials.')

        log.info('Logging in using static token')
        data = await self.http.static_login(token.strip())
        self._ready(token, data)

    async def _credential_login(self, email, password, **kwargs):
        http = self.http
        use_cache = self.use_cache
        undelete = kwargs.get('undelete', False)

        if use_cache and not undelete:
            token = self._get_cache_token(email)
            if token is not None:
                try:
                    data = await http.static_login(token)
                except LoginFailure:
                    log.info('Cached token is invalid')
                else:
                    self._ready(token, data, password=password)
                    return

        token = await http.login(email, password, undelete=undelete)
        data = await http.static_login(token)
        self._ready(token, data, password=password)

        if use_cache:
            self._update_cache()

    async def _claimed_register(self, username, email, password, **kwargs):
        ...

    async def _unclaimed_register(self, username, **kwargs):
        http = self.http
        invite = kwargs.get('invite', None)
        if invite is None:
            raise TypeError('register() missing 1 required keyword-only argument: \'invite\'')
        else:
            invite = utils.resolve_invite(invite)

        token = await http.register_from_invite()

    async def login(self, *args, **kwargs):
        self._closed = False

        length = len(args)
        if length == 1:
            await self._token_login(args[0], **kwargs)
        elif length == 2:
            await self._credential_login(args[0], args[1], **kwargs)
        else:
            raise TypeError(f'login() takes 1 or 2 positional arguments but {length} were given')

    async def register(self, *args, **kwargs):
        self._closed = False

        length = len(args)
        if length == 1:
            await self._unclaimed_register(*args, **kwargs)
        elif length == 3:
            await self._claimed_register(*args, **kwargs)
        else:
            raise TypeError(f'register() takes 1 or 3 positional arguments but {length} were given')

    async def logout(self):
        if self.use_cache:
            self._clear_cache(self.email)

        await self.http.logout()
        await self.close()

    async def close(self):
        if self._closed:
            return

        self.clear()

        await self.http.close()
        self._closed = True
