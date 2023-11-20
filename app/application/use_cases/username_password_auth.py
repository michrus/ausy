from ..dataclasses.user import UserData
from ..interfaces.database import DatabaseAccess
from ..interfaces.token_generator import TokenGenerator
from ..interfaces.username_password_auth_response \
    import UsernamePasswordAuthOutputBoundary, UsernamePasswordAuthResponseModel
from ...domain.user import User



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
        user = User(username=user_data.name,
                    password_hash=user_data.password_hash)
        response = UsernamePasswordAuthResponseModel()

        if user.validate_password(input_password=input_password):
            try:
                token = self._token_generator.generate()
                response.message = "Authentication successful"
                response.token = token
                response.user = user_data
                response.success = True
            except Exception as e:
                response.success = False
                response.message = str(e.with_traceback())
        else:
            response.success = False
            response.message = "Incorrect username or password"

        self._presenter.form_response(response)
