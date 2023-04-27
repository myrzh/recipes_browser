from flask import (
    Flask, 
    render_template, 
    redirect
)

from flask_login import (
    LoginManager,
    current_user,
    login_user,
    login_required,
    logout_user,
)
from forms.user import (
    LoginForm,
    RegisterForm,
    AddingForm,
    AccountForm,
    RecipeForm
)

from data import db_session
from data.users import User
from data.recipes import Recipe


"""Инициализация."""
app = Flask(__name__)
app.config["SECRET_KEY"] = "so_secret_key"
login_manager = LoginManager()
login_manager.init_app(app)
db_session.global_init("flask_app/db/db.sqlite")


@app.route("/")
@app.route("/index")
def index():
    """Все не приватные рецепты."""
    db_sess = db_session.create_session()

    return render_template(
        "index.html", 
        recipes=db_sess.query(Recipe).filter(Recipe.is_private == False)
    )


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    """Вход в систему."""
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")

        return render_template(
            "login.html", 
            message="Неверный логин или пароль.", 
            form=form
        )
    return render_template(
        "login.html", 
        title="Авторизация", 
        form=form
        )


@app.route("/")
@app.route("/register", methods=["GET", "POST"])
def reqister():
    """Регистрация в системе."""
    form = RegisterForm()
    if form.validate_on_submit():

        if form.password.data != form.password_again.data:
            return render_template(
                "register.html",
                title="Регистрация",
                form=form,
                message="Пароли не совпадают.",
            )

        db_sess = db_session.create_session()
        
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template(
                "register.html",
                title="Регистрация",
                form=form,
                message="Такой пользователь уже существует.",
            )

        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()

        return redirect("/login")
    return render_template(
        "register.html", 
        title="Регистрация", 
        form=form
        )


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/")
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """Добавление рецепта."""
    form = AddingForm()
    if form.validate_on_submit():
        user_id = current_user.id

        recipe = Recipe(
            title=form.Title.data,
            ingridients=form.Ingridients.data,
            text=form.Text.data,
            is_private=form.is_private.data,
            user_id=user_id,
        )

        db_sess = db_session.create_session()
        db_sess.add(recipe)
        db_sess.commit()

        return redirect("/")
    return render_template("adding.html", form=form)


@app.route("/")
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    """Получение рецепта."""
    form = RecipeForm()

    db_sess = db_session.create_session()
    recipe_id = int(recipe_id)
    recipe = db_sess.query(Recipe).filter(Recipe.id == recipe_id).first()

    return render_template(
        "recipe.html",
        form=form,
        recipe=recipe,
    )


@app.route("/")
@app.route("/account/<name>")
def account(name):
    """Получение аккаунта пользователя. Переход в свой аккаунт."""
    if current_user.is_authenticated:
        if name == current_user.name:
            form = LoginForm()

            db_sess = db_session.create_session()
            user_id = current_user.id
            user = db_sess.query(User).filter(User.id == user_id).first()
            recipes = db_sess.query(Recipe).filter(Recipe.user_id == user_id)

            return render_template(
                "my_account.html",
                form=form,
                recipes=recipes,
                user=user,
            )

        else:
            form = AccountForm()

            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.name == name).first()
            recipes = db_sess.query(Recipe).filter(
                Recipe.user_id == user.id, Recipe.is_private == False
            )

            return render_template(
                "account.html",
                form=form,
                recipes=recipes,
                user=user,
            )
