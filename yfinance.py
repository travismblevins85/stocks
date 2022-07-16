from yfapi import YahooFinanceAPI, Interval
from datetime import datetime, timedelta


dh = YahooFinanceAPI(Interval.DAILY)
now = datetime.today()
then = now - timedelta(days=365)
df = dh.get_ticker_data("msft", then, now)

print(df.tail)