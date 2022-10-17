from easy_exchange_rates import API
api = API()
time_series = api.get_exchange_rates(
  base_currency=input("From Currency: "), 
  targets=[input("To Currency: ")],
  start_date=input("start date(YYYY-MM-DD): "),
  end_date=input("end date(YYYY-MM-DD): "),
  
)
data_frame = api.to_dataframe(time_series)
print(data_frame.head(5))