from header import *

PRINT_STATUS = False

def intro():
    intro = f"""{CYAN}
██████╗  ██████╗ ███╗   ██╗██╗   ██╗███████╗
██╔══██╗██╔═══██╗████╗  ██║██║   ██║██╔════╝
██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗
██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║
██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████║
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
    {RESET}"""

    print(intro)
    print("\n")

def get_data():
    try: 
        dataset = pd.read_csv(DATASET)
        data["x"] = np.array(dataset["km"])
        data["y"] = np.array(dataset["price"])

    except FileNotFoundError: sys.exit(ERR_READ)        
    except Exception: sys.exit(ERR_DATA)

    try:
        with open(SAVE_RESULT, "r") as f:
            raw= json.load(f)
    
        data["c"] = np.array(raw["c"])
        data["m"] = np.array(raw["m"])
        data["msc"] = np.array(raw["msc"])
        data["size"] = len(data["m"])
    
    except Exception: sys.exit(ERR_DATA)

def show_progress(frame):
    global PRINT_STATUS
    if (PRINT_STATUS):
        print(f"\033[{1}A", end='')
    PRINT_STATUS = True
    print(f"{YELLOW}1. Generating plot:{RESET} {int(frame / (data["size"] - 1) * 100)}%")

def create_info_box(ax_object):
    return ax_object.text(
        0.97, 
        0.97, 
        '', 
        transform=ax_object.transAxes,
        verticalalignment='top',
        horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    )

def render(frame, left_plot, right_plot, left_info, right_info):

    show_progress(frame)

    c = data["c"][frame]
    m = data["m"][frame]
    x = data["x"]
    msc = data["msc"][: frame]
    current_msc = data["msc"][frame]

    left_plot.set_data(x, c + (x * m))
    right_plot.set_data(np.arange(frame), msc)

    left_info.set_text(f"Iter: {frame}\nm: {m:.5f}\nc: {c:.6}")
    right_info.set_text(f"Iter: {frame}\nmsc: {current_msc:.1f}")

    return left_plot, left_info, right_plot, right_info

def plot_graph():
    fig, ax = plt.subplots(1,2, figsize=(16, 6))
    ax[0].scatter(data["x"], data["y"], marker="x", label="Data")

    ax[1].set_xlim(0, data["size"])

    # Round min/max to nearest 100,000
    y_min = int(np.floor(np.min(data["msc"]) / 100_000) * 100_000)
    y_max = int(np.ceil(np.max(data["msc"]) / 100_000) * 100_000)
    ax[1].set_ylim(y_min, y_max)

    # Set y-ticks every 100,000
    ax[1].set_yticks(np.arange(y_min, y_max + 1, 100_000))

    # Disable scientific notation
    ax[1].yaxis.set_major_formatter(ScalarFormatter())
    ax[1].ticklabel_format(style='plain', axis='y')

    left_plot, = ax[0].plot([], [], color="r", label="Learning Pattern")
    right_plot, = ax[1].plot([], [], color="g")

    left_info = create_info_box(ax[0])
    right_info = create_info_box(ax[1])

    ax[0].set_xlabel('km')
    ax[0].set_ylabel('price')
    ax[0].set_title('Linear Regression')

    ax[1].set_xlabel('Iteration')
    ax[1].set_ylabel('Mean Squared Error (MSE)')
    ax[1].set_title(f'Lost Function (Learning Rate = {LEARN_RATE})')

    ani = FuncAnimation(
        fig, 
        func=render,
        fargs=(left_plot, right_plot, left_info, right_info),
        frames=data["size"],
        interval=50,
        blit=True
    )

    ax[0].legend()
    ani.save("plot.gif", writer='pillow', fps=20)

def accuracy():
    # R square calculation
    y = data["y"]
    x = data["x"]
    m = data["m"][-1]
    c = data["c"][-1]    

    y_mean = np.mean(y)
    squareMean = np.sum((y - y_mean) ** 2)

    y_predict = x * m + c
    squarePredict = np.sum((y_predict - y_mean) ** 2)

    r_square = squarePredict  / squareMean
    print(f"{YELLOW}2. Precision calculation using r-square:{RESET} {r_square:.3}")

def main():

    intro()
    get_data()
    plot_graph()
    accuracy()
    print(f"{CYAN}Done...{RESET}")

if __name__ == "__main__":
    main()

