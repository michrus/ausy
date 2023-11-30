from flask import Flask, request, g

from ...adapters.username_password_controller import UsernamePasswordController


app = Flask(__name__)

def get_controller() -> UsernamePasswordController:
    if "controller" not in g:
        raise Exception("Controller object not found in Flask g object!")
    return g.controller


@app.route("/signin", methods=["POST"])
def sign_in():
    data = request.form
    user_id: str = data.get("user_id", "")
    password: str = data.get("password", "")

    controller = get_controller()
    controller.username_password_auth(user_id=user_id,
                                      password=password)
    presenter = controller.use_case.presenter

    return presenter.response
