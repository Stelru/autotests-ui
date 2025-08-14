import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible("username1")
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_empty_view()


new_course = {"title":          "Playwright",
              "estimated_time": "2 weeks",
              "description":    "Playwright",
              "max_score":      "100",
              "min_score":      "10"}


@pytest.mark.regression
@pytest.mark.courses
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_button()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_create_course_form(title="", estimated_time="", description="", max_score="0", min_score="0")
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image(file="./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form(title=new_course["title"],
                                               estimated_time=new_course["estimated_time"],
                                               description=new_course["description"],
                                               max_score=new_course["max_score"],
                                               min_score=new_course["min_score"])
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(title=new_course["title"],
                                                estimated_time=new_course["estimated_time"],
                                                max_score=new_course["max_score"],
                                                min_score=new_course["min_score"],
                                                index=0)
