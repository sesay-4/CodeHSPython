# fill in the arguments and function body
name = "Thelas"
letter= "e"
def name_contains(name, letter):
    name.find(letter)
    if name.find(letter) != -1:
        return True
    else:
        return False

print (name_contains(name, letter))
