import json
import sys
import matplotlib.pyplot as plt
from matplotlib import cycler


def plot_results(results):
    for name, step in results.items():
        x = []
        y = []
        try:
            for bitstring, count in step["output-distribution"][
                "bitstring_distribution"
            ].items():
                x.append(bitstring)
                y.append(count)
        except KeyError:
            for bitstring, count in step["results"].items():
                x.append(bitstring)
                y.append(count)
        finally:
            if len(x) == 0:
                print(f"Couldn't find any results in step {name}")
            else:
                plot(x, y)


def plot(x, y):
    colors = cycler("color", ["#00b578", "#ff3863"])
    plt.rc(
        "axes",
        facecolor="#E6E6E6",
        edgecolor="none",
        axisbelow=True,
        grid=True,
        prop_cycle=colors,
    )
    plt.rc("grid", color="w", linestyle="solid")
    plt.rc("xtick", direction="out", color="gray")
    plt.rc("ytick", direction="out", color="gray")
    plt.rc("patch", edgecolor="#E6E6E6")
    plt.rc("lines", linewidth=2)
    plt.bar(x, y)
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <results_file>")
        sys.exit(-1)
    file_name = sys.argv[1]
    print(f"Plotting results from {file_name}")
    with open(file_name) as f:
        results = json.load(f)
        plot_results(results)
