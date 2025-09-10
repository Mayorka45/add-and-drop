from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.common.action_chains import ActionChains


chrome_driver_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome()


url = "https://my.aui.ma/ICS/Students/Academic_Information.jnz?portlet=Course_Schedules&screen=Add+Drop+Courses&screenType=next"


driver.get(url)


def send_email(course_code, section_info):
    sender_email = "Ab.razid@aui.ma"
    receiver_email = "L.adnane@aui.ma"
    subject = f"Seat Available for {course_code}"
    body = f"Seats available for {course_code}: {section_info}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.starttls()
            server.login(sender_email, "Modriccr7zinobixaui.")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email sent to {receiver_email} for {course_code}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def check_seat_availability(sec):

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//*[@id='pg0_V_dgCourses']/tbody/tr"))
    )

    # Section 1
    if(sec[0]):
        try:
            section1_seat_info_element = driver.find_element(By.XPATH, "//*[@id='pg0_V_dgCourses']/tbody/tr[1]/td[6]")
            section1_seat_info = section1_seat_info_element.text.strip()
            if section1_seat_info and section1_seat_info[0] != '0':
                course_code_element = driver.find_element(By.XPATH, "//*[@id='pg0_V_dgCourses']/tbody/tr[1]/td[3]")
                course_code = course_code_element.text.strip()
                print(f"Seats available for {course_code} (Section 1): {section1_seat_info}")
                send_email(course_code, section1_seat_info)
                return True
        except Exception as e:
            print(f"Error processing Section 1: {e}")

    # Section 2
    if (sec[1]):
        try:
            section2_seat_info_element = driver.find_element(By.XPATH, "//*[@id='pg0_V_dgCourses']/tbody/tr[3]/td[6]")
            section2_seat_info = section2_seat_info_element.text.strip()
            if section2_seat_info and section2_seat_info[0] != '0':
                course_code_element = driver.find_element(By.XPATH, "//*[@id='pg0_V_dgCourses']/tbody/tr[3]/td[1]")
                course_code = course_code_element.text.strip()
                print(f"Seats available for {course_code} (Section 2): {section2_seat_info}")
                send_email(course_code, section2_seat_info)
                return True
        except Exception as e:
            print(f"Error processing Section 2: {e}")
    #Section 3
    if (sec[2]):
        try:
            section3_seat_info_element = driver.find_element(By.XPATH, "//*[@id='pg0_V_dgCourses']/tbody/tr[5]/td[6]")
            section3_seat_info = section3_seat_info_element.text.strip()
            if section3_seat_info and section3_seat_info[0] != '0':
                course_code_element = driver.find_element(By.XPATH, "//*[@id='pg0_V_dgCourses']/tbody/tr[5]/td[3]")
                course_code = course_code_element.text.strip()
                print(f"Seats available for {course_code} (Section 3): {section3_seat_info}")
                send_email(course_code, section3_seat_info)
                return True
        except Exception as e:
            print(f"Error processing Section 3: {e}")
        # Section 4
    if (sec[3]):
        try:
            section4_seat_info_element = driver.find_element(By.XPATH, "//*[@id='pg0_V_dgCourses']/tbody/tr[7]/td[6]")
            section4_seat_info = section4_seat_info_element.text.strip()
            if section4_seat_info and section4_seat_info[0] != '0':  # Adjust seat count as needed
                course_code_element = driver.find_element(By.XPATH, "//*[@id='pg0_V_dgCourses'']/tbody/tr[7]/td[3]")
                course_code = course_code_element.text.strip()
                print(f"Seats available for {course_code} (Section 4): {section4_seat_info}")
                send_email(course_code, section4_seat_info)
                return True
        except Exception as e:
            print(f"Error processing Section 4: {e}")

    print("No available seats found in all sections.")
    return False

try:
    time.sleep(60)
    sec = [False, False, False, False]
    sections = input("Enter the section you are interested in numbers from 1 to 4")
    selected_sections = {int(sec) for sec in sections if sec.isdigit() and 1 <= int(sec) <= 4}
    while True:
        for s in selected_sections:
            sec[s - 1] = True
        if check_seat_availability(sec):
            break
        time.sleep(10)


        search_button = driver.find_element(By.ID, 'pg0_V_btnSearch')
        actions = ActionChains(driver)
        actions.move_to_element(search_button).perform()
        search_button.click()

finally:
    driver.quit()