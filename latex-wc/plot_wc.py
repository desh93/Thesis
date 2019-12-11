import sys
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt

# plt.style.use("thesis")
import pandas as pd

thesis_meetings = [] # 2 august 2019

def main(filein):
    df = pd.read_csv(filein, header=None,
                     delim_whitespace=True,
                     names=["unix_time", "wc"])
    dates = pd.to_datetime(df["unix_time"], unit="s")
    #plt.xkcd()
    fig, ax = plt.subplots()
    ax.plot_date(dates, df["wc"], fmt='', linestyle="-", label="Word count")

    ax.set_ylabel("Word count")
    ax.set_xlabel("Date")
    # ax.axvline(datetime(2019, 7, 23), color="orange") # Started chapter 2
    # ax.axvline(datetime(2019, 8, 13), color="orange") # Finished chapter 4

    #ax.axvline(datetime(2019, 9, 20), color="black", label="Adam's submission")
    #ax.axvspan(datetime(2019, 5, 19), datetime(2019, 6, 2),
    #color="red", alpha=0.4, linewidth=0, label="IPAC")
    # ax.axvline(datetime(2019, 11, 8), color="orange", label="Deadline")

    #ax.axvspan(datetime(2019, 7, 19), datetime(2019, 7, 21),
    #           color="blue", alpha=0.4, linewidth=0,
    #           label="Helena's wedding")

    ax.legend(loc="upper left")
    # from IPython import embed; embed()

    # ax.set_yscale("log")
    # ax.axvline(datetime(2019, 11, 8), color="orange")

    plt.show()

if __name__ == '__main__':
    main("timestamped_wordcounts.txt")
    # main("timestamped_figurecounts.txt")
