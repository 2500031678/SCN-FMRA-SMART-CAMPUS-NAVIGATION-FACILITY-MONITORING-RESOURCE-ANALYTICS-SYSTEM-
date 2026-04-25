import pandas as pd
import json


# --- DATA MODEL ---
class Facility:
    def __init__(self, fid, name, cap):
        self.fid = fid
        self.name = name
        self.cap = cap

    # --- SYSTEM CORE ---


class CampusOS:
    def __init__(self):
        # Dictionary storing Facility objects using ID as the key
        self.facilities = {
            "R101": Facility("R101", "Robotics Lab", 30),
            "S202": Facility("S202", "Seminar Hall", 100)
        }

    def navigate(self):
        dest = input("Enter Destination: ")
        print(f"Pathfinding to {dest}...")
        print("Route: Proceed to Block A, take the stairs to Level 2.")

    def monitor(self):
        fid = input("Enter Facility ID (R101/S202): ").upper()
        if fid in self.facilities:
            occ = int(input(f"Enter current occupancy for {self.facilities[fid].name}: "))
            print(f"Status: {occ}/{self.facilities[fid].cap}")
            if occ > self.facilities[fid].cap:
                print("!!! ALERT: Overcrowding detected. Maintenance log created.")
        else:
            print("Error: Facility ID not found.")

    def analytics(self):
        # Data structure for Pandas analysis
        data = {'Facility': ['Lab', 'Hall', 'Cafe'], 'Usage%': [85, 40, 95]}
        df = pd.DataFrame(data)
        print("\n--- CAMPUS ANALYTICS ---")
        print(df)
        print(f"Average Utilization: {df['Usage%'].mean()}%")

    # --- EXECUTION ---


if __name__ == "__main__":
    system = CampusOS()
    try:
        print("1. Nav | 2. Monitor | 3. Analytics")
        choice = input("Select: ")
        if choice == '1':
            system.navigate()
        elif choice == '2':
            system.monitor()
        elif choice == '3':
            system.analytics()
        else:
            print("Invalid Selection.")
    except Exception as e:
        print(f"System Error: {e}")
