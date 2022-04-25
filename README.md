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

                                Описание классов и функций

У нас есть 7 классов Background,EventsGlobals,InputBox,Game_logic,Realization,Menu,Tamagochi

1)класс Tamagochi

    1)Имеет параметры 
        hunger,happines,time,date,date_of_birth каждая из них соответствует названию 

    2)Имеет методы 
        getinfo(считавания данных с прошлого запуска)
        setinfo(запись данных для следующего запуска)
        coverter(для перевода hh:mm:ss в s)
        to_top(Записывать время жизни в top.txt)

2)Класс Inputbox
(Создан для ввода текста пользователями)

    1)Имеет параметры 
        rect,color,text,txt_surface,active

    2)Имеет методы 
        handle_event(считывает event при нажатие мышкой на него переводится в активное состояние,при нажатие enter сохраняет текст,при нажатие backspace удаляет последний символ)
        update  (Обновляет размеры InputBox если вышли за его рамки)
        draw    (Чертит нашу коробку) 

3)Класс Background
(Создан для фотографии на заднем фоне)

    1)Имеет параметры
        image,rect

4)Класс Globals
(Создан для хранения глобальных переменных)

5)Класс Game_logic
(Хранит в себе логику самой игры)

    1)Имеет методы
        update_screen

        print_all_profiles (Печатает профили игрока)

        check_choosing_tamagochi (Смотрит на какой тамагочи кликнул игрок)

        draw_background (Рисует задний фон)

        place_tamagochi_picture (Располагает картинку тамагочи который выиграл на экран)

        making_textbox (Создание текстбоксов)

        render_textboxes (Вывод текст боксов на экран)

        hunger_button_pressed (При нажатия на кнопку покормить опускает голод на 3)

        live_button_pressed (При нажати на кнопку live начинает игру)

        button_happy (При нажатия на кнопку обнять опускает голод на 3)

        update_game(Обновляет экран(меняет голод и радость))

        mouse_is_hovered_on_button (При наводки на кнопку меняет цвет)

6)Класс Realization
(Реализация игровой логики)

    1)Имеет параметр 
        Класса Game_logic

    2)Имеет методы
        choosing_tamagochi (Располагает картинки всех тамагочи на экран чтобы выбрать)

        event_loop_of_choosing_tamagochi (Event loop для выбора тамагочи)

        main_event_loop (Основной event loop игры)

        get_profiles_length (Находит длину названия каждого профиля )

        clicked_profile (Ивент луп для выбора профиля)

        check_profiles_count (Проверка на то может ли игрок создать нового персонажа)

        start_new_profile (Запуск игры для новичка)

        start_old_profile (Запуск игры для старичка)

7)Класс Menu

    1)Имеет параметр
        screen
    
    2)Имеет методы
        screen_set (Создание экрана)

        top_tamagochi (Выведения топа тамагочи на экран)

        mouse_posesion (Анализатор позиции мышки)
        
        menu_event_loop (Event loop для menu)