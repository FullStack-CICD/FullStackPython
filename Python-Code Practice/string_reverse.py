def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str


str =reverse("Rahul")
print(str)