import matplotlib.pyplot as plt
import pandas
import statistics as stat

from core.mixin.month_mixin import MonthMixIn
from ecommerce.models import SaleInvoice


def generate_weight_histogram(current_date):
    sdate, edate = MonthMixIn.get_month_range(current_date)
    all_bill = SaleInvoice.objects.filter(total__gt=10, cancel=0, sadate__range=(sdate, edate))
    weight_series = []
    for b in all_bill:
        weight_series.append(b.bill_weight)

    # focus weight between 0.1 and 100 Kg
    filtered_weight = list(filter(lambda weight: 0 < weight <= 100, weight_series))
    serie = pandas.Series(filtered_weight)

    # serie = pandas.Series(weight_series)
    serie.plot.hist(grid=True, bins=[0, 1, 5, 10, 15, 20, 30, 50, 100], color='#449900', rwidth=0.95)
    plt.title("Weight Histogram (" + sdate.strftime("%Y-%b") + ")(0-1-5-10-15-20-30-50-100)")
    plt.xlabel('Weight (Kg)')
    plt.savefig("./weight_histogram_" + sdate.strftime("%Y-%b") + ".png", dpi=180)
    plt.cla()


def calculate_statistics(data_list):
    # Z score formula
    # z_score = (score - data_stat["mean"]) / data_stat["SD"])
    data_stat = {
        "mean": stat.mean(data_list),
        "median": stat.median(data_list),
        "SD": stat.stdev(data_list),
        "pop": {
            "0-5 Kg": len(list(filter(lambda weight: 0 < weight <= 5, data_list))) * 100 / len(data_list),
            "5-10 Kg": len(list(filter(lambda weight: 5 < weight <= 10, data_list))) * 100 / len(data_list),
            "10-15 Kg": len(list(filter(lambda weight: 10 < weight <= 15, data_list))) * 100 / len(data_list),
            "15-20 Kg": len(list(filter(lambda weight: 15 < weight <= 20, data_list))) * 100 / len(data_list),
            "20 Kg up": len(list(filter(lambda weight: 20 < weight, data_list))) * 100 / len(data_list)
        }
    }
    return data_stat
