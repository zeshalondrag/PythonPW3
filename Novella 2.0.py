import json
import os
import csv
import datetime

username = input("Введите имя пользователя: ")

def view_json_file():
    print("Чтобы вы смогли просмотреть JSON файл вам надо ввесли - название сохранения.json")
    filename = input("Введите название JSON файла: ")
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
            print(data)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")

def delete_save():
    print("Чтобы удалить сохранение вам достаточно написать его название")
    save_name = input("Введите название сохранения для удаления: ")
    try:
        os.remove(f"{save_name}.json")
        print(f"Сохранение '{save_name}' удалено.")
    except FileNotFoundError:
        print(f"Сохранение '{save_name}' не найдено.")

def load_save(save_name):
    try:
        with open(f"{save_name}.json", "r") as file:
            game_data = json.load(file)
            print(f"Сохранение '{save_name}' успешно загружено.")
    except FileNotFoundError:
        print(f"Сохранение '{save_name}' не найдено.")

def read_data_from_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def write_data_to_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

text = f"добро пожаловать '{username}' в текстовую игру новелла ведьмак"
print(text.upper())
locations = {
        1: "Новиград",
        2: "Острова Скеллиге",
        3: "Туссент(а)",
        4: "Каэр Морхен"
    }

chel = "Геральт"
ng = "\'Новиград\'"
isls = "\'Острова Скеллиге\'"
ts = "\'Туссент\'"
km = "Остаться в \'Каэр Морхен\'"

def menu():
    while True:
        print("Главное меню:")
        print("1 - Начать игру")
        print("2 - Настройки сохранения")
        print("3 - Закончить игру")
        choice = input("Выберите опцию: ")
        if choice == "1":
            novella()
        elif choice == "2":
            print("1 - Загрузить сохранение")
            print("2 - Удалить сохранение")
            print("3 - Просмотр сохранения")
            print("4 - Назад в главное меню")
            choice2 = input("Выберите опцию: ")
            if choice2 == "1":
                print("Чтобы загрузить сохранение вам достаточно написать его название")
                print("Выполняется загрузка сохранения...")
                save_name = input("Введите название сохранения: ")
                load_save(save_name)
            elif choice2 == "2":
                print("Выполняется удаление сохранения...")
                delete_save()
            elif choice2 == "3":
                print("Выполняется просмотр сохранения...")
                view_json_file()
            elif choice2 == "4":
                continue
            else:
                print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")
        elif choice == "3":
            text = "игра завершена!"
            print(text.capitalize())
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

def novella():
        print(f"- Вы {chel} из Ривии.")
        print("- Ему предстоит путешествовать по миру и искать себе приключения!")
        print(f"- Сейчас {chel} находиться в \'Каэр Морхен\'")
        print("Куда отправитесь:")
        print(f"1 - {ng}")
        print(f"2 - {isls}")
        print(f"3 - {ts}")
        print(f"4 - {km}")
        choice = input("Выберите место: ")
        if choice == "1":
            novigrad()
        elif choice == "2":
            islandskelegi()
        elif choice == "3":
            tyssent()
        elif choice == "4":
            kaer_morhen()
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 4.")

