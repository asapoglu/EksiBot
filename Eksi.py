from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time
import os



class Eksi:
    def __init__(self):
        self.username = input("Lütfen Kullanıcı adınızı giriniz : ")
        self.password = input("Lütfen Şifre giriniz : ")
        self.browser = wd.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
        self.browser.maximize_window()
        self.singIn()
    def singIn(self):
        url = "https://eksisozluk.com/giris"
        self.browser.get(url)
        time.sleep(1)
        username = self.browser.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)
        password = self.browser.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        button   = self.browser.find_element_by_xpath("//*[@id='login-form-container']/form/fieldset/div[4]/button").click()
        os.system('cls')
        time.sleep(1)
        self.mainPage()
    def mainPage(self):
        print("*******************************************ANASAYFA*******************************************")
        secenek = self.browser.find_elements_by_xpath("//*[@id='quick-index-nav']/li")
        for i in range(0,5):
            print(f"{i}) {secenek[i].text}")
        print("5) search")
        print("6) çıkış")

        while (1):
            secici = input("Yapmak istediğiniz işlemi seçiniz : ")
            if(secici == '0'):
                os.system('cls')
                secenek[0].click()
                time.sleep(1)
                list = self.browser.find_elements_by_xpath("//*[@id='partial-index']/ul/li")
                for i in range(0, len(list)):
                    k = str(list[i].text)
                    s = int(k.find('\n'))
                    print(f"{i}) {k[0:s]}")
                sec = input("Yapmak istediğiniz işlemi seçiniz : ")
                list[int(sec)].click()
                time.sleep(1.5)
                try:
                    basl = self.browser.find_element_by_xpath("//*[@id='topic']/div[1]/div/span/a[1]").click()
                except Exception:
                    basl = self.browser.find_element_by_xpath("//*[@id='topic']/div[2]/div/span/a[1]").click()

                self.entryleriParcala()
                break
            elif (secici == '1'):
                os.system('cls')
                secenek[1].click()
                time.sleep(1)
                list = self.browser.find_elements_by_xpath("//*[@id='partial-index']/ul/li")
                for i in range(0, len(list)):
                    k = str(list[i].text)
                    s = int(k.find('\n'))
                    print(f"{i}) {k[0:s]}")
                sec = input("Yapmak istediğiniz işlemi seçiniz : ")
                list[int(sec)].click()
                time.sleep(1.5)
                try:
                    basl = self.browser.find_element_by_xpath("//*[@id='topic']/div[1]/div/span/a[1]").click()
                except Exception:
                    basl = self.browser.find_element_by_xpath("//*[@id='topic']/div[2]/div/span/a[1]").click()
                self.entryleriParcala()
                break
            elif (secici == '2'):
                os.system('cls')
                secenek[2].click()
                time.sleep(1)
                list = self.browser.find_elements_by_xpath("//*[@id='partial-index']/ul/li")
                for i in range(0, len(list)):
                    k = str(list[i].text)
                    s = int(k.find('\n'))
                    print(f"{i}) {k[0:s]}")
                sec = input("Yapmak istediğiniz işlemi seçiniz : ")
                list[int(sec)].click()
                source = self.browser.page_source
                self.entryleriParcala()
                break
            elif (secici == '3'):
                os.system('cls')
                secenek[3].click()
                time.sleep(1)
                list = self.browser.find_elements_by_xpath("//*[@id='partial-index']/ul/li")
                for i in range(2, len(list)):
                    k = str(list[i].text)
                    s = int(k.find('\n'))
                    print(f"{i-2}) {k[0:s]}")
                sec = input("Yapmak istediğiniz işlemi seçiniz : ")
                list[int(sec)].click()
                source = self.browser.page_source
                self.entryleriParcala(source)
                break
            elif (secici == '4'):
                os.system('cls')
                secenek[4].click()
                time.sleep(1)
                list = self.browser.find_elements_by_xpath("//*[@id='partial-index']/ul/li")
                for i in range(0, len(list)):
                    k = str(list[i].text)
                    s = int(k.find('\n'))
                    print(f"{i}) {k[0:s]}")
                sec = input("Yapmak istediğiniz işlemi seçiniz : ")
                list[int(sec)].click()
                source = self.browser.page_source
                self.entryleriParcala()
                break
            elif (secici == '5'):
                os.system('cls')
                sea = input("Lütfen aramak istediğiniz metni giriniz: ")
                se = self.browser.find_element_by_xpath("//*[@id='search-textbox']")
                se.send_keys(sea)
                cli = self.browser.find_element_by_xpath("//*[@id='a3-toggle']").click()
                os.system('cls')
                time.sleep(1)
                list = self.browser.find_elements_by_xpath("//*[@id='partial-index']/ul/li")
                for i in range(0, len(list)):
                    k = str(list[i].text)
                    s = int(k.find('\n'))
                    print(f"{i}) {k[0:s]}")
                sec = input("Yapmak istediğiniz işlemi seçiniz : ")
                list[int(sec)].click()
                source = self.browser.page_source
                self.entryleriParcala()
                break
            elif (secici == '6'):
                os.system('cls')
                print("Çıkış yapılıyor lütfen bekleyin...")
                time.sleep(1.5)
                break
            else:
                print("Yanlış değer girdiniz lütfen 0 ile 8 arasında bir değer giriniz...")

    def entryleriParcala(self):
        time.sleep(2)
        source = self.browser.page_source
        soup = bs(source, 'html.parser')
        entryler = soup.find_all("li", attrs={"data-flags":"share msg report vote entrymodlog favorite"})
        baslik = self.browser.find_element_by_xpath("//*[@id='title']/a/span")
        bsk = (str)(baslik.text)
        print('-'*20, bsk.upper(), '-'*20, sep='\n')
        for num, entry in enumerate(entryler, 1):
            yazar = entry.find(class_='entry-author').get_text(strip=True)
            tarih = entry.find(class_='entry-date').get_text(strip=True)
            icerik = entry.find(class_='content').get_text(strip=True)

            print('{}. {} \n\nyazar: {}, tarih: {}'.format(
                num, icerik, yazar, tarih)
                )
            print('-'*75)
        self.sayfaDegistir(soup)
    def dosyayaYaz(self,soup,name):
        entryler = soup.find_all("li", attrs={"data-flags":"share msg report vote entrymodlog favorite"})
        txt = name + ".txt"
        with open(txt, "a", encoding="UTF-8") as file:

            for num, entry in enumerate(entryler, 1):
                yazar = entry.find(class_='entry-author').get_text(strip=True)
                tarih = entry.find(class_='entry-date').get_text(strip=True)
                icerik = entry.find(class_='content').get_text(strip=True)

                file.write('{}. {} \n\nyazar: {}, tarih: {}\n'.format(
                    num, icerik, yazar, tarih)
                    )
                file.write('-'*75)
                file.write('\n')

    def sayfaDegistir(self, soup):
        time.sleep(1)
        page = soup.find("div", attrs={"class": "pager"})
        try:
            sayfa = page.find("a", attrs={"class": "last"}).get_text(strip=True)
            q = (int)(sayfa)
        except Exception:
            q = 0
        print(f"Başlıktaki sayfa sayısı: {q}")
        print('\n')
        print('=' * 75)
        while(1):
            print("Anasayfaya dönmek için -1\nEntryleri dosyaya yazdırmak için -2\nYeni Entry girmek için -3\nSayga değiştirmek için sayfa numarasını yazınız")
            sec = input("Yapmak istediğiniz işlemi seçiniz : ")
            if(sec == '-1'):
                os.system('cls')
                self.mainPage()
            elif(sec == '-2'):
                baslik = self.browser.find_element_by_xpath("//*[@id='title']/a/span")
                bsk = (str)(baslik.text)
                self.dosyayaYaz(soup, bsk)
            elif(sec == '-3'):
                os.system('cls')
                text = input("Lütfen entrynizi giriniz ve enter tuşuna basınız...\n")
                textbox = self.browser.find_element_by_xpath("//*[@id='editbox']").send_keys(text)
                yolla = self.browser.find_element_by_xpath("//*[@id='topic']/div[6]/form/fieldset/div[2]/button[3]").click()
                print("Entryniz başarıyla girildi... Başlığa yönlendiriliyorsunuz...")
                time.sleep(1.5)
                basl = self.browser.find_element_by_xpath("//*[@id='topic']/div[1]/div/span/a[1]")
                basl.click()
                self.entryleriParcala()
            elif((int)(sec) > 0 and (int)(sec) <= q):
                os.system('cls')
                yeniS = self.browser.find_element_by_xpath("//*[@id='topic']/div[3]/select/option["+(str)(sec)+"]").click()
                self.entryleriParcala()

            else:
                print("Hatalı seçim yaptınız...")



print("Ekşi Sözlük Konsol Arayüzüne Hoşgeldiniz...")

Eksi()


