divtionary_check = {
    "dic" : "dictionary",
    "wor" : "word",
    "jum" : "jump",
    1 : 2,
}
print(divtionary_check["jum"])
print(divtionary_check.get("dd" , "not a valid key"))
# using get one can pass default value