# Day 10 Functions with Outputs

def my_function():
    print("This is a simple function.")


my_function()


def input_function(something):
    print(f"This function had an input: {something}")


input_function("Inputed Something")


# This function has an input and output
# Convert name to title case
# DOCString is first line after def
def format_name(f_name, l_name):
    """Takes first (f_name) and last (l_name) name and formats and returns Title Case"""
    if f_name == "" or l_name == "":
        return "Missing data"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formated_name = format_name(input("What is your first name: "), input("What is your last name: "))
print(formated_name)

# or just call function in the print
print(format_name("HerSEY", "cArtWright"))