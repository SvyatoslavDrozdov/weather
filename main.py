from get_information import get_weather, get_current_city

history_data_file = open("history.txt", mode="a+")


def add_to_history_data_file(weather):
    history_data_file.write("\n")
    for strings in weather:
        history_data_file.write(strings + "\n")


def read_from_history_data_file():
    request_history = []
    requests_number = -1
    history_data_file.seek(0)
    for strings in history_data_file:
        if strings != "\n":
            request_history[requests_number].append(strings.replace("\n", ""))
        else:
            request_history.append([])
            requests_number += 1

    return request_history


history = read_from_history_data_file()

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
        history_data_file.close()
        break

    elif choice == "1":
        print("Enter the name of the city:")
        city = input().strip()
        try:
            weather_information = get_weather(city)
        except TypeError:
            print("City not found.")

    elif choice == "2":
        city = get_current_city()
        weather_information = get_weather(city)

    elif choice == "3":
        if history:
            print("How many recent requests to display?")
            try:
                history_len = len(history)
                number_of_requests = int(input())
                number_of_requests = min(number_of_requests, history_len)
                for n in range(history_len - 1, history_len - number_of_requests - 1, -1):
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
        history_data_file.close()
        history_data_file = open("history.txt", mode="w")
        history_data_file.close()
        history_data_file = open("history.txt", mode="a+")
    else:
        print("No such option exists.")
        continue

    if weather_information:
        print("-------------------------------------------")
        for i in range(0, 5):
            print(weather_information[i])
        print("-------------------------------------------")
        history.append(weather_information)
        add_to_history_data_file(weather_information)

    print("\n")