def novigrad():
    ng = locations[1]
    print(f"--\'Под угрозой {ng}\'--")
    print(f"- {chel} решил отправиться в {ng}")
    print(f"- {chel} прибыл в напряженный {ng}, чтобы выполнить важные задания и защитить горожан от опасности.")
    print("1 - Продолжить сюжет")
    print("2 - Альтернативный сюжет ")
    choice = input("Выберите действие (1 или 2): ")
    if choice == "1":
        print(f"- {chel} расследует убийства, встречает женщину, утверждающую, что вампиры виновны.")
        print("1 - Довериться")
        print("2 - Искать самому убийц")
        choice = input("Выберите развилку: ")
        if choice == "1":
            print("--\'Страшная правда\'--")
            print(f"- Если {chel} доверяет женщине, она помогает уничтожить вампиров, но оказывается сама вампиром, предлагая ему стать спутником вечности.")
            print("--\'Концовка\'--")
            print(f"- {chel} отклоняет предложение стать вампиром и продолжает борьбу с монстрами и тьмой, оставаясь верен своей судьбе.")
            print("Новелла завершена!")
            print("Выполняется сохранение...")
            print("1 - Сохраниться")
            choice = input("Выберите действие: ")
            if choice == "1":
                data = read_data_from_csv("data.csv")
                if username != "":
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data.append([username, current_time])
                    write_data_to_csv("data.csv", data)
                save_name = input("Введите название сохранения: ")
                game_data = {
                    "Глава": "--\'Страшная правда\'--",
                    "Концовка": "Была выбрана концовка \'Доверие\'"
                }
                with open(f"{save_name}.json", "w") as file:
                    json.dump(game_data, file)
                    menu()
        elif choice == "2":
            print("--\'Истина на свет\'--")
            print(f"- {chel} не доверяет женщине и продолжает расследование самостоятельно.")
            print("--\'Концовка\'--")
            print(f"- {chel} продолжает расследование в одиночку и, наконец, уничтожает вампиров, но тайна женщины остается нераскрытой.")
            print("Новелла завершена!")
            print("Выполняется сохранение...")
            print("1 - Сохраниться")
            choice = input("Выберите действие 1: ")
            if choice == "1":
                data = read_data_from_csv("data.csv")
                if username != "":
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data.append([username, current_time])
                    write_data_to_csv("data.csv", data)
                save_name = input("Введите название сохранения: ")
                game_data = {
                    "Глава": "--\'Истина на свет\'--",
                    "Концовка": "Была выбрана концовка \'Искатель убийц\'"
                }
                with open(f"{save_name}.json", "w") as file:
                    json.dump(game_data, file)
                    menu()
    elif choice == "2":
        print("--\'Загадочное зелье\'--")
        print(f"- {chel} находит аптеку с необычным зельем, заявляющим, что оно исцеляет все недуги.")
        print("1 - Продолжить сюжет")
        print("2 - Альтернативный сюжет ")
        choice = input("Выберите действие (1 или 2): ")
        if choice == "1":
            print(f"- Если {chel} решает купить зелье и выпить его, его раны заживают мгновенно, и...")
            print("--\'Концовка\'--")
            print(f"- {chel} выпив зелье, становится сначала непобедимым, но потом превращается в монстра. В поисках возвращения к человечности он исследует древние тексты и жертвует многими, наконец, находит способ вернуться к обычному состоянию, осознав важность контроля над собой.")
            print("Новелла завершена!")
            print("Выполняется сохранение...")
            print("1 - Сохраниться")
            choice = input("Выберите действие 1: ")
            if choice == "1":
                data = read_data_from_csv("data.csv")
                if username != "":
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data.append([username, current_time])
                    write_data_to_csv("data.csv", data)
                save_name = input("Введите название сохранения: ")
                game_data = {
                    "Глава": "--\'Загадочное зелье\'--",
                    "Концовка": "Была выбрана концовка \'Решительность = Важность\'"
                }
                with open(f"{save_name}.json", "w") as file:
                    json.dump(game_data, file)
                    menu()
        elif choice == "2":
            print(f"- Если {chel} игнорирует зелье, он продолжает приключение в Новиграде...")
            print("--\'Концовка\'--")
            print(f"- {chel} проигнорировал зелье и решил проблемы в Новиграде без нежелательных побочных эффектов, завоевав при этом признание жителей.")
            print("Новелла завершена!")
            print("Выполняется сохранение...")
            print("1 - Сохраниться")
            choice = input("Выберите действие 1: ")
            if choice == "1":
                data = read_data_from_csv("data.csv")
                if username != "":
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data.append([username, current_time])
                    write_data_to_csv("data.csv", data)
                save_name = input("Введите название сохранения: ")
                game_data = {
                    "Глава": "--\'Загадочное зелье\'--",
                    "Концовка": "Была выбрана концовка \'Лютый игнор\'"
                }
                with open(f"{save_name}.json", "w") as file:
                    json.dump(game_data, file)
                    menu()

