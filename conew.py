def gregorian_to_jd(year, month, day):  
   if month < 3:  
      month += 12  
      year -= 1  
   a = int(year / 100)  
   b = 2 - a + int(a / 4)  
   jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + b - 1524.5  
   return jd  
  
def jd_to_hijri_shamsi(jd):  
   hijri_shamsi_epoch = 1948320.5  
   hijri_shamsi_year = int((jd - hijri_shamsi_epoch) / 365.242198781)  
   remainder = (jd - hijri_shamsi_epoch) % 365.242198781  
   if remainder < 0:  
      hijri_shamsi_year -= 1  
      remainder += 365.242198781  
   month_lengths = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]  
   hijri_shamsi_month = 0  
   while remainder >= month_lengths[hijri_shamsi_month]:  
      remainder -= month_lengths[hijri_shamsi_month]  
      hijri_shamsi_month += 1  
   hijri_shamsi_day = int(remainder) + 1  
   return hijri_shamsi_year + 1, hijri_shamsi_month, hijri_shamsi_day  
  
def gregorian_to_hijri_shamsi(year, month, day):  
   jd = gregorian_to_jd(year, month, day)  
   hijri_shamsi_year, hijri_shamsi_month, hijri_shamsi_day = jd_to_hijri_shamsi(jd)  
   month_names = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"]  
   return f"{hijri_shamsi_day} {month_names[hijri_shamsi_month - 1]} {hijri_shamsi_year}"  
  
def main():  
   print("Gregorian to Hijri Shamsi Date Converter")  
   year = int(input("Enter the year (Gregorian): "))  
   month = int(input("Enter the month (Gregorian, 1-12): "))  
   day = int(input("Enter the day (Gregorian, 1-31): "))  
  
   hijri_shamsi_date = gregorian_to_hijri_shamsi(year, month, day)  
   print(f"The Hijri Shamsi date for {year}/{month}/{day} is: {hijri_shamsi_date}")  
  
if __name__ == "__main__":  
    main()
