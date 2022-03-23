from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://fs16.formsite.com/form_app/FormSite?FormId=LoadNewUserSignUp&DesiredServiceLevel=&LinkSource=LoginPage&Referrer=https%3A%2F%2Ffs1.formsite.com%2Fform_app%2FFormSite%3FFormId%3DLoadLogin%26Auto")

# How to find how many input boxes present in a webpage

inputboxes = driver.find_elements(By.CLASS_NAME, 'auth-form__text-input')
print(len(inputboxes))

# How to provide value into textbox
driver.find_element(By.ID, 'UserEmail').send_keys("snextech@gmail.com")
driver.find_element(By.ID, 'UserEmail').is_displayed()

driver.find_element(By.ID, 'Password1').send_keys("Teddy001")