def islandskelegi():
    isls = locations[2]
    print("--\'Таинственный остров\'--")
    print(f"- {chel} решил отправиться на {isls}")
    print(f"- Прибыв на Острова Скеллиге, {chel} обнаруживает спокойное побережье и красивые пейзажи.")
    print("- Внезапно, из глубин моря поднимается огромное морское чудовище!")
    print(f"- {chel} решает сразиться с морским чудовищем!")
    print("Сражение начинается!")
    class Character:
        def __init__(self, name, health):
            self.name = name
            self.health = health

        def is_alive(self):
            return self.health > 0

    class Geralt(Character):
        def __init__(self):
            super().__init__("Геральт", 100)

        def attack(self, monster):
            damage = 10
            monster.health -= damage
            print(f"{self.name} наносит {damage} урон своим мечом. Здоровье монстра составляет {monster.health}")

        def use_igni(self, monster):
            damage = 20
            monster.health -= damage
            print(f"{self.name} наносит {damage} урон с помощью Игни. Здоровье монстра теперь {monster.health}")

        def defend(self):
            heal = 20
            self.health = min(100, self.health + heal)
            print(f"{self.name} уходит в защиту. Выпив зелье \'Ласточку\' получает {heal}. Его здоровье {self.health}")

    class SeaMonster(Character):
        def __init__(self):
            super().__init__("Морское чудовище", 100)

        def attack(self, geralt):
            damage = 15
            geralt.health -= damage
            print(f"{self.name} атакует! У {geralt.name}'а здоровье сейчас {geralt.health}")

    geralt = Geralt()
    monster = SeaMonster()

    while geralt.is_alive() and monster.is_alive():
        print("\nВыберите свое действие: ")
        print("1 - Атаковать мечом")
        print("2 - Использовать знак Игни")
        print("3 - Защититься")
        choice = input()

        if choice == "1":
            geralt.attack(monster)
        elif choice == "2":
            geralt.use_igni(monster)
        elif choice == "3":
            geralt.defend()
        else:
            print("Недопустимое действие.")

        if monster.is_alive():
            monster.attack(geralt)

    print("\nБитва завершена.\n")

    if geralt.is_alive():
        print(f"{geralt.name} победил!")
        print("Выполняется сохранение...")
        print("1 - Сохраниться")
        choice = input("Выберите действие 1: ")
        if choice == "1":
            data = read_data_from_csv("data.csv")
            if username != "":
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data.append([username, current_time])
                write_data_to_csv("data.csv", data)
            save_name = input("Введите название сохранения: ")
            game_data = {
                "Глава": "--\'Таинственный остров\'--",
                "Битва": "Геральт смог одержать поюеду над морским монстром"
            }
            with open(f"{save_name}.json", "w") as file:
                json.dump(game_data, file)
                menu()
    else:
        print(f"{monster.name} победил!")
        print("Выполняется сохранение...")
        print("1 - Сохраниться")
        choice = input("Выберите действие 1: ")
        if choice == "1":
            data = read_data_from_csv("data.csv")
            if username != "":
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data.append([username, current_time])
                write_data_to_csv("data.csv", data)
            save_name = input("Введите название сохранения: ")
            game_data = {
                "Глава": "--\'Таинственный остров\'--",
                "Битва": "Морской монстр смог одержать победу над Геральтом"
            }
            with open(f"{save_name}.json", "w") as file:
                json.dump(game_data, file)
                menu()

