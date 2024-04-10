from pages.swag_labs import SwagLabs
def test_check_icon(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    demo_qa_page.visit_name()
    demo_qa_page.visit_password()
