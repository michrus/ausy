from ..application.use_cases.username_password_auth \
    import UsernamePasswordAuthInteractor


class UsernamePasswordController:
    """_summary_
    """

    def __init__(self, use_case: UsernamePasswordAuthInteractor) -> None:
        self._use_case = use_case

    def username_password_auth(self, username: str, password: str) -> None:
        username_standardized = username.lower()
        self._use_case.do(username=username_standardized,
                          input_password=password)
