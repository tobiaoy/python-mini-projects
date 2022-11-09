# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ______"
youtuber = "Kurtis Conner" # some string variable

# a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {youtuber}".format(youtuber=youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
celebrity = input("Celebrity: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {celebrity}!"

print(madlib)