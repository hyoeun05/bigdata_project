from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_monday_webtoons_info():
    """네이버 웹툰 월요 전체 웹툰 목록에서 정보를 수집합니다."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    url = "https://comic.naver.com/webtoon/weekday.nhn?weekday=mon"
    driver.get(url)
    time.sleep(2)  # 페이지 로딩 대기

    webtoon_list = driver.find_elements(By.CSS_SELECTOR, '#content > div.list_area.daily_img > ul > li')
    webtoon_data = []

    for webtoon in webtoon_list:
        try:
            thumbnail_url = webtoon.find_element(By.CSS_SELECTOR, 'div.thumb > a > img').get_attribute('src')
            title = webtoon.find_element(By.CSS_SELECTOR, 'div.info > h5 > a').text
            author = webtoon.find_element(By.CSS_SELECTOR, 'div.info > p > a').text
            rating_element = webtoon.find_element(By.CSS_SELECTOR, 'div.info > div.rating_type > strong')
            rating = float(rating_element.text)

            webtoon_data.append({
                'thumbnail_url': thumbnail_url,
                'title': title,
                'author': author,
                'rating': rating
            })
        except Exception as e:
            print(f"데이터 추출 중 오류 발생: {e}")

    driver.quit()
    return webtoon_data

if __name__ == "__main__":
    monday_webtoons_info = get_monday_webtoons_info()
    for webtoon in monday_webtoons_info:
        print(f"타이틀: {webtoon['title']}")
        print(f"작가: {webtoon['author']}")
        print(f"평점: {webtoon['rating']}")
        print(f"썸네일 URL: {webtoon['thumbnail_url']}")
        print("-" * 30)