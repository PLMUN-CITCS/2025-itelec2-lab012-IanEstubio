# IAN JAY P. ESTUBIO 
# Week 04 - Conditional Statements
# Laboratory # 12 - Simulating a Switch Statement and Ternary Operator in Python

def main():
    """Main function to determine the day."""
    
    day_messages = {
        "monday": "Today is Monday.",
        "tuesday": "Today is Tuesday.",
        "wednesday": "Today is Wednesday.",
        "thursday": "Today is Thursday.",
        "friday": "Today is Friday.",
        "saturday": "Today is Saturday.",
        "sunday": "Today is Sunday."
    }

    day = input("Enter a day of the week: ").strip().lower()
    
    message = day_messages.get(day, "Invalid day entered.")
    
    day_type = "Weekend" if day in ("saturday", "sunday") else "Weekday"

    print(message)
    print("It's a", day_type + "!")

if __name__ == "__main__":
    main()
