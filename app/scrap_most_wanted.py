import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from scapper_crud import save_suspect_to_db
from config import init_db


BASE_URL = "https://crimestoppers-uk.org"

driver = None

init_db()


def get_selenium_page_content(url):
    driver.get(url)
    return driver.page_source


def parse_gallery(parsed_content):
    list_of_url_suspects = []
    gallery_list = parsed_content.find("div", class_="row wanted-gallery gallery-page")
    if gallery_list:
        for entry in gallery_list.find_all("div", class_="col-md-4 col-lg-3 d-flex"):
            link_tag = entry.find("a", href=True)
            list_of_url_suspects.append(link_tag["href"])
        return list_of_url_suspects
    return None


def parse_suspect(html_content):
    parsed_content = BeautifulSoup(html_content, "html.parser")
    suspect_info = parsed_content.find("div", class_="wanted-intro")

    suspect_details = {}
    if suspect_info:
        suspect_details["img_url"] = suspect_info.find("img")["src"]
        details_list = suspect_info.find("ul").find_all("li")

        for detail in details_list:
            key_untouched = detail.find("strong").text
            key = key_untouched.replace(":", "").strip().lower().replace(" ", "_")
            value = detail.text.replace(key_untouched, "").strip()
            suspect_details[key] = value

    summary_heading = parsed_content.find("h2", text="Summary")
    if summary_heading:
        suspect_details["summary"] = summary_heading.find_next_sibling(
            text=True
        ).strip()

    full_details_heading = parsed_content.find("h2", text="Full Details")
    if full_details_heading:
        suspect_details["full_details"] = full_details_heading.find_next_sibling(
            "p"
        ).text.strip()

    suspect_description_heading = parsed_content.find("h2", text="Suspect description")
    if suspect_description_heading:
        description_list = suspect_description_heading.find_next_sibling("ul").find_all(
            "li"
        )

        for description in description_list:
            key = (
                description.find("strong")
                .text.replace(":", "")
                .strip()
                .lower()
                .replace(" ", "_")
            )
            value = description.text.split(":")[-1].strip()
            suspect_details[key] = value

    return suspect_details


def craw_pages(base_url):
    gallery_list = f"{base_url}/give-information/most-wanted"
    page_number = 1

    while True:

        html_content = get_selenium_page_content(f"{gallery_list}/?page={page_number}")
        parsed_content = BeautifulSoup(html_content, "html.parser")

        suspect_urls = parse_gallery(parsed_content)

        if not suspect_urls:
            break

        for suspect_url in suspect_urls:
            full_suspect_url = f"{base_url}{suspect_url}"
            try:
                suspect_html_content = get_selenium_page_content(full_suspect_url)
                suspect_details = parse_suspect(suspect_html_content)
                save_suspect_to_db(suspect_details)
            except Exception as e:
                print(f"Error processing suspect at {full_suspect_url}: {str(e)}")

        page_number += 1
        time.sleep(1)


if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver_path = "/snap/bin/chromium.chromedriver"
    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    try:
        craw_pages(BASE_URL)
    finally:
        driver.quit()
