import secrets
from datetime import timedelta

from app.frameworks_and_drivers.server.flask_router import app, g

from app.adapters.api_presenter import ApiAuthTokenPresenter
from app.adapters.username_password_controller import UsernamePasswordController
from app.application.use_cases.username_password_auth \
    import UsernamePasswordAuthInteractor
from app.frameworks_and_drivers.database.sqlite3_db \
    import LowLevelEagerSQLite3Database
from app.frameworks_and_drivers.token.jwt_token import JWTTokenGenerator


if __name__ == "__main__":

    low_level_eager_sqlite3_db = LowLevelEagerSQLite3Database(db_name="test.db",
                                                              db_dir_path="./")

    secrets_hex = secrets.token_hex(32)
    one_hour = timedelta(hours=1)
    jwt_generator = JWTTokenGenerator(secret_key=secrets_hex,
                                      expiration_period=one_hour)

    presenter = ApiAuthTokenPresenter()
    username_password_interactor = UsernamePasswordAuthInteractor(
        data_access=low_level_eager_sqlite3_db,
        token_generator=jwt_generator,
        presenter=presenter
    )
    controller = UsernamePasswordController(
        use_case=username_password_interactor
    )

    g.controller = controller

    app.run(debug=True)
