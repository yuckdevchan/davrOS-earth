import tomllib

planet = int(input("planet:"))
year = int(input("year: "))

tests = ("population", "human progress")

population = ("size", "life expectancy", "birth rate", "death rate")

def test_list():
  print("test categories:")
  for i in tests:
    print(i+1, tests[i])
  print("end of category list.")
  user_test_category = int(input("test category (e.g: 1)"))

def test_list_sub_categories():
  print("test sub-categories:")
  for i in user_test_category:
    print(i+1)

def read()
