from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


options = Options()
service = Service()
#options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")  # Disable automation controls
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

cislo = input("cislo obeti: ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
action = ActionChains(driver)
wait = WebDriverWait(driver, 10)




def o2_internet():
    for x in range(2):
        try:
            driver.get('https://www.o2.cz/osobni/internet')
            sleep(3)

            input_element = driver.find_element(By.XPATH, '//input[@placeholder="Ulice 123/4, Město"]')
            input_element.send_keys("Netolice")
            sleep(0.5)

            action.move_to_element_with_offset(input_element, 100, 50)
            action.click().perform()
            sleep(0.5)

            input_element = driver.find_element(By.XPATH, '//input[@id="phoneNumber"]')
            input_element.send_keys(cislo)
            sleep(0.5)

            button_element = driver.find_element(By.CSS_SELECTOR, '.d2-btn.d2-btn--pad-45.d2-btn--sm-pad-30.d2-btn--md-auto-width.d2-btn--primary')
            button_element.click()
            sleep(8)

            print("O2 Internet completed.")
            break
        except Exception as e:
            print("O2 failed. Retry in 1s ")
            print(e)

def o2_tarif():
    driver.get('https://www.o2.cz/osobni/volani/mobilni-tarify')
    sleep(2)

    neco = driver.find_element(By.XPATH, '//*[@id="m-nenasli-jste-to-co-jste-hledali"]/div[2]/div/div/a[4]')
    action.move_to_element(neco).perform()
    sleep(2)
    neco = driver.find_element(By.XPATH, '//*[@id="m-nenasli-jste-to-co-jste-hledali"]/div[2]/div/div/a[4]')
    action.move_to_element(neco).perform()

    input_element = driver.find_element(By.XPATH, '//*[@id="cmb-m-a82500-form-e16241-input"]')
    action.move_to_element(input_element).perform()
    input_element.send_keys(cislo)
    sleep(0.5)
                                        
    button_element = driver.find_element(By.XPATH, '//*[@id="cmb-m-a82500-form-e16244"]/button')
    action.move_to_element(button_element).perform()
    button_element.click()

    input_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cmb-detail-a216901-form-a72969-input"]')))
    action.move_to_element(input_element).perform()
    input_element.click()
    input_element.send_keys(cislo)
    sleep(0.25)

    button_element = driver.find_element(By.XPATH, '//*[@id="cmb-detail-a216901-form-a72976"]/button')
    button_element.click()
    sleep(5)

    print("O2 Tarif completed.")

def starnet_internet():
    driver.get('https://www.starnet.cz/internet')
    sleep(1)

    button_element = driver.find_element(By.CLASS_NAME, 'CybotCookiebotDialogBodyButton')
    button_element.click()
    sleep(1)

    span_element = driver.find_element(By.XPATH, '//span[@class="select2-selection__placeholder"]')
    action.click(span_element).perform()
    sleep(0.5)

    input_element = driver.find_element(By.XPATH, '//input[@class="select2-search__field"]')
    input_element.send_keys("netolice")
    sleep(1)

    input_element.send_keys(Keys.ENTER)
    sleep(1)

    input_element = driver.find_element(By.XPATH, '//input[@id="phone"]')
    input_element.send_keys(cislo)

    input_element = driver.find_element(By.XPATH, '//input[@class="wpcf7-form-control wpcf7-submit has-spinner"]')
    input_element.click()
    sleep(5)

    button_element = driver.find_element(By.XPATH, '//button[contains(text(), "Chci internet")]')
    button_element.click()
    sleep(3)

    print("Starnet Internet completed.")


def starnet_tarif():
    driver.get('https://www.starnet.cz/startel')
    sleep(2)
    
    button_element = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4054-o1"]/form/div[2]/p[3]/input')
    action.move_to_element(button_element).perform()
    
    input_element = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4054-o1"]/form/div[2]/p[1]/span/input')
    input_element.send_keys(cislo)
    sleep(0.5)

    input_element = driver.find_element(By.XPATH, '//*[@id="wpcf7-f4054-o1"]/form/div[2]/p[2]/span/textarea')
    input_element.send_keys("Prosím pokud se mi nedovoláte, tak to zkuste později hodně mi vypadává signál :( Promiňte, S pozdravem Karel Sugma")
    sleep(0.5)

    action.move_to_element(button_element).perform()
    action.click_and_hold(button_element).perform()
    sleep(0.6)
    action.release(button_element).perform()
    sleep(5)
    
    print("Starnet Internet completed.")
    
def telecom_internet():
    driver.get('https://nordictelecom.cz/internet')
    sleep(1)

    button_element = driver.find_element(By.XPATH, '//button[contains(text(), "Povolit vše")]')
    action.move_to_element(button_element).perform()
    button_element.click()
    sleep(0.5)

    input_element = driver.find_element(By.XPATH, '//input[@id="id_address"]')
    input_element.send_keys("České Vrbné 1901, 37011 České Budějovice")
    sleep(0.5)

    input_element = driver.find_element(By.XPATH, '//input[@class="availability__form__field"]')
    input_element.send_keys(cislo)
    sleep(0.5)

    button_element = driver.find_element(By.XPATH, '//button[contains(text(), "Ověřit dostupnost")]')
    action.move_to_element(button_element).perform()
    button_element.click()

    button_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[contains(text(), "Objednat po telefonu")]')))
    action.move_to_element(button_element).perform()
    button_element.click()
    sleep(0.5)

    input_element = driver.find_element(By.XPATH, '//input[@class="image-blocks__block__form__input image-blocks__block__form__input--popup"]')
    for x in range (9):
        ActionChains(driver).key_down(cislo[x]).key_up(cislo[x]).perform()
    sleep(0.5)
    
    button_element = driver.find_element(By.XPATH, '//*[@id="order-phone-popup"]/form/div/div/button')
    action.move_to_element(button_element).perform()
    button_element.click()
    sleep(4)

    print("Telecom Internet completed.")

def telecom_tarif():
    driver.get('https://nordictelecom.cz/internet')
    sleep(1)

    input_element = driver.find_element(By.XPATH, '//*[@id="id_phone_shared_lead_banner"]')
    action.move_to_element(input_element).perform()
    input_element.send_keys(cislo)
    sleep(0.5)

    button_element = driver.find_element(By.XPATH, '//*[@id="form-block-phone"]/button')
    action.move_to_element(button_element).perform()
    button_element.click()
    sleep(4)

    print("Telecom Tarif completed.")

def vodafone_internet():
    driver.get('https://www.vodafone.cz/internet')
    sleep(3)

    button_element = driver.find_element(By.XPATH, '//button[contains(text(), "Povolit vše")]')
    button_element.click()

    input_element = driver.find_element(By.XPATH, '//input[@id="supercheckerInput"]')
    input_element.send_keys("Obecní 42, 38411 Netolice")
    sleep(0.5)

    action.move_to_element_with_offset(input_element, 100, 50)
    action.click().perform()
    sleep(0.5)

    input_element = driver.find_element(By.XPATH, '//input[@id="supercheckerPhoneNumber"]')
    input_element.send_keys(cislo)
    sleep(0.5)

    button_element = driver.find_element(By.XPATH, '//div[contains(text(), "Zobrazit dostupnost")]')
    button_element.click()
    sleep(4)

    print("Vodafone Internet completed.")

def vodafone_tarif():
    driver.get('https://www.vodafone.cz/tarify')
    sleep(3)

    input_element = driver.find_element(By.XPATH, '//*[@id="c2c_phone"]')
    action.move_to_element(input_element).perform()
    input_element.send_keys(cislo)
    sleep(0.25)
    
    button_element = driver.find_element(By.XPATH, '//*[@id="c2c_submit"]')
    button_element.click()
    sleep(4)

    print("Vodafone Tarif completed.")

def bazos_sms():
    driver.get('https://elektro.bazos.cz/pridat-inzerat.php')
    sleep(3)

    box_element = driver.find_element(By.XPATH, '//*[@id="podminky"]')
    box_element.click()
    sleep(0.25)

    input_element = driver.find_element(By.XPATH, '//*[@id="teloverit"]')
    input_element.send_keys(cislo)
    sleep(0.25)

    button_element = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div[2]/div/form/input[3]')
    button_element.click()

    sleep(4)

    print("Bazos completed.")

def kalkulator_call():
    driver.get('https://www.kalkulator.cz/tarify-internet-tv/019026bd-964b-7132-a057-60a47f4f8d48/vysledky')
    sleep(3)

    cookies = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div[3]/div/a/span/span/span')
    cookies.click()
    sleep(0.25)
    
    input = driver.find_element(By.XPATH, '//*[@id="rescue-form__phone"]')
    input.send_keys(cislo)
    sleep(0.25)

    send = driver.find_element(By.XPATH, '//*[@id="rescue-form"]/div[2]/a/span')
    send.click()
    sleep(4)

    print("Kalkulator Call completed.")

def nej_tarif():
    driver.get('https://www.nej.cz/volani')
    sleep(3)

    cookies = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    cookies.click()
    sleep(0.25)

    send = driver.find_element(By.XPATH, '//*[@id="recaptcha-item2"]')
    action.move_to_element(send).perform()
    sleep(0.25)

    input = driver.find_element(By.XPATH, '//*[@id="kontakt"]/div/div[2]/form/div[1]/div[1]/input')
    input.send_keys(cislo)
    sleep(0.25)

    send.click()
    sleep(3)

    print("NejTarif completed.")

def usetreno_tarif():
    driver.get('https://www.usetreno.cz/tarify/kalkulacka-mobilnich-tarifu/kalkulace/?offers=1')
    sleep(3)

    cookies = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    cookies.click()
    sleep(0.25)

    send = driver.find_element(By.XPATH, '//*[@id="web_calculator_tarif_desktopCalculationForm_RDS255v4_submit"]')
    action.move_to_element(send).perform()
    sleep(0.25)

    input = driver.find_element(By.XPATH, '//*[@id="web_calculator_tarif_desktopCalculationForm_RDS255v4_spending_kc"]')
    input.send_keys('569')
    sleep(0.25)

    checkbox = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/main/form/div[6]/div[2]/div/label[2]/div/div[1]')
    checkbox.click()
    sleep(0.25)

    send.click()
    sleep(2)

    button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/div[1]/div/div[1]/div/div/div/a[2]')
    button.click()
    sleep(0.25)

    input_number = driver.find_element(By.XPATH, '//*[@id="phone"]')
    input_number.send_keys(cislo)
    sleep(0.25)

    submit = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')
    submit.click()
    sleep(3)

    print("Usetreno Tarif completed.")



def srovnejto_tarif(): #jmeno se musi upravovat asi dat input
    driver.get('https://www.srovnejto.cz/mobilni-tarify/kalkulace/')
    sleep(2)
    
    cookies = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    cookies.click()
    sleep(0.25)

    button = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div/div[3]/div/div[2]/div[2]/div[2]/div/button')
    action.move_to_element(button).perform()
    button.click()

    input_name = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[9]/div/div[2]/div/div/form/div[2]/div/div[2]/input')))
    input_name.click()
    input_name.send_keys('Mira Vynadal')
    sleep(0.25)    

    input_phone = driver.find_element(By.XPATH, '/html/body/div[9]/div/div[2]/div/div/form/div[3]/div[2]/div/input')
    input_phone.send_keys(cislo)
    sleep(0.25)   

    input_text = driver.find_element(By.XPATH, '/html/body/div[9]/div/div[2]/div/div/form/div[5]/div/textarea')
    input_text.send_keys('Prosím pokud se mi nedovoláte, tak mi zavolejte později.')
    sleep(0.25)

    button = driver.find_element(By.XPATH, '/html/body/div[9]/div/div[2]/div/div/form/div[6]/button')
    button.click()
    sleep(3)

    print("Srovnejto Tarif completed.")

def gomobil_tarif(): 
    driver.get('https://www.gomobil.cz/')
    sleep(2)

    cookies = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    cookies.click()
    sleep(0.25)

    submit = driver.find_element(By.XPATH, '//*[@id="frm-sectionLeadFormHomepage-form"]/div[1]/div[2]/input')
    action.move_to_element(submit).perform()
    sleep(0.25)

    input_phone = driver.find_element(By.XPATH, '//*[@id="frm-sectionLeadFormHomepage-form-phone"]')
    input_phone.send_keys(cislo)
    sleep(0.25)

    submit.click()

    sleep(3)
    print("GoMobil completed.")

def centrum_tarif():
    driver.get('https://www.centrum-tarifu.cz/')
    sleep(2)

    cookies = driver.find_element(By.XPATH, '//*[@id="cookie_enable_all"]')
    cookies.click()
    sleep(0.25)

    input_name = driver.find_element(By.XPATH, '//*[@id="frm-name"]')
    input_name.click()
    input_name.send_keys('Mira Vynadal')
    sleep(0.25)    

    input_phone = driver.find_element(By.XPATH, '//*[@id="frm-phone"]')
    input_phone.send_keys(cislo)
    sleep(0.25)   

    input_text = driver.find_element(By.XPATH, '//*[@id="frm-poznamka"]')
    input_text.send_keys('Prosím pokud se mi nedovoláte, tak mi zavolejte později.')
    sleep(0.25)

    checkbox = driver.find_element(By.XPATH, '//*[@id="form"]/div/form/div[5]/div[2]/div[2]/label')
    checkbox.click()
    sleep(0.25)

    checkbox = driver.find_element(By.XPATH, '//*[@id="form"]/div/form/div[5]/div[2]/div[3]/label')
    checkbox.click()
    sleep(0.25)

    checkbox = driver.find_element(By.XPATH, '//*[@id="form"]/div/form/div[6]/div[2]/div/label')
    checkbox.click()
    sleep(0.25)

    submit = driver.find_element(By.XPATH, '//*[@id="form"]/div/form/div[7]/button')
    submit.click()
    sleep(3)

    print("CentrumTarif completed.")

def cez_tarif():
    driver.get('https://www.cez.cz/cs/mobil')
    sleep(2)

    cookies = driver.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]')
    cookies.click()
    sleep(0.25)

    submit = driver.find_element(By.XPATH, '//*[@id="send"]')
    action.move_to_element(submit).perform()
    sleep(0.25)

    input_phone = driver.find_element(By.XPATH, '//*[@id="phone"]')
    input_phone.send_keys(cislo)
    sleep(0.25) 

    submit.click()
    sleep(3)

    print("Cez completed.")
    
