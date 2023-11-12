from weather.get_information import get_weather, get_current_city

history = []
while True:
    weather_information = None

    print("-------------------------------------------")
    print("0 - Exit.")
    print("1 - View weather by city name.")
    print("2 - See the weather for my location.")
    print("3 - View request history.")
    print("4 - Delete request history.")

    print("-------------------------------------------")

    choice = input().strip()
    if choice == "0":
        break

    elif choice == "1":
        print("Enter the name of the city:")
        city = input().strip()
        try:
            weather_information = get_weather(city)
        except KeyError:
            print("City not found.")
        except TypeError:
            print("City not found.")

    elif choice == "2":
        city = get_current_city()
        weather_information = get_weather(city)

    elif choice == "3":
        if history:
            print("How many recent requests to display?")
            try:
                number_of_requests = int(input())
                number_of_requests = min(number_of_requests, len(history))
                for n in range(0, number_of_requests):
                    print(f"---------------Request № {n + 1}-----------------")
                    for i in range(0, 5):
                        print(history[n][i])
                    print("-------------------------------------------")
                if number_of_requests < 0:
                    print("Incorrect number.")
            except ValueError:
                print("Incorrect number.")
        else:
            print("Request history is empty.")

    elif choice == "4":
        history = []

    else:
        print("No such option exists.")
        continue

    if weather_information:
        print("-------------------------------------------")
        for i in range(0, 5):
            print(weather_information[i])
        print("-------------------------------------------")
        history.append(weather_information)

    print("\n")
