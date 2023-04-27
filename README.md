# Recipes Browser

Веб-сайт, предоставляющий возможность добавлять рецепты, которые будут видны в 
их профиле и общем каталоге.

## Используемые технологии





mkdir recipes_browser
cd recipes_browser
git clone https://github.com/myrzh/recipes_browser .
py -3.9 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python flask_app/run.py