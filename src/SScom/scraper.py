import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.97 Safari/537.36 Vivaldi/4.1.2369.21"
}


class SS:
    def __init__(self, url):
        self.url = url

    def _get_page_amount(self) -> int:
        page = requests.get(self.url, headers=HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")

        last_url = soup.find(class_="td2").findChild("a")["href"]
        page_amount = last_url[last_url.find("page") + 4 : last_url.find(".html")]
        print(f"Page amount = {page_amount}")

        return int(page_amount)

    def get_data(self) -> list:
        """Runs the scraper"""
        gpus_list = []
        for page_number in range(1, self._get_page_amount() + 1):
            url = self.url + f"/page{page_number}.html"
            page = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(page.content, "html.parser")

            # item ids
            ids = [tag["id"] for tag in soup.select("tr[id]")]  # creates list with ids
            # removes "tr_bnr" elements from list
            ids = [x for x in ids if "tr_bnr" not in x]
            ids.remove("head_line")  # removes first "head_line" id

            # getting item data
            for item_no, elem in enumerate(soup.find_all(id=ids)):
                print(f"Item {item_no + 1} on page {page_number}")

                # adverts url
                item = elem.find_all(class_="msga2-o pp6")  # gets url
                gpu = []
                for text in item:
                    gpu.append(text.get_text())
                for _ in range(3):
                    gpu.pop(1)

                # removes commas from prices
                gpu[1] = gpu[1].replace(",", "")

                # removes excessive symbols from price (€ and white-spaces)
                gpu[1] = gpu[1][:-3]

                # converts prices to float
                gpu[1] = float(gpu[1])

                gpus_list.append(gpu)

        gpus_list = sorted(gpus_list, key=lambda x: x[1])

        for index, gpu in enumerate(gpus_list):
            # convert price back to string and add `€`
            gpu[1] = str(gpu[1]) + " €"
            # transform 2D array to 1D
            gpus_list[index] = " - ".join(gpu)

        return gpus_list


gpus = SS("https://www.ss.com/lv/electronics/computers/completing-pc/video/sell")


def main():
    """Funcion to test scraper"""
    data = gpus.get_data()

    message_size = 100
    chunked_data = [
        data[i : i + message_size] for i in range(0, len(data), message_size)
    ]
    for i in chunked_data:
        print("\n".join(i))


if __name__ == "__main__":
    main()
