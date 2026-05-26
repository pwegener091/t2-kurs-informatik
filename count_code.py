wort = "codednskcolekdkdcopekdlcodecodecoleekr"

count = 0
for i in range(len(wort)-3):
    neues_wort = wort[i:i+4]
    if neues_wort[:2] == "co" and neues_wort[3] == "e":
        count += 1

print(count)