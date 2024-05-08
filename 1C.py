import pandas as pd

flight_data = pd.DataFrame({
    "flight_id": [1, 2, 3],
    "departure_city": ["City A", "City B", "City C"],
    "arrival_city": ["City X", "City Y", "City Z"],
    "departure_time": ["2023-01-01 09:00:00", "2023-01-02 10:00:00", "2023-01-03 11:00:00"],
    "arrival_time": ["2023-01-01 12:00:00", "2023-01-02 13:00:00", "2023-01-03 14:00:00"],
    "delay_minutes": [10, 15, 5]
})

flight_data_table = flight_data.copy()

new_flight_data = pd.DataFrame({
    "flight_id": [4, 5],
    "departure_city": ["City D", "City E"],
    "arrival_city": ["City W", "City X"],
    "departure_time": ["2023-01-04 12:00:00", "2023-01-05 15:00:00"],
    "arrival_time": ["2023-01-04 15:00:00", "2023-01-05 18:00:00"],
    "delay_minutes": [8, 12]
})

flight_data_table = pd.concat([flight_data_table, new_flight_data], ignore_index=True)
flight_data_table.loc[2, 'arrival_city'] = 'City Z Updated'
joined_data = flight_data_table.merge(flight_data_table, on='flight_id')

flight_data_table.set_index('flight_id', inplace=True)

flight_data_table['departure_time'] = pd.to_datetime(flight_data_table['departure_time'])
flights_2008 = flight_data_table[flight_data_table['departure_time'].dt.year == 2008]
avg_delay_per_day = flights_2008.groupby(flights_2008['departure_time'].dt.date)['delay_minutes'].mean()

print("Joined Table:")
print(joined_data)

print("\nFlight Information Table with Index:")
print(flight_data_table)

print("\nAverage Departure Delay per Day in 2008:")
print(avg_delay_per_day)