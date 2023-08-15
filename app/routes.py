from app import turnip_app


@turnip_app.route("/", methods=["GET"])
def index():
    return "<p>Index</p>"


@turnip_app.route("/hello_world/", methods=["GET"])
def hello_world():
    return "Hello World"
