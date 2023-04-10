from app import main_app
# from users import RegisterResource, LoginResource


# @main_app.route("/", defaults={"path": ""})
# @main_app.route("/a<path:path>")
# @main_app.route("/u<path:path>")
# def root(path):
#     main_app.send_static_file("index.html")


# # main_app.api.add_resource(RegisterResource, "/api/register")
# # main_app.api.add_resource(LoginResource, "/api/login")

if __name__ == "__main__":
    main_app.run(debug=True)
