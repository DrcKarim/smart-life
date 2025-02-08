from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year

    # Check if birthday has occurred this year  yes yes yes
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def get_horoscope(month, day):
    # Horoscope signs based on birth month and day
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Capricorn"

def get_age_category(age):
    if 0 <= age < 10:
        return "You are young."
    elif 10 <= age < 20:
        return "You are a child."
    elif 20 <= age < 30:
        return "You are an adult."
    elif 30 <= age < 40:
        return "You are in your thirties."
    elif 40 <= age < 50:
        return "You are in your forties."
    elif 50 <= age < 60:
        return "You are in your fifties."
    elif 60 <= age < 70:
        return "You are in your sixties."
    elif 70 <= age < 80:
        return "You are in your seventies."
    elif 80 <= age < 90:
        return "You are in your eighties."
    elif 90 <= age < 100:
        return "You are in your nineties."
    else:
        return "You are a centenarian or beyond."

def main():
    print("Welcome to the Age and Horoscope Calculator!")
    while True:
        try:
            print("\nEnter your birthdate:")
            
            # Validate day
            day_input = input("Day (1-31): ")
            if not day_input.isdigit():
                raise ValueError("Day must be a number between 1 and 31.")
            day = int(day_input)
            if not (1 <= day <= 31):
                raise ValueError("Day must be between 1 and 31.")
            
            # Validate month
            month_input = input("Month (1-12): ")
            if not month_input.isdigit():
                raise ValueError("Month must be a number between 1 and 12.")
            month = int(month_input)
            if not (1 <= month <= 12):
                raise ValueError("Month must be between 1 and 12.")
            
            # Validate year
            year_input = input("Year (e.g., 2000): ")
            if not year_input.isdigit():
                raise ValueError("Year must be a valid positive number.")
            year = int(year_input)
            if year <= 0:
                raise ValueError("Year must be a positive number.")
            
            # Create a birthdate object
            birth_date = datetime(year, month, day)
            age = calculate_age(birth_date)
            horoscope = get_horoscope(month, day)
            age_category = get_age_category(age)
            
            print(f"\nYou are {age} years old, and your horoscope is {horoscope}. {age_category}")
            
        except ValueError as e:
            print(f"\nError: {e}. Please try again.")
        
        # Ask if user wants to calculate another age
        choice = input("\nDo you want to calculate another age? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()