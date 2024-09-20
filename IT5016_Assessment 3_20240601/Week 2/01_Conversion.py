"""
converting 500 nzd into aus

converting 500 aus into nzd

Author Stefan Davis Smith Steunenberg

"""


amount_to_convert = 500
nz_to_aus_rate = 0.95
nzdollars = amount_to_convert

aus_dollars = nzdollars * nz_to_aus_rate
print("NZ $",nzdollars, "=AUS $",aus_dollars,sep="")

aus_dollars = amount_to_convert
nz_dollars = aus_dollars / nz_to_aus_rate
print("AUS $", aus_dollars,"= NZ $", nz_dollars,sep="")