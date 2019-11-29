from decimal import Decimal, getcontext

# plot_num:1..plot_numまで表示する
# plot_limited_num:最大表示数+1
# plot_digits:表示桁数(0001=4,001=3)

plot_num = 1000
plot_limited_num = 10000
plot_limited_num_c = plot_limited_num
plot_digits = 0
while (plot_limited_num_c % 10 == 0):
    plot_limited_num_c /= 10
    plot_digits += 1
getcontext().prec = plot_num*plot_digits-2
plot1to100 = (Decimal(1) / (Decimal(plot_limited_num-1) * Decimal(plot_limited_num-1))) * Decimal(plot_limited_num)
plot1to100 = str(plot1to100)[2:]
for i in range(plot_num):
    print(plot1to100[i*plot_digits:(i+1)*plot_digits])