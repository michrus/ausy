from ..data_transfer_objects.user import UserData, UserHash
from ..data_transfer_objects.username_password_auth_response_model \
    import UsernamePasswordAuthResponseModel
from ..interfaces.database import DatabaseAccess
from ..interfaces.token_generator import TokenGenerator
from ..interfaces.username_password_auth_response \
    import UsernamePasswordAuthOutputBoundary
from ...domain.user import User, UserException



class UsernamePasswordAuthInteractor:
    """_summary_
    """
    def __init__(self,
                 db_access: DatabaseAccess,
                 token_generator: TokenGenerator,
                 presenter: UsernamePasswordAuthOutputBoundary) -> None:
        self._db_access = db_access
        self._token_generator = token_generator
        self._presenter = presenter

    def do(self, username: str, input_password: str):
        user_data: UserData = self._db_access.get_user_by_username(username)
        user_hash: UserHash = self._db_access.get_hash_by_user_id(user_data.id)
        user = User(user_id=user_data.id,
                    username=user_data.name,
                    email=user_data.email,
                    access_level=user_data.access_level,
                    password_hash=user_hash.password_hash)
        response = UsernamePasswordAuthResponseModel()

        try:
            user.validate_password(input_password=input_password)
            token = self._token_generator.generate()
            response.message = "Authentication successful"
            response.token = token
            response.user = user_data
            response.success = True
        except UserException as user_exception:
            response.success = False
            response.message = str(user_exception)

        self._presenter.form_response(response)
