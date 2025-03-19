class Smartphone:

    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_life = battery_life
        self.is_on = False

    def power_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.brand} {self.model} is now ON.")
        else:
            print(f"{self.brand} {self.model} is already ON.")

    def power_off(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.brand} {self.model} is now OFF.")
        else:
            print(f"{self.brand} {self.model} is already OFF.")

    def battery_status(self):
        print(f"Battery life: {self.battery_life} hours.")

    def __str__(self):
        return f"{self.brand} {self.model} - Price: KES{self.price}"


class Smartphone5G(Smartphone):
    """A subclass representing a 5G-enabled smartphone."""

    def __init__(self, brand, model, price, battery_life, network_speed):
        super().__init__(brand, model, price, battery_life)
        self.network_speed = network_speed

    def check_network_speed(self):
        print(
            f"{self.brand} {self.model} supports 5G speeds up to {self.network_speed} Mbps.")


phone1 = Smartphone("Apple", "iPhone 14", 999, 20)
phone2 = Smartphone5G("Samsung", "Galaxy S23 Ultra", 1200, 24, 2000)

print(phone1)
phone1.power_on()
phone1.battery_status()

print("\n")

print(phone2)
phone2.power_on()
phone2.check_network_speed()
