-------------------------
Design Decisions
-------------------------
Although I never used "Behave" before, I thought it was a good opportunity to
use it and learn about it. Because it is the first time I use it I am sure
there will be several things that could be defined in a better way that the
actual implementation that I have chosen.

I have built this tests on Windows

 * Framework: Behave
 * Language: Python 3.10
 * IDE: PyCharm
 * Web automation: Selenium

-------------------
Dependencies
-------------------
There are some dependencies that must be installed:
 > pip install behave
 > pip install selenium
 > pip install ConfigParser

Additionally it will be needed to add the chrome webdriver and include it
into the path of the OS. It can be downloaded from:

 * https://chromedriver.chromium.org/downloads


----------------------
Command Line
----------------------

Example:  behave .\features\login.feature

------------------------------
Possible improvements
------------------------------
There are several improvements to do in case more time was allocated
1) Use selenium grid to perform parallel tests
2) Use different browsers
3) Test input restrictions for email field
4) Actual test that the email after "forgot password" is received
5) Get fields based on class and text instead of ID, this way the same steps
   could be used for different sites (EU Central, US East, ...)
6) Test the login with Google, SAML and OpenID
7) Test the background and logo is displayed correctly
