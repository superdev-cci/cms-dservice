from commission.functions.fix_sale_maintain import WSFixBalance


def main():
    instance = WSFixBalance(mcode='TH2644655', round_code=113)
    instance.fix_ws_bonus()
    instance = WSFixBalance(mcode='TH2644655', round_code=114)
    instance.fix_ws_bonus()
