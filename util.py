import sys
import datetime


def progressBar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length) - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("Percent: [{0}] {1}% \r".format(arrow + spaces, int(round(percent * 100))))
    # sys.stdout.flush()
    return


def progbar(message, curr, total, full_progbar=50, ):
    frac = curr / total
    filled_progbar = round(frac * full_progbar)
    print('\r', '#' * filled_progbar + '-' * (full_progbar - filled_progbar), '[{:>7.2%}]'.format(frac), '  ', message,
          end='')


def clear_line():
    print('\r', ' ' * 100)
    pass


def print_time_delta(stime, etime):
    diff = etime - stime
    # if delay.days > 0:
    #     out = str(delay).replace(" days, ", ":")
    # else:
    #     out = "0:" + str(delay)[:]
    #
    # out_ar = out.split(':')
    # out_ar = ["%02d" % (int(float(x))) for x in out_ar]
    # out = ":".join(out_ar)
    out = str(diff)
    return out[:10]
