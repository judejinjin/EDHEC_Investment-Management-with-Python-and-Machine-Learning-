# uncompyle6 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.10.16 | packaged by Anaconda, Inc. | (main, Dec 11 2024, 16:19:12) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: C:\Users\E_CHINI\OneDrive - EDHEC\Desktop\COURSERA_PYTHON\Lab 5 - Jan2021\Lab 5 - Jan2021\Jupyter Notebooks\regimeplot.py
# Compiled at: 2021-04-12 03:14:17
# Size of source mod 2**32: 2689 bytes
import matplotlib.pyplot as plt

class RegimePlot:

    def __init__(self, df, regime_col):
        self.df = df
        self.regime = regime_col
        self.regime_dates = self.get_regime_dates()

    def get_regime_dates(self):
        regime_dates = []
        crash_regime = 1
        normal_regime = 0
        regime = normal_regime
        for i, j, k in zip(self.df[self.regime], self.df["Date"], range(len(self.df))):
            if i == crash_regime:
                if regime == normal_regime:
                    regime_span = []
                    regime = crash_regime
                    regime_span.append(j)
                elif i == normal_regime and regime == crash_regime:
                    regime = normal_regime
                    regime_span.append(self.df["Date"].iloc[k - 1])
                    regime_dates.append(regime_span)
                if i == crash_regime and j == self.df["Date"].iloc[-1]:
                    regime_span.append(j)
                    regime_dates.append(regime_span)

        return regime_dates

    def plt_regime(self, plt_series: list, series_label: list, regime_label: str, log_scale=True, title=None, orj_series=False):
        plt.figure(figsize=(18, 6))
        plt.xlabel(" ")
        plt.ylabel(" ")
        if orj_series:
            for i in range(len(plt_series)):
                plt.plot((self.df["Date"]), (self.df[plt_series[i]]), label=(series_label[i]))

        else:
            for i in range(len(plt_series)):
                plt.plot((self.df["Date"]), ((1 + self.df[plt_series[i]]).cumprod()), label=(series_label[i]))

        if log_scale:
            plt.yscale("log")
        else:
            for i in range(len(self.regime_dates)):
                if i != len(self.regime_dates) - 1:
                    plt.axvspan((self.regime_dates[i][0]), (self.regime_dates[i][1]), alpha=0.3, color="grey")
                else:
                    plt.axvspan((self.regime_dates[i][0]), (self.regime_dates[i][1]), alpha=0.3, color="grey", label=regime_label)

            plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.16), fontsize=12, frameon=False, ncol=(len(plt_series) + 1))
            if title:
                plt.title(title, fontsize=18)
            else:
                plt.title("Cumulative Performance Over time", fontsize=18)
        plt.show()

# okay decompiling regimeplot.cpython-37.pyc