def tarifon_tarif():
    driver.get('https://www.tarifon.cz')
    sleep(2)

    input = driver.find_element(By.XPATH, '//*[@id="frmc280-minutes"]')
    input.click()
    sleep(0.25) 

    input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frmleadForm-orn_phone"]')))
    input.send_keys(cislo)
    sleep(0.25)
    
    submit = driver.find_element(By.XPATH, '//*[@id="frmleadForm-send"]')
    submit.click()
    sleep(3)

    print("Tarfion completed.")

def komercnibanka_tarif():
    driver.get('https://www.kb.cz/cs/obcane/tarify')
    sleep(2)

    cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/button[2]')
    cookies.click()
    sleep(0.25)

    button = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[8]/div/div[2]/div/div/a/span')
    action.move_to_element(button).perform()
    button.click()
    sleep(0.25)

    input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="phoneNumber"]')))
    input.send_keys(cislo)
    sleep(0.25)

    input = driver.find_element(By.XPATH, '//button[contains(text(), "Odeslat")]')
    input.click()
    sleep(3)

    print("KomercniBanka completed.") 
    
def avonet_tarif():
    driver.get('https://avonet.cz/volani')
    sleep(2)

    cookies = driver.find_element(By.XPATH, '//*[@id="cookies-bar"]/div[2]/div/p[2]/a[2]')
    cookies.click()
    sleep(0.25)

    input = driver.find_element(By.XPATH, '//*[@id="f2098"]')
    action.move_to_element(input).perform()
    input.send_keys(cislo)
    sleep(0.25) 

    submit = driver.find_element(By.XPATH, '//*[@id="getvolani"]')
    submit.click()
    sleep(2)

    print("Avonet completed.")





o2_internet()
o2_tarif()
starnet_internet()
starnet_tarif() 
telecom_internet()
telecom_tarif()
vodafone_internet()
vodafone_tarif()
bazos_sms()
kalkulator_call()
nej_tarif()
usetreno_tarif()
srovnejto_tarif()
gomobil_tarif()
centrum_tarif()
cez_tarif()
tarifon_tarif()
komercnibanka_tarif()
avonet_tarif()

print("Completed 😈🤫")
sleep(2)

driver.quit()
