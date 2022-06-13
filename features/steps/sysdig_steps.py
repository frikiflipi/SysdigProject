# ---------------------------------------------------------------------------
# Created By  : Guillermo Navarro
# Created Date: 13/06/2022
# version ='1.0'
# Comment: Definition of test steps
# ---------------------------------------------------------------------------

from behave import given, when, then


@given('I am on "{url}"')
def step(context, url):
    context.helperfunc.open(url)


@when('I set email to "{email}"')
def enter_email(context, email):
    context.helperfunc.find_by_id('ember1666').send_keys(email)


@when('I set password to "{password}"')
def enter_password(context, password):
    context.helperfunc.find_by_id('ember1667').send_keys(password)


@when('I click login button')
def click_on_login_button(context):
    context.helperfunc.find_by_id('ember1676').click()


@then('I get message denying the access')
def see_invalid_message(context):
    msg = context.helperfunc.find_by_xpath('//*/p[@class="login__error-display"]').text
    assert msg == "Credentials are not valid"


@then('I can login')
def i_am_on_login_page(context):
    title = context.helperfunc.find_by_xpath('//*/div[@class="css-11u27a6"]').text
    assert title == "What to expect with Sysdig Monitor"


@when('I click on forgot your password')
def click_on_forgot_your_password(context):
    context.helperfunc.find_by_id('ember1680').click()


@when('I set recovery email to "{email}"')
def enter_recovery_email(context, email):
    context.helperfunc.find_by_id('ember1729').send_keys(email)


@when('I click on password reset button')
def click_on_password_reset(context):
    context.helperfunc.find_by_id('ember1730').click()


@then('I get message saying the password has been sent')
def see_password_sent_message(context):
    msg = context.helperfunc.find_by_xpath('//*/p[@class="login__feedback-message"]').text
    print(msg)
    assert "We just sent the password reset email to" in msg
