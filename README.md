Процесс установки и запуска

    1.Клонируйте репозиторий: git clone https://github.com/teagad/python_project.git

    2.Войти в директорию python_project: cd python_project

    3.Переключитесь на ветку dev: git switch dev
    
    4.Выполните установку pygame,numpy: pip3 install pygame && pip3 install numpy
    
    5.Запустить код: python3 main.py

Что же код делает?

    Нужно войти либо в существующий профиль либо создать новый, затем выбрать одного из 3 х животных.
    Игра о питомцах за которыми вы должны ухаживать и не дать умереть.
    У него есть две характеристики happines и hunger вы не должны дать hunger превзойти отметку 40 а happines спустится до
    1
    (питомец будет помогать вам говоря когда он голоден или хочет поиграть) для этого у вас есть кнопки hug и feed нажимая
    на которые вы поднимаете happines на 3 или отпускаете hunger на 3.
    За минуту у вас будут падать характеристики на 1 и в офлайн и в онлайн режиме.