import numpy as np
import matplotlib.pyplot as plt


def main():

    x = np.linspace(0.1, 10, 500)
    y = -5 * np.cos(10 * x) * np.transpose(np.sin(3 * x)) / np.sqrt(x)

    plt.figure(figsize=(10, 6))

    plt.plot(x, y,
             label=r"$Y(x) = \frac{-5 \cos(10x) \sin(3x)}{\sqrt{x}}$",
             color="forestgreen",
             linestyle="-",
             linewidth=2)

    plt.title("Func graph", fontsize=14)
    plt.xlabel("X", fontsize=12)
    plt.ylabel("Y", fontsize=12)

    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(loc="upper right", fontsize=12)
    plt.show()


if __name__ == "__main__":
    main()
