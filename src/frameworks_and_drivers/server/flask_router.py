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
    username: str = data.get("username", "")
    password: str = data.get("password", "")

    controller = get_controller()
    controller.username_password_auth(username=username,
                                      password=password)
    presenter = controller.use_case.presenter

    return presenter.response
