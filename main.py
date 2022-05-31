import selenium
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from queue import Empty
from select import select
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import csv
import time


class bulk_purchase :
    def csv_reader(self, sample) :
        # to open sample csv file provided and store its data for placing order
        with open(sample, 'r') as file:
            reader = csv.DictReader(file)
            self.order_placing(reader)


    def order_placing(self, reader) :
        #for opening purchase link provided        
        driver = webdriver.Chrome(executable_path=r"C:\Users\Ritesh Pushkar\Desktop\bulk_purchase\chromedriver_win32\chromedriver.exe")
        url = 'https://edalnice.cz/en/bulk-purchase/index.html'
        driver.get(url)
        time.sleep(5) # gives an implicit wait for 5 seconds
        
        #accept cookie 
        driver.find_element_by_xpath("/html/body/footer/div[2]/div/div/div[2]/div/button[3]").click()
            
        for row in reader : 
            #Vehicle’s country of registration       
            country_name = driver.find_elements_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[2]/div[1]/div[1]/div/div[1]/div[2]/input")[-1]
            country_name.send_keys(row['Country'])
            time.sleep(5)
            country_name.send_keys(Keys.RETURN)
            
            #Beginning of vignette validity
            validity_begin = driver.find_elements_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div/input")[-1]   
            validity_begin.send_keys(row['Validity Begins'])
            
            #License plate number (1)
            license_plate = driver.find_elements_by_xpath('/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[3]/div/div/div[1]/input')[-1]            
            license_plate.send_keys(row['License Plate'])
            license_plate.send_keys(Keys.RETURN)
            
            #vehicle powered by natural gas, methane
            if(row['Powered by'] != '') :
                driver.find_elements_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[4]/div/div/input")[-1].click()
                time.sleep(1)
                if(row['Powered by'] == 'Natural Gas') :
                    driver.find_elements_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[4]/div/div[2]/div/div[1]/div/label")[-1].click()
                else :
                    driver.find_elements_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[4]/div/div[2]/div/div[2]/div/label")[-1].click()

             #Type of vignette   
            if(row['Type of Vignette'] == 'Annual'):
                driver.find_elements_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/fieldset/div/div/div/div[1]/div/div/label/div/div/div[2]/div/div[1]/span")[-1].click()
            elif(row['Type of Vignette'] == '30-day'):
                driver.find_elements_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/fieldset/div/div/div/div[2]/div/div/label/div/div/div[2]")[-1].click()
            else :
                driver.find_elements_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/fieldset/div/div/div/div[3]/div/div/label/div/div/div[2]")[-1].click()

            #add new batch
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[1]/div/div[5]/button/span/span[2]").click()


        #continue button 
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div/form/div/div[2]/div/div[4]/div/button/span").click() #click to continue
        # driver.find_element_by_name('Continue').click() #click to continue on new page
        # email_enter = driver.find_element_by_id('email-input')
        # email_enter.send_keys('sample@gmailcom')
        # email_confirm = driver.find_element_by_id('email-confirmation-input')
        # email_confirm.send_keys('sample@gmailcom')
        # driver.find_element_by_class_name('mb-3 col-auto').click() #payment method selected
        # driver.find_element_by_id('_termsAgreement-true').click() #terms agreemnt
        # driver.find_element_by_name('Pay').click()  #pay

        




            
if __name__ == "__main__":
    bulk_purchase_object = bulk_purchase()
    bulk_purchase_object.csv_reader('sample.csv')

