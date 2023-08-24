def grocery_store(**kwargs):
   result = ""
   kwargs = sorted(kwargs.items(), key=lambda x: x[0])
   kwargs = sorted(kwargs, key=lambda x: len(x[0]), reverse=True)
   kwargs = sorted(kwargs, key = lambda x: x[1], reverse=True)

   for el in kwargs:
      result += f"{el[0]}: {el[1]}"+"\n"
   return result




print(grocery_store(bread=2,pasta=2,eggs=20,carrot=1,))

