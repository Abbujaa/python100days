# to dos when making modules
# independent functionality




def black_tea(name = "Tejas", should_add_sugar = True, tell_me = False)-> str:

    if tell_me :
        print("1. Boiling Water")
        print("2. Adding Powder")

        if should_add_sugar:
            print("3. Adding Sugar")

        print("4. Boiling Some More")
        print("5. Pouring in a cup")

        output = f"Black tea made for {name}!"
    if should_add_sugar:
        output = output + " (with sugar)"
    else:
        output = output + " (without sugar)"

    return output

def soda(name, type) -> str:
  output = f"{type} soda made for {name}!"
  return output

def family(names, preferences) -> list[str] | None:
  if len(names): # len(preferences)
    print("error")
    return

  return [black_tea(*item) for item in zip(names, preferences)]

print(family(["tejas", "shiva", "aman", "jazad", "ayush"], [True, True, False, False, True]))