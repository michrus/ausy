from dataclasses import dataclass
from typing import Any

@dataclass
class UserHashAlgorithm:
    user_id: str
    hash_algorithm: str
    algorithm_parameters: dict[str, Any]
