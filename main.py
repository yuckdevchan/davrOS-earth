import tomllib
import os

planet = int(input("planet:"))
year = int(input("year: "))

tests = ("population", "human progress")

population = ("size", "life expectancy", "birth rate", "death rate")

def read(file):
 with open(file, "rb") as f:
   data = tomllib.load(f)

def test_list_sub_categories(test_category):
  print("test sub-categories:")
  for i in user_test_category:
    print(i+1, test_category[i])
  print("end of sub-category list.")
  user_test_sub_category = input("test sub-category (e.g: 1': ")
  test_sub_category = eval(user_test_sub_category)
  file = os.path.join(str(test_category), str(test_sub_category) + ".toml")
  read(file)

def test_list():
  print("test categories:")
  for i in tests:
    print(i+1, tests[i])
  print("end of category list.")
  user_test_category = int(input("test category (e.g: 1: )"))
  test_category = eval(user_test_category)
  test_list_sub_categories(test_category)
