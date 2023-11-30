from ..application.use_cases.username_password_auth \
    import UsernamePasswordAuthInteractor


class UsernamePasswordController:
    """_summary_
    """

    def __init__(self, use_case: UsernamePasswordAuthInteractor) -> None:
        self._use_case = use_case

    def username_password_auth(self, user_id: str, password: str) -> None:
        user_id_standardized = user_id.lower()
        self._use_case.do(user_id=user_id_standardized,
                          input_password=password)

    @property
    def use_case(self) -> UsernamePasswordAuthInteractor:
        return self._use_case
