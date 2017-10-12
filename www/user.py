# -*- coding: utf-8 -*-

import orm, asyncio
from models import User, Blog, Comment

async def test(loop1):
    await orm.create_pool(loop=loop1, user='root', password='12345678', db='awesome')

    u = User(name='Test', email='test123@example.com', passwd='1234567890', image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