inventory = []
def tyssent():
    tr = "сокровищниц"
    item = {
        1: "древнюю карту",
        2: "античные манускрипты",
        3: "древние артефакты",
        4: "магические свитки"
    }
    print(f"-- Прибытие в {ts} --")
    print(f"- {chel} из Ривии, снова отправился в новое приключение.")
    print(f"- Его следующая цель - загадочный город {chel}, известный своими тайнами и уникальными сокровищами.")
    print("- Город был окутан легендами, и многие считали его недоступным для чужаков.")
    print("1 - Продолжить сюжет")
    choice = input("Выберите действие 1: ")
    if choice == "1":
        print(f"- По прибытии в {ts}, {chel} столкнулся с недружелюбием местных жителей, которые были известны своей скрытностью.")
        choice = input("Выберите действие 1: ")
        if choice == "1":
            print("- Он решил исследовать город, надеясь разгадать его головоломки и раскрывать его секреты.")
            print("1 - Продолжить сюжет")
            choice = input("Выберите действие 1: ")
            if choice == "1":
                print("-- Поиск и сбор предметов --")
                print(f"- В своих приключениях, {chel} сталкивался с различными загадками и преградами, которые требовали умелого использования предметов, которые он находил по пути.")
                print("1 - Продолжить сюжет")
                choice = input("Выберите действие 1: ")
                if choice == "1":
                    print(f"- Он обнаружил {item[2]}, {item[3]} и {item[4]}, которые становились ему весьма полезными.")
                    inventory.append(f"{item[2]}")
                    inventory.append(f"{item[3]}")
                    inventory.append(f"{item[4]}")
                    print("В ваш инвентарь добавлено 3 предмета")
                    print("1 - Продолжить сюжет")
                    choice = input("Выберите действие 1: ")
                    if choice == "1":
                        print(f"- Однажды, он нашел {item[1]}, указывающую на забытую подземную руину, где, по легенде, спрятана великая сила.")
                        inventory.append(f"{item[1]}")
                        print("В ваш инвентарь добавлен 1 предмет")
                        print("1 - Продолжить сюжет")
                        choice = input("Выберите действие 1: ")
                        if choice == "1":
                            print(f"- {chel} использовал свой интеллект и навыки, чтобы разгадать загадки на пути к руинам и победить стражей, чтобы добраться до заветной {tr}'ы.")
                            print("1 - Продолжить сюжет")
                            choice = input("Выберите действие 1: ")
                            if choice == "1":
                                print(f"-- Раскрытие тайн {ts} --")
                                print(f"- По мере того как {chel} исследовал {ts}, он раскрывал давно забытые истории о городе.")
                                print("1 - Продолжить сюжет")
                                choice = input("Выберите действие 1: ")
                                if choice == "1":
                                    print(f"- Оказалось, что в прошлом {ts} был центром магии и тайных обрядов.")
                                    print("1 - Продолжить сюжет")
                                    choice = input("Выберите действие 1: ")
                                    if choice == "1":
                                        print(f"- {chel} узнал о таинственных орденах и их магических обертоних, которые были ключом к пониманию {ts}.")
                                        print("1 - Продолжить сюжет")
                                        choice = input("Выберите действие 1: ")
                                        if choice == "1":
                                            print("-- Финальное сражение --")
                                            print(f"- В конечном счете, {chel} столкнулся с самой большой тайной {ts} - древним драконом, который хранил {tr}'у города.")
                                            print("1 - Продолжить сюжет")
                                            choice = input("Выберите действие 1: ")
                                            if choice == "1":
                                                print(f"- Используя свои знания и предметы, которые он собрал на своем пути, {chel} вступил в схватку с драконом.")
                                                print("1 - Продолжить сюжет")
                                                choice = input("Выберите действие 1: ")
                                                if choice == "1":
                                                    print(f"- После жесткой битвы и с помощью мудрости, приобретенной в ходе своих приключений, {chel} смог победить дракона и получить доступ к {tr}'е {ts}.")
                                                    print("1 - Продолжить сюжет")
                                                    choice = input("Выберите действие 1: ")
                                                    if choice == "1":
                                                        print("-- Завершение приключения --")
                                                        print(f"- Получив доступ к {tr}'е, {chel} обнаружил древнее оружие и магические артефакты, которые могли быть использованы для защиты и спасения мира.")
                                                        print("1 - Продолжить сюжет")
                                                        choice = input("Выберите действие 1: ")
                                                        if choice == "1":
                                                            print(f"- Он покинул {ts}, но с собой унес не только сокровища, но и мудрость, которую приобрел в этом загадочном месте.")
                                                            print("1 - Продолжить сюжет")
                                                            choice = input("Выберите действие 1: ")
                                                            if choice == "1":
                                                                print(f"- Так завершилось его последнее приключение, но его жажда исследования и борьбы с монстрами продолжалась, и {chel} отправился в новую главу своей бессмертной саги.")
                                                                print(f"Ваш инвентарь: {inventory}")
                                                                print("Новелла завершена!")
                                                                print("Выполняется сохранение...")
                                                                print("1 - Сохраниться")
                                                                choice = input("Выберите действие 1: ")
                                                                if choice == "1":
                                                                    data = read_data_from_csv("data.csv")
                                                                    if username != "":
                                                                        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                                                        data.append([username, current_time])
                                                                        write_data_to_csv("data.csv", data)
                                                                    save_name = input("Введите название сохранения: ")
                                                                    game_data = {
                                                                        "Глава": f"-- Прибытие в {ts} --",
                                                                        "Концовка": "Таинственное сокровище",
                                                                        "Инвентарь": f"Вещи: {inventory}"
                                                                    }
                                                                    with open(f"{save_name}.json", "w") as file:
                                                                        json.dump(game_data, file)
                                                                        menu()

