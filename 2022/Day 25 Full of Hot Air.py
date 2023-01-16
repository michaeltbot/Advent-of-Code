to_decimal = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
to_SNAFU = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}

def SNAFU_to_decimal(snafu):
    n = to_decimal[snafu[-1]]
    power = 1
    for i in range(len(snafu)-2, -1, -1):
        power *= 5
        d = to_decimal[snafu[i]]
        n += d*power
    return n

def decimal_to_SNAFU(n):
    snafu = ""
    while n > 0:
        d = n % 5
        if d > 2:
            d -= 5
        snafu = to_SNAFU[d] + snafu
        n = (n - d)//5
    return snafu

with open("Day 25 Full of Hot Air.txt", "r") as f:
    decimal = sum(SNAFU_to_decimal(line.rstrip("\n")) for line in f if line != "\n")

result = decimal_to_SNAFU(decimal)
print(result)

