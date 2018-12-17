# flask_finek :thinking:

## Установка

Скорее всего, у вас нет библиотеки для виртуальной среды, поэтому установите её

pip install virtualenv

Затем установите сам flask

pip install flask

Затем введите следующую команду в консоль. (Мы и сами не знаем, зачем она. Правда)

virtualenv venv

Или

\pyth\Scripts\virtualenv.exe venv

Теперь создаём виртуальную среду
py -3 -m venv venv

Теперь войдём в среду:

venv\Scripts\activate

Теперь вы как бы работаете от имени среды. Введите в консольку вот это

pip install Flask

Теперь можно работать и создавать приложения.

## Работать и создавать, угу

Создайте py файл с содержимым hello_world.py

теперь вот это введите

C:\Users\User\Desktop\flask\ex.py>set FLASK_APP=ex.py
