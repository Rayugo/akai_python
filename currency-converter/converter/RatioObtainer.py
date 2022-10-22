import json, datetime, urllib.request, requests
from os.path import exists

class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise

        if not exists("ratios.json"):
            return False
        
        date_today = datetime.datetime.today()
        date_today = date_today.date()
        with open("ratios.json", "r") as outfile:
            fetched_data = json.load(outfile)
            found = False
            for i in fetched_data:
                date_fetched = datetime.datetime.strptime(i["data_fetched"], "%Y-%m-%d")
                date_fetched = date_fetched.date()
                if (
                    i["base_currency"] == self.base and
                    i["target_currency"] == self.target
                ):
                    found = True
                    if date_fetched < date_today:
                        return False
            return found

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it

        url = f"https://api.exchangerate.host/latest?base={self.base}&symbols={self.target}"
        response = requests.get(url)
        data = response.json()
        self.save_ratio(float(data["rates"][self.target]))

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        
        today = str(datetime.date.today())
        date_today = datetime.datetime.today()
        date_today = date_today.date()

        data = {
            "base_currency": self.base,
            "target_currency": self.target,
            "data_fetched": today,
            "ratio": ratio
        }

        saved = False

        if not exists("ratios.json"):
            with open("ratios.json", "w") as outfile:
                data = [data]
                json.dump(data, outfile, indent=1)
                saved = True
        
        # Update JSON file
        if not saved: 
            with open("ratios.json", "r+") as outfile:
                fetched_data = json.load(outfile)
                for i in fetched_data:
                    if (
                        self.base == i["base_currency"] and
                        self.target == i["target_currency"]
                    ):
                        i["data_fetched"] = today
                        i["ratio"] = ratio
                        saved = True
                        outfile.seek(0)
                        json.dump(fetched_data, outfile, indent=1)
                        break
        
        # Save JSON file with new data
        if not saved:
            with open("ratios.json", "r+") as outfile:
                fetched_data = json.load(outfile)
                fetched_data.append(data)
                outfile.seek(0)
                json.dump(fetched_data, outfile, indent=1)

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        
        with open("ratios.json", "r") as outfile:
            fetched_data = json.load(outfile)
            for i in fetched_data:
                if(
                    i["base_currency"] == self.base and
                    i["target_currency"] == self.target
                ):
                    return float(i["ratio"])


