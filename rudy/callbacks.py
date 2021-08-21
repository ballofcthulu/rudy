import random
from nio import AsyncClient, RoomMessageText, MatrixRoom

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from rudy.data import NAMES, QUOTES

class Callbacks:
  def __init__(self, client: AsyncClient):
    self.client = client
    client.add_event_callback(self.message, RoomMessageText)
    self.sid = SentimentIntensityAnalyzer(lexicon_file='/usr/share/nltk_data/sentiment/vader_lexicon/vader_lexicon.txt')

  async def message(self, room: MatrixRoom, event: RoomMessageText) -> None:

    print(event.source)

    if (event.source['unsigned']['age'] > 5000):
      return

    if (event.body.upper().find(self.client.user_id.upper()) != -1):
      name  = random.choice(NAMES)
      statement = ""
      sentiment = ""

      # flip a coin
      if (event.body.upper().find('FLIP') != -1):
        quote = random.choice(['HEADS, {name}!','TAILS, {name}!'])

      # sentiment analysis
      elif (event.body.upper().find('SENTIMENT: ') != -1):
        statement = event.body.upper()
        statement = statement[statement.find('SENTIMENT: ')+11:]
        sentiment = self.sid.polarity_scores(statement)['compound']
        if (sentiment > 0):
          quote = "'{statement}' {sentiment} 👍"
        elif (sentiment < 0):
          quote = "'{statement}' {sentiment} 👎"
        else:
          quote = "🤷"

      # random quote
      else:
        quote = random.choice(QUOTES)

      await self.client.room_send(
        self.client.room_id,
        message_type="m.room.message",
        content={
          "msgtype": "m.text",
          "body": quote.format(name=name,statement=statement,sentiment=sentiment)
        }
      )
