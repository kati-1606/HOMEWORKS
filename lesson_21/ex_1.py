# Class Exercise:
# Create a Python class representing a Hospital account with methods
# to schedule visit and remove schedule

class HospitalAccount:
    def __init__(self, patient_name, account_id):
        self.patient_name = patient_name
        self.account_id = account_id
        self.schedules = {}

    def schedule_visit(self, visit_date, doctor_name):
        self.schedules[visit_date] = doctor_name
        print(f"Visit scheduled on {visit_date} with Dr. {doctor_name}.")

    def remove_schedule(self, visit_date):
        if visit_date in self.schedules:
            removed_doctor = self.schedules.pop(visit_date)
            print(f"Scheduled visit with Dr. {removed_doctor} on {visit_date} has been removed.")
        else:
            print(f"No scheduled visit on {visit_date}.")

account = HospitalAccount("John Doe", 12345)
account.schedule_visit("2025-01-21", "Smith")
account.remove_schedule("2025-01-21")
account.remove_schedule("2025-01-21")



from datetime import datetime, timedelta
import threading


class HospitalAccount:
    def __init__(self, patient_name, account_id):
        self.patient_name = patient_name
        self.account_id = account_id
        self.schedules = {}  # Store visit_date as keys and doctor_name as values
        self.lock = threading.Lock()  # To prevent concurrent modifications

    def schedule_visit(self, visit_date, doctor_name):
        # Convert visit_date string to datetime for validation
        visit_datetime = datetime.strptime(visit_date, "%Y-%m-%d %H:%M")

        with self.lock:  # Ensure thread-safety
            # Check if there are no concurrent registrations
            if visit_datetime in self.schedules:
                print(f"Error: A visit is already scheduled on {visit_date}.")
                return

            # Check for the 30-minute gap constraint
            for scheduled_date in self.schedules.keys():
                scheduled_datetime = datetime.strptime(scheduled_date, "%Y-%m-%d %H:%M")
                if abs((visit_datetime - scheduled_datetime).total_seconds()) < 1800:
                    print(f"Error: Visits must be at least 30 minutes apart. Conflict with {scheduled_date}.")
                    return

            # Schedule the visit
            self.schedules[visit_date] = doctor_name
            print(f"Visit scheduled on {visit_date} with Dr. {doctor_name}.")

    def remove_schedule(self, visit_date):
        with self.lock:  # Ensure thread-safety
            if visit_date in self.schedules:
                removed_doctor = self.schedules.pop(visit_date)
                print(f"Scheduled visit with Dr. {removed_doctor} on {visit_date} has been removed.")
            else:
                print(f"No scheduled visit on {visit_date}.")

# Example usage
account = HospitalAccount("John Doe", 12345)
account.schedule_visit("2025-01-27 14:00", "Smith")
account.schedule_visit("2025-01-27 14:15", "Brown")  # Should fail due to 30-min gap constraint
account.schedule_visit("2025-01-27 14:30", "Brown")  # Should succeed
account.remove_schedule("2025-01-27 14:30")
account.schedule_visit("2025-01-27 14:30", "Taylor")  # Should now succeed





