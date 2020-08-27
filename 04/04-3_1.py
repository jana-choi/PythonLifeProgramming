import usecsv

total = usecsv.opencsv("popSeoul.csv")

usecsv.switch(total)
print(total)