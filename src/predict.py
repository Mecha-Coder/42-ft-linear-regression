from header import *

def intro():
    intro = f"""{CYAN}
 ██████╗ █████╗ ██████╗     ██████╗ ██████╗ ██╗ ██████╗███████╗    ██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗████████╗ ██████╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
██║     ███████║██████╔╝    ██████╔╝██████╔╝██║██║     █████╗      ██████╔╝██████╔╝█████╗  ██║  ██║██║██║        ██║   ██║   ██║██████╔╝
██║     ██╔══██║██╔══██╗    ██╔═══╝ ██╔══██╗██║██║     ██╔══╝      ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██║██║        ██║   ██║   ██║██╔══██╗
╚██████╗██║  ██║██║  ██║    ██║     ██║  ██║██║╚██████╗███████╗    ██║     ██║  ██║███████╗██████╔╝██║╚██████╗   ██║   ╚██████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    {RESET}"""

    print(intro)
    print(f"======================================")
    print(f"# {RED}To exit press Ctrl + C{RESET}")
    print(f"======================================")
    print("c = ", data["c"])
    print("m = ", data["m"])
    print("\n")


def init():
    try:
        with open(SAVE_RESULT, "r") as f:
            raw= json.load(f)
    
        data["c"] = raw.get("final_c", 0)
        data["m"] = raw.get("final_m", 0)
    
    except Exception: pass

def prompt_user():
    c = data["c"]
    m = data["m"]

    while True:

        try:
            user_input = input(USER_PROMPT)
            mileage = int(user_input)
           
            if 0 <= mileage <= 999999:
                price = c + (mileage * m)
                if (price < 0):
                    print(f"Price: ${0.00}")
                else:
                    print(f"Price: ${price:.2f}")
            else:
                print(ERR_OUT_OF_RANGE)
        
        except ValueError: print(ERR_INVALID_TYPE)
        except KeyboardInterrupt:
            print(f"\n{CYAN}Exiting program...{RESET}")
            break

def main():
  
    init()
    intro()
    prompt_user()

if __name__ == "__main__":
    main()