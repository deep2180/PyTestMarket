from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='LOBRGIUPNJZZLHJX', output_format='pandas',indexing_type='date')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
#data['close'].plot()
##
# plt.title('Intraday Times Series for the MSFT stock (1 min)')
##plt.show()