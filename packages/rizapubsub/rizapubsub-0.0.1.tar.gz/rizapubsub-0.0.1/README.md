# RizaPubsub

inhouse gcp pubsub

## publish

```python
import time
from pubsub import PubSub

c = {}

# begin
p = PubSub(c)
publisher = p.pub()

# xpub = p.create_topic('test_001')
# print(xpub)
# xsub = p.create_subscription('test_001', 'test_sub_001')
# print(xsub)
3

pid = p.send(
    publisher, {
        'topic': 'test001',
        'namespace': 'auth',
        'subname': 'auth_register',
        'delay': 1,
        'data': {
            'fullname': 'mas joko',
            'email': 'panas@gmail.com'
        }
    })
print('send pubsub:', pid)
```

## subscribe

```python
import asyncio
from datetime import datetime
from pubsub import PubSub

c = {}


async def executor(data):
    print("{}".format(data.data), datetime.now())


async def sublistener(config, subname, count=1):
    '''Pubsub listen subscribtion tasks'''
    p = PubSub(c)
    while True:
        subscrb = p.sub()
        with subscrb:
            subpath = subscrb.subscription_path(config["project_id"], subname)

            # get messages
            response = subscrb.pull(request={
                'subscription': subpath,
                'max_messages': count
            })

            ack_ids = []
            for msg in response.received_messages:

                # print("Received: {}".format(msg.message))
                await executor(msg.message)

                ack_ids.append(msg.ack_id)

            # Acknowledges the received messages so they will not be sent again.
            tot = len(response.received_messages)
            if tot > 0:
                subscrb.acknowledge(request={
                    "subscription": subpath,
                    "ack_ids": ack_ids,
                })

        await asyncio.sleep(2)


# begin
async def main_pubsub(c):
    await sublistener(c, 'test001-sub', 10)


if __name__ == '__main__':

    loop = asyncio.new_event_loop()
    try:
        loop.create_task(main_pubsub(c))
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
    finally:
        loop.close()

```
