
from selenium import webdriver
import csv


def ReadWebURL():
    # Set up Chrome WebDriver
    driver = webdriver.Chrome()
    # driver.implicitly_wait(10)
    startBtnPath = "/html/body/div[1]/div/main/section/div/div[2]/button"
    totalQuestionPath = "/html/body/div[1]/div/main/section/div/div/div[1]/ol/li[1]/div/div/div/div[1]/h2"
    answers = {
        "1": "ich stimme zu (I agree)",
        "2": "ich stimme nicht zu (I disagree)",
        "3": "neutral"
    }

# Open the webpage
    driver.get("https://www.wahl-o-mat.de/bundestagswahl2021/app/main_app.html")

    try:

        startBtn = driver.find_element("xpath", startBtnPath)
        startBtn.click()

        totalQuestions =  driver.find_element("xpath", totalQuestionPath).text.split()[3]
        print("Plesae select the number to choose option no other Character will be used:")

        for i in range(int(totalQuestions)):
            options = {
                "1": f"/html/body/div[1]/div/main/section/div/div/div[1]/ol/li[{i+1}]/div/div/div/div[2]/ul/li[1]",
                "2": f"/html/body/div[1]/div/main/section/div/div/div[1]/ol/li[{i+1}]/div/div/div/div[2]/ul/li[2]",
                "3": f"/html/body/div[1]/div/main/section/div/div/div[1]/ol/li[{i+1}]/div/div/div/div[2]/ul/li[3]",
            }

            questionPath = f"/html/body/div[1]/div/main/section/div/div/div[1]/ol/li[{i+1}]/div/div/div/div[1]/p"

            question = driver.find_element("xpath", questionPath)

            option = ""
            while option not in options.keys():


                print("Question:", question.text)
                print("1 : ich stimme zu (I agree):")
                print("2 : neutral")
                print("3 : ich stimme nicht zu (I disagree)")
                option = input("Enter Option : ")

            buttonXpath = options.get(option)
            optionButton = driver.find_element("xpath", buttonXpath)
            save_results(question.text,answers.get(option))

            optionButton.click()

    except Exception as e:
        # Once all questions are answered, we'll reach an exception when trying to find the next button
        print("Reached the end of questions. Capturing results...")

    finally:
        # Close the browser
        driver.quit()

def save_results(question,answer):
    # Write results to CSV
    with open("AnswerData.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([question, answer])

# Call the function to start navigation and capturing results
ReadWebURL()

