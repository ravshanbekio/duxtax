class Car:
    def __init__(self, price, engine_volume, manufacture_year):
        self.price = price
        self.engine_volume = engine_volume
        self.manufacture_year = manufacture_year

    def calculate_customs_duty(self):
        if self.manufacture_year <= 1:
            if self.engine_volume <= 1000:
                customs_duty_rate = 0.00
            elif 1000 < self.engine_volume <= 1200:
                customs_duty_rate = 0.05
            else:
                customs_duty_rate = 0.15
        elif 1 < self.manufacture_year <= 3:
            customs_duty_rate = 0.30
        else:
            customs_duty_rate = 0.40
        return self.price * customs_duty_rate

    def calculate_vat(self):
        return self.price * 0.12

    def calculate_utilization_fee(self):
        if self.manufacture_year <= 3:
            if self.engine_volume <= 1000:
                base_calculation_amount = 30
            elif 1000 < self.engine_volume <= 2000:
                base_calculation_amount = 120
            elif 2000 < self.engine_volume <= 3000:
                base_calculation_amount = 180
            elif 3000 < self.engine_volume <= 3500:
                base_calculation_amount = 180
            else:
                base_calculation_amount = 300
        else:
            if self.engine_volume <= 1000:
                base_calculation_amount = 90
            elif 1000 < self.engine_volume <= 2000:
                base_calculation_amount = 210
            elif 2000 < self.engine_volume <= 3000:
                base_calculation_amount = 330
            elif 3000 < self.engine_volume <= 3500:
                base_calculation_amount = 390
            else:
                base_calculation_amount = 480
        return base_calculation_amount * 3454

    def calculate_customs_fee(self):
        return self.price * 0.002

    def calculate_total_cost(self):
        customs_duty = self.calculate_customs_duty()
        vat = self.calculate_vat()
        utilization_fee = self.calculate_utilization_fee()
        customs_fee = self.calculate_customs_fee()
        total_cost = self.price + customs_duty + vat + utilization_fee + customs_fee
        return total_cost

def main():
    price = float(input("Enter the price of the car in USD: "))
    engine_volume = float(input("Enter the engine volume of the car in cubic cm: "))
    manufacture_year = float(input("Enter the number of years since the car was manufactured: "))
    car = Car(price, engine_volume, manufacture_year)
    total_cost = car.calculate_total_cost()
    print(f"The total cost of importing the car to Uzbekistan is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
