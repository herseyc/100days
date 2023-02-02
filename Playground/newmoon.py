import datetime

moon_phases = [
    "🌑 New Moon",
    "🌒 Waxing Crescent",
    "🌓 First Quarter",
    "🌔 Waxing Gibbous",
    "🌕 Full Moon",
    "🌖 Waning Gibbous",
    "🌗 Last Quarter",
    "🌘 Waning Crescent"
]

LUNAR_CYCLE = 29.53058770576
LUNAR_ORBIT = 27.32

currentdate = datetime.date.today()
#currentdate = datetime.date(year=2017, month=3, day=1)
jdn = currentdate.toordinal() + 1721424.5
print(f"JDN = {jdn}")

# 2451549.5 is 01/6/2000 - and the moon was new
newmoondate = datetime.date(year=2000, month=1, day=6)
nmd = newmoondate.toordinal() + 1721424.5
print(f"NMD = {nmd}")


dsn = jdn - nmd
print(f"Days Since Jan 6, 2000 New Moon = {dsn}")

newmoons = (dsn / LUNAR_CYCLE) % 1
print(f"Since last new moon = {newmoons}")
#newmoons = newmoons % 1
#print(f"New Moons Fractional = {newmoons}")

lunar_day = round(newmoons * LUNAR_CYCLE, 3)
print(f"It has been {lunar_day} days since the last New Moon")

if lunar_day <=1:
    print(moon_phases[0])
elif lunar_day <= 6.383:
    print(moon_phases[1])
elif lunar_day <= 8.383:
    print(moon_phases[2])
elif lunar_day <= 13.765:
    print(moon_phases[3])
elif lunar_day <= 15.765:
    print(moon_phases[4])
elif lunar_day <= 21.148:
    print(moon_phases[5])
elif lunar_day <= 23.148:
    print(moon_phases[6])
elif lunar_day <= 28.530:
    print(moon_phases[7])
else:
    print(moon_phases[0])








