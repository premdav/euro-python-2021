from fastapi import Body, FastAPI, Request, Response
import requests
from benedict import benedict
from dotenv import dotenv_values

config = dotenv_values('.env')

app = FastAPI()

@app.post("/")
async def echo(request: Request, response: Response, data=Body(...)):
    raw_body = await request.body()
    body = raw_body.decode("utf-8")
    payload = benedict(data)

    event_type = payload.get('event.type')
    
    if event_type == 'app_mention':
      channel_id = payload.get('event.channel')
      msg_ts = payload.get('event.ts')
      threaded_ts = payload.get('event.thread_ts')
      print(channel_id)
      msg_data = {
        "channel": channel_id,
        "thread_ts": threaded_ts if threaded_ts is not None else msg_ts,
        "text": "Hello, I am your bot :wave:"
      }
      headers = {
        'Authorization': f'Bearer {config["BOT_TOKEN"]}'
      }

      # try:
      result = requests.post(
        'https://slack.com/api/chat.postMessage',
        json=msg_data,
        headers=headers
      )
      print(result.text)

    return {
        "data": data,
        "raw_body": body,
        "headers": request.headers
    }
