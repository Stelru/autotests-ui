import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage

new_course = {"title":          "Playwright",
              "estimated_time": "2 weeks",
              "description":    "Playwright",
              "max_score":      "100",
              "min_score":      "10"}

edited_course = {"title":          "PW",
              "estimated_time": "3 weeks",
              "description":    "PW",
              "max_score":      "80",
              "min_score":      "1"}

@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_empty_courses_list(self,courses_list_page: CoursesListPage):
        courses_list_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        courses_list_page.sidebar.check_visible()
        courses_list_page.navbar.check_visible("username1")
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()


    def test_create_course(self,courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(title="", estimated_time="", description="", max_score="0", min_score="0")
        create_course_page.create_exercise_toolbar.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(title=new_course["title"],
                                                   estimated_time=new_course["estimated_time"],
                                                   description=new_course["description"],
                                                   max_score=new_course["max_score"],
                                                   min_score=new_course["min_score"])
        create_course_page.create_course_form.check_visible(title=new_course["title"],
                                                            estimated_time=new_course["estimated_time"],
                                                            description=new_course["description"],
                                                            max_score=new_course["max_score"],
                                                            min_score=new_course["min_score"])
        create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=False)
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(title=new_course["title"],
                                                    estimated_time=new_course["estimated_time"],
                                                    max_score=new_course["max_score"],
                                                    min_score=new_course["min_score"],
                                                    index=0)

    def test_edit_course(self,courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_form.fill(title=new_course["title"],
                                                   estimated_time=new_course["estimated_time"],
                                                   description=new_course["description"],
                                                   max_score=new_course["max_score"],
                                                   min_score=new_course["min_score"])
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.course_view.check_visible(title=new_course["title"],
                                                    estimated_time=new_course["estimated_time"],
                                                    max_score=new_course["max_score"],
                                                    min_score=new_course["min_score"],
                                                    index=0)
        courses_list_page.course_view.menu.click_edit(index=0)
        # по хорошему можно сделать отдельные   компоненты на  апдейт  карточки (в реальных ситуациях вполне возможны отличия),
        # но у нас  локаторы там полностью совпадают с созданием + в требованиях по заданию небыло про добавление новых компонентов :)
        create_course_page.create_course_form.fill(title=edited_course["title"],
                                                   estimated_time=edited_course["estimated_time"],
                                                   description=edited_course["description"],
                                                   max_score=edited_course["max_score"],
                                                   min_score=edited_course["min_score"])
        create_course_page.create_course_toolbar.click_create_course_button()
        courses_list_page.course_view.check_visible(title=edited_course["title"],
                                                    estimated_time=edited_course["estimated_time"],
                                                    max_score=edited_course["max_score"],
                                                    min_score=edited_course["min_score"],
                                                    index=0)