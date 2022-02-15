import json
from TrafficMonitor import TrafficMonitor

def main():
    f = open("./config.json", "r")
    config = json.load(f)
    print(config)

    tm = TrafficMonitor(config["home"], config["work"], config["api_key"])
    
    km, minute = tm.get_data()
    print(f"{km*1000/1000} Km, {minute*1000/1000} Minutes")

    km, minute = tm.get_data(False)
    print(f"{km*1000/1000} Km, {minute*1000/1000} Minutes")

if __name__ == '__main__':
    main()
