from ..interfaces.database import DatabaseAccess, UserDTO
from ..interfaces.token import TokenGenerator
from ..interfaces.username_password_auth_response \
    import UsernamePasswordAuthBoundary, UsernamePasswordAuthResponseModel
from ...domain.user import User



class UsernamePasswordAuthInteractor:
    """_summary_
    """
    def __init__(self,
                 db_access: DatabaseAccess,
                 token_generator: TokenGenerator,
                 presenter: UsernamePasswordAuthBoundary) -> None:
        self._db_access = db_access
        self._token_generator = token_generator
        self._presenter = presenter

    def do(self, username: str, input_password: str):
        user_dto: UserDTO = self._db_access.get_user_by_username(username)
        user = User(username=user_dto.username,
                    password_hash=user_dto.password_hash)
        response = UsernamePasswordAuthResponseModel()

        if user.validate_password(input_password=input_password):
            try:
                response.token = self._token_generator.generate()
            except Exception as e:
                response.error_message = str(e.with_traceback())
        else:
            response.error_message = "Incorrect username or password"

        self._presenter.form_response(response)
