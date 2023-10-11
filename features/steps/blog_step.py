from behave import given, when, then

@then('Verify blog is opened')
def verify_opened(context):
    context.app.blog.verify_opened()

@then('Close blog')
def close_blog(context):
    context.app.blog.close_page()

@then('Returns to original window')
def return_to_original_window(context):
    context.app.blog.switch_to_window(context.original_window)
