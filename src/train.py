from header import *

def intro():
    intro = f"""{CYAN}
████████╗██████╗  █████╗ ██╗███╗   ██╗    ███╗   ███╗ ██████╗ ██████╗ ███████╗██╗     
╚══██╔══╝██╔══██╗██╔══██╗██║████╗  ██║    ████╗ ████║██╔═══██╗██╔══██╗██╔════╝██║     
   ██║   ██████╔╝███████║██║██╔██╗ ██║    ██╔████╔██║██║   ██║██║  ██║█████╗  ██║     
   ██║   ██╔══██╗██╔══██║██║██║╚██╗██║    ██║╚██╔╝██║██║   ██║██║  ██║██╔══╝  ██║     
   ██║   ██║  ██║██║  ██║██║██║ ╚████║    ██║ ╚═╝ ██║╚██████╔╝██████╔╝███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚══════╝
    {RESET}"""

    print(intro)
    print(f"# =============================================================")
    print(f"# Train using Gradient Decent Algorithm")
    print(f"# To determine linear regression y = mx + c values for (m) & (c) ")
    print(f"# That best fit dataset {BOLD}[{DATASET}]{RESET}")
    print(f"# =============================================================")
    print(f"# Start training with:")  
    print(f"    {BOLD}c = {INIT_C}")
    print(f"    m = {INIT_M}{RESET}")
    print(f"# Other parameters:")
    print(f"    {BOLD}Learning rate  = {LEARN_RATE}")
    print(f"    Converge limit = {CONVERGE_LIMIT:.5f}{RESET}")  
    print("\n")

def show_progress(i, c, m, overwrite=False):

    if (overwrite):
        print(f"\033[{3}A", end='')

    print(f"{YELLOW}Iteration ={RESET} {i}")
    print(f"{YELLOW}m ={RESET} {m}")
    print(f"{YELLOW}c ={RESET} {c}")

def get_data():
    
    try: 
        dataset = pd.read_csv(DATASET)
        x_actual = np.array(dataset["km"])
        y_actual = np.array(dataset["price"])
    
    except FileNotFoundError: sys.exit(ERR_READ)        
    except Exception: sys.exit(ERR_DATA)

    # Check if enough data for training
    if (len(dataset) < 5 and len(x_actual) == len(y_actual)):
        sys.exit(ERR_SMALL)

    data["x_actual"] = x_actual 
    data["y_actual"] = y_actual 
    data["size"] = len(dataset)

def normalize_data():
    x = data["x_actual"]
    y = data["y_actual"]

    data["x_norm"] = (x - np.min(x)) / (np.max(x) - np.min(x))
    data["y_norm"] = (y - np.min(y)) / (np.max(y) - np.min(y))

def train_model():
    x = data["x_norm"]
    y = data["y_norm"]
    s = data["size"]
    c = INIT_C
    m = INIT_M

    show_progress(0, INIT_C, INIT_M)

    x_range = np.max(data["x_actual"]) - np.min(data["x_actual"])
    y_range = np.max(data["y_actual"]) - np.min(data["y_actual"])
    
    data["m"] = []
    data["c"] = []
    data["msc"] = []

    for i in range(ITERATION_LIMIT):
        
        # Compute the sum of errors
        y_pred = x * m + c
        sumError_c = y_pred - y
        sumError_m = (y_pred - y) * x
        squareError = (y_pred - y) ** 2

        # Compute the step size
        step_c = LEARN_RATE * (1/s) * np.sum(sumError_c)
        step_m = LEARN_RATE * (1/s) * np.sum(sumError_m)
        mean_square_error = np.sum(squareError) / (2 * s)

        # Break loop if step is converging
        if (abs(step_c) < CONVERGE_LIMIT and abs(step_m) < CONVERGE_LIMIT):
            break
        
        # Adjust new m & c value
        c = c - step_c
        m = m - step_m

        # De-normalize c and m values, used for graph plotting
        m_denorm = m * (y_range / x_range)
        c_denorm = (c * y_range) + np.min(data["y_actual"]) - (m_denorm * np.min(data["x_actual"]))
        data["m"].append(m_denorm)
        data["c"].append(c_denorm)
        data["msc"].append(mean_square_error)
        show_progress(i + 1, c_denorm, m_denorm, True)
        time.sleep(0.05)

def save_result():

    with open(SAVE_RESULT, "w") as f:
        json.dump({
            "final_c": data["c"][-1], 
            "final_m": data["m"][-1],
            "m": data["m"],
            "c": data["c"],
            "msc": data["msc"]
        }, f)
    
    print(f"\n{CYAN}Done training {RESET} 👍")
    print(f"Result save in [{SAVE_RESULT}]")

def main():
    intro()
    get_data()
    normalize_data()
    train_model()
    save_result()

if __name__ == "__main__":
    main()