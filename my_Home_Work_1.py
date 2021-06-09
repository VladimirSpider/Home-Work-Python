#!/usr/bin/env python
# coding: utf-8

# In[1]:

carBrand = ["Audi", "BMW", "Mercedes", "Opel", "Volvo"]
Audi = ["Audi", "A5", "A6",["Дизель", "Бензин" , "Гибрид", "Электромобиль"]]
BMW = ["BMW", "5", "7",["Дизель", "Бензин" , "Гибрид", "Электромобиль"]]
Mercedes = ["Mercedes", "E-class", "S-class",["Дизель", "Бензин" , "Гибрид", "Электромобиль"]]
Opel = ["Opel", "Corsa", "Insignia",["Дизель", "Бензин" , "Гибрид", "Электромобиль"]]
Volvo = ["Volvo", "S90", "XC90",["Дизель", "Бензин" , "Гибрид", "Электромобиль"]]
variable = True
print("Добрый день, вы хотите приобрести автомобиль?\nДля продолжения нажмите Y. Если хотите уйти нажмите N.")
while variable:
     answer = input("Я ввел: ")
     if answer.lower() == "n":
          print("До скорых встреч!")
          break
     elif answer.lower() == "y":
          while variable:
               print("В нашем автосалоне вы можете купить автомобили следующих марок:")
               for item in carBrand:
                    print("-" + item)
               buy_carBrand = input("Введите марку автомобиля, который вы хотите приобрести: ")
               if buy_carBrand in carBrand:
                    while variable:
                         print("Выберите модель марки " + buy_carBrand + ": ")
                         if buy_carBrand in Audi:
                              carBrandModel = Audi
                         if buy_carBrand in BMW:
                              carBrandModel = BMW
                         if buy_carBrand in Mercedes:
                              carBrandModel = Mercedes
                         if buy_carBrand in Opel:
                              carBrandModel = Opel
                         if buy_carBrand in Volvo:
                              carBrandModel = Volvo
                         i = 0
                         while i < len(carBrandModel):
                              if carBrandModel[i] != carBrandModel[0] and type(carBrandModel[i]) != list:
                                   print("-" + str(carBrandModel[i]))
                              i +=1
                         buy_carBrandModel = input("Введите модель автомобиля " + buy_carBrand + ", которую вы хотите приобрести: ")
                         if buy_carBrandModel in carBrandModel:
                              while variable:
                                   print("Выберите двигатель марки " + buy_carBrand + " у модели " + buy_carBrandModel + ": ")
                                   i = 0
                                   while i < len(carBrandModel):
                                        if type(carBrandModel[i]) == list:
                                             for item in carBrandModel[i]:
                                                  print("-" + item)
                                        carBrandModelEngine = carBrandModel[i]
                                        i += 1
                                   buy_carBrandModelEngine = input("Введите двигатель автомобиля " + buy_carBrand + " у модели " + buy_carBrandModel + ", который вы хотите приобрести: ")
                                   if buy_carBrandModelEngine in  carBrandModelEngine:
                                        print("Вы выбрали следующую машину марки: " + buy_carBrand + "\nМодель: " + buy_carBrandModel + "\nДвигатель: " + buy_carBrandModelEngine)
                                        print("С вами свяжется наш менеджер и вы вместе подберете комплектацию вашей машины. Ожидайте.")
                                        variable = False
                                   else: print("Ткого двигателя мы не предлагаем!")
                         else: print("Такую модель мы не предлагаем!")
               else: print("Такую марку мы не предлагаем!")
     else: print("Вы ввели что-то не то!")


# In[ ]:




