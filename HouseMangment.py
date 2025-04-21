class House:
    def __init__(self, address, owner, price):
        self.address = address
        self.owner = owner
        self.price = price

    def display_details(self):
        print(f"Address: {self.address}")
        print(f"Owner: {self.owner}")
        print(f"Price: ${self.price}")

class HouseManagementSystem:
    def __init__(self):
        self.houses = []

    def add_house(self, address, owner, price):
        house = House(address, owner, price)
        self.houses.append(house)
        print("House added successfully!")

    def remove_house(self, address):
        for house in self.houses:
            if house.address == address:
                self.houses.remove(house)
                print("House removed successfully!")
                return
        print("House not found!")

    def list_houses(self):
        if not self.houses:
            print("No houses available.")
        else:
            for house in self.houses:
                house.display_details()
                print("-" * 20)

# Example usage
if __name__ == "__main__":
    system = HouseManagementSystem()
    system.add_house("123 Main St", "Alice", 250000)
    system.add_house("456 Elm St", "Bob", 300000)
    system.list_houses()
    system.remove_house("123 Main St")
    system.list_houses()