def kaer_morhen():
    chel = "Геральт"
    friends = "Ламбертом"
    print(f"- Герой {chel}, ведьмак охотник на монстров, прибывает в Каэр Морхен - обитель ведьмаков.")
    print(f"- Здесь он встречается со своим старым другом {friends}, который сообщает ему о странных происшествиях, происходящих в окрестностях.")
    print(f"-- Исход {locations[4]} -- ")
    print("1 - Кровавая угроза")
    print("2 - Тайна темных сил")
    choice = input("Выберите продолжение сюжета 1 или 2: ")
    if choice == "1":
        print("-- \'Кровавая угроза\' --")
        print(f"- {chel} расследует дело и обнаруживает, что племя ведьмаков, известное своей агрессивностью, намерено захватить {locations[4]}.")
        print("- Причиной этого является их недовольство жизнью в изоляции и ограничениями, которые налагаются на них в обители.")
        print("1 - Продолжить сюжет")
        choice = input("Выберите действие 1: ")
        if choice == "1":
            print(f"- {chel} приходится действовать быстро и эффективно.")
            print("- Он начинает собирать союзников среди верных друзей-ведьмаков и обитателей Каэр Морхена, убеждая их противостоять враждебному племени.")
            print(f"- {chel} проводит многочисленные разговоры, выступает в качестве посредника и старается примирить стороны. ")
            print(f"- Его задача - предотвратить битву и сохранить мир в {locations[4]}.")
            print("1 - Продолжить сюжет")
            choice = input("Выберите действие 1: ")
            if choice == "1":
                print(f"- Но усилия {chel}'a оказываются напрасными - вождь племени оказывается непреклонным и отказывается от любого компромисса.")
                print(f"- В результате неизбежно возникает конфликт, и {chel}'y приходится принять решение о начале битвы.")
                print("1 - Продолжить сюжет")
                choice = input("Выберите действие 1: ")
                if choice == "1":
                    print(f"- Битва разворачивается в эпическом сражении, где {chel} и его союзники сражаются против враждебного племени.")
                    print("- Ведьмак использует свои уникальные навыки и снаряжение, чтобы противостоять монстрам и воинам племени.")
                    print("1 - Продолжить сюжет")
                    choice = input("Выберите действие 1: ")
                    if choice == "1":
                        print(f"- Битва оказывается кровопролитной и жестокой, но благодаря мастерству и дружбе {chel} и его союзников, они одерживают победу, побеждая вождя и разбивая полчища врагов.")
                        print("1 - Продолжить сюжет")
                        choice = input("Выберите действие 1: ")
                        if choice == "1":
                            print("--\'Концовка\'--")
                            print(f"- {locations[4]} спасается от захвата, и жители обители могут продолжить свое существование в безопасности.")
                            print(f"- {chel} получает признание и благодарность за свои подвиги, и его имя становится еще более известным в ведьмачьем мире.")
                            print("Конец!")
                            print("1 - Сохраниться")
                            print("Выполняется сохранение...")
                            choice = input("Выберите действие 1: ")
                            if choice == "1":
                                data = read_data_from_csv("data.csv")
                                if username != "":
                                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                    data.append([username, current_time])
                                    write_data_to_csv("data.csv", data)
                                save_name = input("Введите название сохранения: ")
                                game_data = {
                                    "Глава": "-- \'Кровавая угроза\' --",
                                    "Концовка": "Была выбрана концовка \'Угроза? Не проблема\'",
                                }
                                with open(f"{save_name}.json", "w") as file:
                                    json.dump(game_data, file)
                                    menu()
    elif choice == "2":
        print("-- \'Тайна темных сил\' --")
        print(f"- {chel} продолжает расследование и раскрывает все больше деталей о загадочных происшествиях в {locations[4]}.")
        print("- Он узнает, что в замок проникла магическая энергия, которая вызывает хаос и разрушение. ")
        print(f"- С помощью своих чародейских навыков и сильной интуиции, {chel} раскрывает тайну этой магической сущности.")
        print("1 - Продолжить сюжет")
        choice = input("Выберите действие 1: ")
        if choice == "1":
            print(f"- По ходу расследования {chel} узнает, что это древний колдун, который стремится получить полный контроль над силами, заключенными в {locations[4]}, чтобы использовать их для своих зловещих целей.")
            print("- Он понимает, что время работает против него, и ему необходимо найти способ остановить колдуна до того, как тот обретет полный контроль над локацией.")
            print("1 - Продолжить сюжет")
            choice = input("Выберите действие 1: ")
            if choice == "1":
                print(f"- {chel} проводит тщательные расследования, изучает древние записи и консультируется с другими чародеями, чтобы разработать план действий.")
                print(f"- Он исследует запутанные коридоры и тайные комнаты {locations[4]}, сражается с опасными монстрами и преодолевает различные ловушки, которые колдун расставил на своем пути.")
                print("1 - Продолжить сюжет")
                choice = input("Выберите действие 1: ")
                if choice == "1":
                    print(f"- {chel} находит уязвимое место колдуна и использует это знание, чтобы нейтрализовать его. ")
                    print(f"- С помощью своих мастерских боевых навыков и магических заклинаний, {chel} сражается с колдуном в эпической схватке и, наконец, побеждает его, освобождая {locations[4]} от его зловещего влияния.")
                    print("1 - Продолжить сюжет")
                    choice = input("Выберите действие 1: ")
                    if choice == "1":
                        print("--\'Концовка\'--")
                        print(f"- {chel} спасает {locations[4]} и его обитателей от опасности, представляемой древним колдуном, и восстанавливает порядок и безопасность в этой локации.")
                        print("Конец!")
                        print("Выполняется сохранение...")
                        print("1 - Сохраниться")
                        choice = input("Выберите действие 1: ")
                        if choice == "1":
                            data = read_data_from_csv("data.csv")
                            if username != "":
                                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                data.append([username, current_time])
                                write_data_to_csv("data.csv", data)
                            save_name = input("Введите название сохранения: ")
                            game_data = {
                                "Глава": "-- \'Тайна темных сил\' --",
                                "Концовка": "Была выбрана концовка \'Магия вне Хогвартса запрещена!\'",
                            }
                            with open(f"{save_name}.json", "w") as file:
                                json.dump(game_data, file)
                                menu()
menu()