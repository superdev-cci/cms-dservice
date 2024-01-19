from commission.models import WeakStrongSummary, WeekCommission


class WSFixBalance:
    def __init__(self, mcode, round_code, *args, **kwargs):
        self.member = mcode
        self.select_round = round_code
        self.commission = WeekCommission.objects.get(mcode=mcode, rcode=round_code)
        self.ws_summary = WeakStrongSummary.objects.get(mcode=mcode, rcode=round_code)

    def fix_ws_bonus(self):
        ws_bonus = float(self.ws_summary.balance * self.ws_summary.ws_factor)
        self.ws_summary.total = ws_bonus
        self.ws_summary.tax = ws_bonus * 0.05
        self.ws_summary.totalamt = ws_bonus - self.ws_summary.tax
        self.ws_summary.save()

        self.commission.ws_bonus = ws_bonus
        self.commission.total = ws_bonus + float(self.commission.fast_bonus)
        self.commission.save()
