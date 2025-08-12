from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_button = page.get_by_test_id("registration-page-registration-button")
        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        email_input.fill("user.name1@gmail.com")
        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        username_input.fill("username1")
        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        password_input.fill("password1")
        registration_button.click()
        context.storage_state(path='state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='state.json')
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        result_icon = page.get_by_test_id('courses-list-empty-view-icon')
        result_title = page.get_by_test_id('courses-list-empty-view-title-text')
        result_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text('Courses')
        expect(result_icon).to_be_visible()
        expect(result_title).to_be_visible()
        expect(result_title).to_have_text('There is no results')
        expect(result_text).to_be_visible()
        expect(result_text).to_have_text('Results from the load test pipeline will be displayed here')