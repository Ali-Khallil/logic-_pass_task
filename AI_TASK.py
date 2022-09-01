#Write a method that will remove any given character from a String?

Name = 'Ali Khalil'
Name.replace('A', '')
print(Name.replace('A', 'B'))



#Q/write a function that count how many the given character repeated in a given string?
test_str = "AIcoursee"
count = 0
for i in test_str:
    if i == 'e':
        count = count + 1

print("Count e in string is : "
      + str(count))