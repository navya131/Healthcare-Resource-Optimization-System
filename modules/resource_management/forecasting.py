import random


def resource_forecast():

    return {
        "Ventilator":
            random.randint(10, 50),

        "Oxygen":
            random.randint(20, 100),

        "Equipment":
            random.randint(50, 200)
    }