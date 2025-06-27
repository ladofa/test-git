_token = "7825846987:AAFJdBPdZm95IZkOqrOGm76ZQ6a1BRq7a70"
_myid = "6952012815"

import asyncio
#pip install telelgram-bot
import telegram
import datetime

_bot = telegram.Bot(_token)
_confirmed = {} #읽은 메시지

_last_messages = []
# _loop = asyncio.get_event_loop()


async def _get_message():
    global _last_messages
    try:
        async with _bot:
            updates = (await _bot.get_updates(offset=-1))
            _last_messages = []
            for up in reversed(updates):
                date = up.message.date + datetime.timedelta(hours=9)
                message = up.message.text

                if date in _confirmed:
                    break
                else:
                    _confirmed[date] = message
                    _last_messages.append(message)
    except:
        print('error - telegram', datetime.datetime.now())
        

        
    

async def _send(message):
    # bot = telegram.Bot(_token)
    try:
        async with _bot:
            await _bot.send_message(text=message, chat_id=_myid, parse_mode='HTML')
    except:
        print('error - telegram', datetime.datetime.now())
        _last_messages = ['error']
        
 
# def send_ju(message):
#     asyncio.run_coroutine_threadsafe(_send(message), _loop)

# def get_messages_ju():
#     asyncio.run_coroutine_threadsafe(_get_message(), _loop)
#     return list(reversed(_last_messages))

def send(message):
    if len(message) == 0:
        return
    asyncio.run(_send(message))

def get_messages():
    asyncio.run(_get_message())
    return list(reversed(_last_messages))

if __name__ == '__main__':
    import time
    send('hi this is a test!')
    while True:
        messages = get_messages()
        if messages:
            print(messages)
        time.sleep(1)
