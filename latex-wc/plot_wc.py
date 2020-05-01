import sys
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
#plt.style.use("thesis")#
# plt.xkcd()
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
    ax.axvline(datetime(2020, 3, 23), color="orange",linestyle="dotted", label="Lockdown Starts") # Started chapter 2
    #ax.axvline(datetime(2020, 4, 01), color="orange") # Finished chapter 4

    # ax.axvline(datetime(2020, 3, 20), color="black", label="Lewis's submission")
    ax.axvline(datetime(2020, 4, 29), color="green", linestyle="dotted", label="Lewis's viva")
    ax.axvline(datetime(2020, 4, 27), color="red", linestyle="dotted", label="2nd circulation")
    ylim = ax.get_ylim()
    ax.axvspan(datetime(2019, 12, 20), datetime(2020, 3, 1),color="red", alpha=0.3, linewidth=0, label="Analysis push")

    # ax.axvline(datetime(2019, 11, 8), color="orange", label="Deadline")

    #ax.axvspan(datetime(2019, 7, 19), datetime(2019, 7, 21),
    #           color="blue", alpha=0.4, linewidth=0,
    #           label="Helena's wedding")

    ax.legend(loc="upper left",frameon=0)
    # from IPython import embed; embed()

    # ax.set_yscale("log")
    # ax.axvline(datetime(2019, 11, 8), color="orange")

    plt.show()

if __name__ == '__main__':
    main("timestamped_wordcounts.txt")
#    main("timestamped_figurecounts.txt")
