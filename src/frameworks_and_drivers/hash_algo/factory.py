from typing import Any

from .hash_bcrypt import BCryptHashingAlgorithm
from ...application.interfaces.hash_algo \
    import HashingAlgorithm, HashingAlgorithmFactoryInterface, \
        HashingAlgorithmFactoryException


class HashingAlgorithmFactory(HashingAlgorithmFactoryInterface):
    def get_hash_algo(self,
                      name: str,
                      parameters: dict[str, Any]) -> HashingAlgorithm:
        match name.lower():
            case "bcrypt":
                prefix: str = parameters.get("prefix", "")
                bcrypt_algo = BCryptHashingAlgorithm(
                    name=parameters["name"],
                    rounds=int(parameters["rounds"]),
                    prefix=prefix.encode("utf-8")
                )
                return bcrypt_algo
            case "pbkdf2":
                raise NotImplementedError("pbkdf2 not implemented yet")
            case _:
                message = f"No implementation for {name} hashing algorithm."
                raise HashingAlgorithmFactoryException(message)
