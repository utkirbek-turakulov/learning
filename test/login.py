import datetime
from playwright.sync_api import Playwright, sync_playwright


def login_page(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()
    page.set_viewport_size({"width": 1800, "height": 900})
    start_time = datetime.datetime.now()
    print(f"Test boshlandi: {start_time}")

    try:
        phone_number = "+998 90 200 20 20"
        page.goto("https://mohirdev.uz/blog/")
        page.click('.text-sm.btn.font-semibold.md\\:px-8\\.5.ml-2.px-8.py-3\\.5.shadow-none')  # click login button
        page.click('.PhoneInputInput')  # click phone number input
        page.locator('.PhoneInputInput').fill(f"{str(phone_number)}")  # fill phone number input

        page.click('.chakra-button.css-1ckhh3f')  # click continue button

        page.locator('.chakra-input.css-1ulvpvt').nth(0).click()  # click name
        page.locator('.chakra-input.css-1ulvpvt').nth(0).fill("login uchun yozilgan telefon raqam")  # fill name input
        page.locator('.chakra-input.css-1ulvpvt').nth(1).click()  # click surname
        page.locator('.chakra-input.css-1ulvpvt').nth(1).fill("ortga qaytsa ko'rinmayabdi")  # fill surname input
        page.go_back()
        input_value = page.locator('.PhoneInputInput').input_value()  # get phone number input value
        if str(input_value) == str(phone_number):
            print("kiritilgan telefon raqam mavjud")
        else:
            print(f"kiritilgan telefon raqam UI da ko'rinmayabdi: {input_value}")
        page.wait_for_timeout(5000)

    except Exception as e:
        print(f"Xatolik: {e}")
    finally:
        context.tracing.stop(path='login.zip')
        context.close()
        browser.close()


with sync_playwright() as playwright:
    login_page(playwright)
