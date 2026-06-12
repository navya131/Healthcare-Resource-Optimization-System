from dataclasses import asdict, dataclass


@dataclass
class Resource:
    resource_name: str
    resource_type: str
    quantity: int
    available_quantity: int
    status: str = "Active"

    def to_dict(self):
        return asdict(self)
