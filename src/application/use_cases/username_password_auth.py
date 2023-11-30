from ..data_transfer_objects.user import UserData, UserHash
from ..data_transfer_objects.username_password_auth_response_model \
    import UsernamePasswordAuthResponseModel
from ..interfaces.data import DataAccess
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
        self._token_generator = token_generator
        self._presenter = presenter

    def do(self, user_id: str, input_password: str):
        user_hash: UserHash = self._data_access.get_hash_by_user_id(user_id)
        user = User(user_id=user_id,
                    password_hash=user_hash.password_hash)
        response = UsernamePasswordAuthResponseModel()

        try:
            user.validate_password(input_password=input_password)
            token = self._token_generator.generate()
            response.message = "Authentication successful"
            response.token = token
            response.user_id = user_id
            response.success = True
        except UserException as user_exception:
            response.success = False
            response.message = str(user_exception)

        self._presenter.form_response(response)

    @property
    def presenter(self) -> UsernamePasswordAuthOutputBoundary:
        return self._presenter
