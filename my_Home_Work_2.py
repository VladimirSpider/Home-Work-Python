order = "Ваша игра:\n"
###################
type1 = "Логическая"
type2 = "Экономическая"
type3 = "Романтическая"
type4 = "Пошаговая"
###################
genre1 = "Стратегическая"
genre2 = "Головоломка"
genre3 = "Дедуктивная"
genre4 = "Реакция и координация"
###################
number_of_players1 = "1"
number_of_players2 = "2 - 4"
number_of_players3 = "5 - 8"
number_of_players4 = "более 8"
###################
time1 = "10 минут"
time2 = "20 минут"
time3 = "60 минут"
time4 = "2 часа"
###################
age1 = "5 лет"
age2 = "10 лет"
age3 = "16 лет"
age4 = "Для взрослых"
###################
language1 = "Русский"
language2 = "Английский"
language3 = "Немецкий"
language4 = "Французский"
###################
print("Вы хотите купить настольную игру?\nВведите YES или NO")
while True:
     answer = input("Ваш ответ: ")
     if answer == "YES":
          print("=" * 40, "\nSTEP №1")
          print("Выбирите тип настольной игры:\n-type1 - Логическая; \n-type2 - Экономическая; \n-type3 - Романтическая; \n-type4 - Пошаговая.")
          STEP1 = input("Введите тип настольной игры: ")
          if STEP1 == type1 or STEP1 == type2 or STEP1 == type3 or STEP1 == type4:
               order = order + "-Тип: " + STEP1 + "\n"
          else:
               order = order + "-Тип: " + STEP1 + "(Информация введена не корректно!)" + "\n"
          print("=" * 40, "\nSTEP №2")
          print("Выбирите жанр настольной игры:\n-genre1 - Стратегическая; \n-genre2 - Головоломка; \n-genre3 - Дедуктивная; \n-genre4 - Реакция и координация.")
          STEP2 = input("Введите жанр настольной игры: ")
          if STEP2 == genre1 or STEP2 == genre2 or STEP2 == genre3 or STEP2 == genre4:
               order = order + "-Жанр: " + STEP2 + "\n"
          else:
               order = order + "-Жанр: " + STEP2 + "(Информация введена не корректно!)" + "\n"
          print("=" * 40, "\nSTEP №3")
          print("Выбирите колличество игроков для настольной игры:\n-number of players1 - 1 ; \n-number of players2 - 2 - 4 ; \n-number of players3 - 5 - 8; \n-number of players4 - более 8.")
          STEP3 = input("Введите колличество игроков для настольной игры: ")
          if STEP3 == number_of_players1 or STEP3 == number_of_players2 or STEP3 == number_of_players3 or STEP3 == number_of_players4:
               order = order + "-Колличество игроков: " + STEP3 + "\n"
          else:
               order = order + "-Колличество игроков: " + STEP3 + "(Информация введена не корректно!)" + "\n"
          print("=" * 40, "\nSTEP #4")
          print("Выбирите время на партию для настольной игры:\n-time1 - 10 минут; \n-time2 - 20 минут; \n-time3 - 60 минут; \n-time4 - 2 часа.")
          STEP4 = input("Введите время на партию для настольной игры: ")
          if STEP4 == time1 or STEP4 == time2 or STEP4 == time3 or STEP4 == time4:
               order = order + "-Время на партию: " + STEP4 + "\n"
          else:
               order = order + "-Время на партию: " + STEP4 + "(Информация введена не корректно!)" + "\n"
          print("=" * 40, "\nSTEP #5")
          print("Минимальный возраст для настольной игры:\n-age1 - 5 лет; \n-age2 - 10 лет; \n-age3 - 16 лет; \n-age4 - Для взрослых.")
          STEP5 = input("Введите возраст настольной игры: ")
          if STEP5 == age1 or STEP5 == age2 or STEP5 == age3 or STEP5 == age4:
               order = order + "-Возраст: " + STEP5 + "\n"
          else:
               order = order + "-Возраст: " + STEP5 + "(Информация введена не корректно!)" + "\n"
          print("=" * 40, "\nSTEP #6")
          print("Выберите язык настольной игры:\n-language1 - Русский; \n-language2 - Английский; \n-language3 - Немецкий; \n-language4 - Французский.")
          STEP6 = input("Введите язык настольной игры: ")
          if STEP6 == language1 or STEP6 == language2 or STEP6 == language3 or STEP6 == language4:
               order = order + "-Язык: " + STEP6 + "\n"
          else:
               order = order + "-Язык: " + STEP6 + "(Информация введена не корректно!)" + "\n"
          print("=" * 40)
          print(order)
          break
     elif answer == "NO":
          print("Досвидание!")
          break
     else:
          print("Вы ввели что-то не то!")
print("Спасибо за покупку!")





