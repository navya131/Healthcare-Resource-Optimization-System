import random


def predict_workload():

    return {
        "expected_patients":
            random.randint(50, 250),

        "required_staff":
            random.randint(10, 40)
    }