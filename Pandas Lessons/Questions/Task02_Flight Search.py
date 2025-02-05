import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/flights.csv")

while True:
    dates = ("01/04/22 - 29/06/22")
    starts = df["From"].unique().tolist()
    ends = df["To"].unique().tolist()

    Select_date = input(f"Select a date from {dates}: ")
    Select_from = input(f"Select a departure location from {starts}: ").strip()
    Select_to = input(f"Select a destination from {ends}: ").strip()
    Select_time = input("Select AM or PM: ").strip().upper()
    df = df[["From", "To", "Time", Select_date]]
    print(df)
    
    flight = df[
               
                (df["From"].str.contains(Select_from, na=False)) &
                (df["To"].str.contains(Select_to, na=False)) &
                (df["Time"].str.contains(Select_time, na=False))
                
]

    if not flight.empty:
        print("\nAvailable Flights:")
        print(flight)
    else:
        print("\nNo flights available for the selected criteria.")

    again = input("\nSearch for another flight? (yes/no): ").strip().lower()
    if again != "yes":
        break