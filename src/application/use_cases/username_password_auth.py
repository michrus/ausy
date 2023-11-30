from ..data_transfer_objects.user_hash import UserHash
from ..data_transfer_objects.user_hash_algo import UserHashAlgorithm
from ..data_transfer_objects.username_password_auth_response_model \
    import UsernamePasswordAuthResponseModel
from ..interfaces.data import DataAccess, DataAccessException
from ..interfaces.hash_algo \
    import HashingAlgorithm, HashingAlgorithmFactory, \
        HashingAlgorithmFactoryException
from ..interfaces.token_generator import TokenGenerator
from ..interfaces.username_password_auth_response \
    import UsernamePasswordAuthOutputBoundary
from ...domain.user import User, UserException


class UsernamePasswordAuthInteractor:
    """_summary_
    """
    def __init__(self,
                 data_access: DataAccess,
                 token_generator: TokenGenerator,
                 presenter: UsernamePasswordAuthOutputBoundary) -> None:
        self._data_access = data_access
        self._hash_algo_factory = HashingAlgorithmFactory()
        self._token_generator = token_generator
        self._presenter = presenter

    def do(self, user_id: str, input_password: str):
        response = UsernamePasswordAuthResponseModel()
        try:
            user_hash: UserHash = \
                self._data_access.get_hash_by_user_id(user_id=user_id)
            user = User(user_id=user_id,
                        password_hash=user_hash.password_hash)

            user_hash_algo: UserHashAlgorithm = \
                self._data_access.get_hash_algo_by_user_id(user_id=user_id)
            hash_algo: HashingAlgorithm = self._hash_algo_factory.get_hash_algo(
                name=user_hash_algo.hash_algorithm,
                parameters=user_hash_algo.algorithm_parameters
            )

            input_password_hash = hash_algo.hash(input_password)

            user.validate_password(input_password_hash=input_password_hash)
            token = self._token_generator.generate()

            response.message = "Authentication successful"
            response.token = token
            response.user_id = user_id
            response.success = True
        except (UserException,
                DataAccessException,
                HashingAlgorithmFactoryException) as exception:
            response.success = False
            response.message = str(exception)

        self._presenter.form_response(response)

    @property
    def presenter(self) -> UsernamePasswordAuthOutputBoundary:
        return self._presenter
