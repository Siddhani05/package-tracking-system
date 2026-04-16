# src/main.py

class Package:
    def __init__(self, tracking_id, sender, receiver):
        self.tracking_id = tracking_id
        self.sender = sender
        self.receiver = receiver
        self.status = "CREATED"
        self.history = []

    def update_status(self, new_status):
    from datetime import datetime
    self.history.append((self.status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    self.status = new_status
    print(f"[{self.tracking_id}] Status updated to: {self.status}")

    def get_status(self):
        return self.status

    def get_history(self):
        return self.history


class DeliverySystem:
    def __init__(self):
        self.packages = {}

    def add_package(self, package):
        self.packages[package.tracking_id] = package
        print(f"Package {package.tracking_id} registered successfully.")

    def track_package(self, tracking_id):
    pkg = self.packages.get(tracking_id)
    if pkg:
        return f"""
Tracking Details:
-----------------
Tracking ID : {tracking_id}
Status      : {pkg.get_status()}
Sender      : {pkg.sender}
Receiver    : {pkg.receiver}
"""
    return "Package not found."


if __name__ == "__main__":
    system = DeliverySystem()

    p1 = Package("PKG001", "Alice", "Bob")
    system.add_package(p1)

    p1.update_status("IN_TRANSIT")
    p1.update_status("OUT_FOR_DELIVERY")
    p1.update_status("DELIVERED")

    print(system.track_package("PKG001"))
    print("History:", p1.get_history())
    print("Sender:", p1.sender)
    print("Receiver:", p1.receiver)