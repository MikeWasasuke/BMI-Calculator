# BMI CALCULATOR FIRST PROJECT
import pyautogui

last_na = ('Do you wish to continue? ')
tip = ('type YES for more tips. Type NO if you dont want to continue: ')
# first batch of tips
tip1 = (
    '\nEat healthy snacks like peanut butter and jelly sandwich,\nnuts, cheese, sliced vegetables, dried fruits\nor avocados!\n')
tip2 = (
    '\nDrinks that are high in sugar or calories are another major\ncause of weight gain. Keep these beverages to a minimum,\nand drink more water!\n')
tip3 = (
    '\nChoose healthy sources of protein. You should opt for proteins\nwith unsaturated fats like soy and salmon, not\nthe cholesterol-boosting saturated fats!\n')
tip4 = (
    '\nDon’t forget to watch your portion sizes - you can do this by\nusing smaller dishes at meals, serving the right portion amounts\nof food and not going back for seconds. Portion control is vital for\nweight management!\n')
##second batch
tip5 = (
    '\nGet enough exercise daily, especially strength training, which\ncan help you build up your muscles and gain weight.\nExercise also stimulates your appetite!\n')
tip6 = (
    '\nIncrease fruit and vegetable intake, decrease harmful fats, and\nyou’ll be able to maintain your BMI while also enjoying\nmore energy and better organ function!\n')
tip7 = (
    '\neating small portions of healthy foods will send a signal to the\nbrain that you are full, so it is time to burn those calories\nquickly!\n')
tip8 = ('\nAvoid or limit intake of processed and junk foods that contain\nsaturated fat, added salt, added sugars!\n')
feedback = (
    '\nThank you and please leave a feedback! Message me at:\nFacebook: Jorge Relunia Rojas\nGmail: jorgereluniarojas@gmail.com')
feedback1 = (
    '\nThat\'s all folks! Thank you and please leave a feedback! Message me at:\nFacebook: Jorge Relunia Rojas\nGmail: jorgereluniarojas@gmail.com')


def prompt():
    formula = weight / height ** 2
    formula = round(formula)
    formula = str(formula)
    pyautogui.alert('Your BMI is ' + formula)
    formula = int(formula)


x = 1
while x <= 1:
    x = x + 1
    name = pyautogui.prompt('What is your name? ')
    name = str(name)
    name = name.upper()
    height = pyautogui.prompt('What is your height in meters? ')
    try:
        height = float(height)
    except:
        pyautogui.alert('Please enter numeric value mamser.')
        continue

    weight = pyautogui.prompt('How about your weight in kilograms? ')
    try:
        weight = float(weight)
    except:
        pyautogui.alert('Please enter numeric value mamser.')
        continue

    formula = weight / height ** 2
    formula = round(formula)
    formula = int(formula)

    # for UNDERWEIGHT
    if formula <= 18.5:
        prompt()
        pyautogui.alert(
            '\nI knew it! Hi ' + name + ' sad to say that you are UNDERWEIGHT.\nEat more healthy foods and have proper diet.\n')
        tips = pyautogui.prompt(tip)
        if tips == ('YES') or tips == ('yes'):
            pyautogui.alert(tip1)
        else:
            pyautogui.alert(feedback)
            continue
        last = pyautogui.prompt(last_na)
        if last == ('YES') or last == ('yes'):
            pyautogui.alert(tip5)
            pyautogui.alert(feedback1)
            continue
        else:
            pyautogui.alert(feedback1)
            continue

    # for NORMAL
    elif formula <= 25:
        if formula > 18.5:
            prompt()
            pyautogui.alert('\nI knew it! Hello ' + name + ' and congratulations!\nyour classification  is NORMAL.\n')
            tips = pyautogui.prompt(tip)
            if tips == ('YES') or tips == ('yes'):
                pyautogui.alert(tip2)
            else:
                pyautogui.alert(feedback)
                continue
            last = pyautogui.prompt(last_na)
            if last == ('YES') or last == ('yes'):
                pyautogui.alert(tip6)
                pyautogui.alert(feedback1)
                continue
            else:
                pyautogui.alert(feedback1)
                continue


    # for OVERWEIGHT
    elif formula < 30:
        if formula > 25:
            pyautogui.alert(
                '\nI knew it! Hello ' + name + ' you are in the\n OVERWEIGHT class. Start to exercise and have proper diet.\n')
            tips = pyautogui.prompt(tip)
            if tips == ('YES') or tips == ('yes'):
                pyautogui.alert(tip3)
            else:
                pyautogui.alert(feedback)
                continue
            last = pyautogui.prompt(last_na)
            if last == ('YES') or last == ('yes'):
                pyautogui.alert(tip7)
                pyautogui.alert(feedback1)
                continue
            else:
                pyautogui.alert(feedback1)
                continue


    # for OBESE
    else:
        pyautogui.alert(
            '\nI knew it! Hello ' + name + ' sorry to say that you are\nOBESE. Change  your bad lifestyle and adapt\nto better one. I know you can do it!\n')
        tips = pyautogui.prompt(tip)
        if tips == ('YES') or tips == ('yes'):
            pyautogui.alert(tip4)
        else:
            pyautogui.alert(feedback)
            continue
        last = pyautogui.prompt(last_na)
        if last == ('YES') or last == ('yes'):
            pyautogui.alert(tip8)
            pyautogui.alert(feedback1)
            continue
        else:
            pyautogui.alert(feedback1)
            continue
