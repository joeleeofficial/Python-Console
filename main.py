
user_color = "white"
console_color = "white"

pointer = "$JOE >"
pointer_color = "green"

# {} is the command given by the user
class error:
    syntax_error = "Error: '{}' is not a valid command."
    name_error = "Error: '{}' is not defined."
    type_error = "Error: wrong type for '{}'"
    invalid_parameter_error = "Error: {required_params} required parameters required and {optional_params} optional parameters needed but {params_given} given."


error_color = "red"

do_help_command = True
help_command = "help"

version = "1.5.2" 
language_name = "Blitz"
author = "JoeLee"

clear_command = ["clear","clr"] 





from inspect import signature as s, isfunction as f
from json import loads as parse, dumps as stringify
import config

colors = {
    "white": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "purple": "\033[35",
    "cyan": "\033[36m",
    "orange": "\033[33m"
}

def e(c):
    exec('global i; i = %s' % c)
    global i
    return i

try:
    user_color = colors[user_color]
    console_color = colors[console_color]
    pointer_color = colors[pointer_color]
    error_color = colors[error_color]
except:
    print("\033[31mInvalid colors in configuration.\033[0m")

if do_help_command:
    print("{} {} 2021 © Copyright \nAll Right Reserved By Joe Lee\n  > https://github.com/joeleeofficial".format(language_name,version,author))
else:
    print("{} {} 2021 © Copyright \nAll Right Reserved By Joe Lee\n> https://github.com/joeleeofficial".format(language_name,version,author))

help = '== Help ==\nHello There, I am Joe. A Programmer, Developer.'

while True:
    x = input(pointer_color + pointer + console_color + " ")
    if x.startswith(help_command + " ") and do_help_command:
        x = x.split(help_command + " ")[1]
        try:
            if f(e("config." + x)):
                print("== Help | " + x + " ==")
                h = []
                prm = [0,0]
                co = 0
                sig = s(e("config." + x.split(" ")[0]))
                for key in list(dict(sig.parameters).keys()):
                    if str(dict(sig.parameters)[key]).startswith("{}=".format(key)):
                        prm[1] += 1
                    else:
                        prm[0] += 1
                for i in str(s(e("config." + x)))[1:-1].split(", "):
                    if co <= prm[0]:
                        h.append("[" + i.split("=")[0] + "]")
                    else:
                        h.append("(" + i.split("=")[0] + ")")
                    co += 1
                print("Usage: " + x + " " + ' '.join(h) + "\nParams: " + " | ".join(str(s(e("config." + x)))[1:-1].split(",")))
        except:
            print(error_color + error.syntax_error.format(x))
  
    elif x in clear_command:
        print("\033c",end="",flush=True)
        if do_help_command:
            print("{} {} 2021 © Copyright \nAll Right Reserved By Joe Lee\n  > https://github.com/joeleeofficial Type Help For More Information".format(language_name,version,author))
        else:
            print("{} {} 2021 © Copyright \nAll Right Reserved By Joe Lee\n  > https://github.com/joeleeofficial Type Help For Information".format(language_name,version,author))
    elif x.strip() != "":
        y = x.split(" ")
        c = x.split(" ")[0]
        del(y[0])
        y = ','.join(y)
        sig = ''
        prm = [0,0]
        try:
            if f(e("config." + c)):
                sig = s(e("config." + x.split(" ")[0]))
                for key in list(dict(sig.parameters).keys()):
                    if str(dict(sig.parameters)[key]).startswith("{}=".format(key)):
                        prm[1] += 1
                    else:
                        prm[0] += 1
                if (len(y.split(",")) == prm[0] or y.split(",") == ['']) or len(y.split(",")) <= (prm[0] + prm[1]):
                    try:
                        if not y == "":
                            e("config." + c + "(" + y + ")")
                        else:
                            try:
                                e("config." + c + "()")
                            except:
                                print("<[function] {}>".format(c))
                    except TypeError:
                        print(error_color + error.type_error.format(x))
                    except NameError:
                        print(error_color + error.name_error.format(x))
                else:
                    print(error_color + error.invalid_parameter_error.format(required_params=prm[0],optional_params=prm[1],params_given=len(y.split(","))))

            else:
                raise AttributeError
        except (AttributeError, SyntaxError):
            print(error_color + error.syntax_error.format(x))
