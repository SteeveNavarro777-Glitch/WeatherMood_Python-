def weather_mood():
    print("🌦️ Welcome to WeatherMood Advisor!")
    weather = input("What's the weather like today? (sunny/rainy/cloudy): ").lower()
    mood = input("How are you feeling? (happy/sad/tired): ").lower()

    if weather == "sunny" and mood == "happy":
        print("☀️ Perfect day for a picnic!")
    elif weather == "rainy" and mood == "sad":
        print("🌧️ Cozy up with a book and hot chocolate.")
    elif weather == "cloudy" and mood == "tired":
        print("☁️ Take a nap and recharge.")
    else:
        print("✨ Just be yourself and enjoy the day!")

weather_mood()