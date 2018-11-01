from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

my_key='LOBRGIUPNJZZLHJX'
#ts = TimeSeries(key=my_key, output_format='pandas',indexing_type='date')
ts = TimeSeries(key=my_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='60min', outputsize='full')
#print(data.head(5))
#print(data.tail(5))
#print(meta_data)
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()


ti = TechIndicators(key=my_key, output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()