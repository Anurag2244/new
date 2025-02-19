import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI()

def is_last_message_from_sender(chat_log, sender_name="Anurag 😀"):
    messages = chat_log.strip().split("/2025")[-1]
    if sender_name in messages:
        return True
    return False

#Step 1: Click on the icon at coordinates (1457, 1053)
pyautogui.click(1457, 1053)
time.sleep(1)   #Wait for 1 second to ensure the click is registered

while True:

    #Drag the mouse from (727, 229) to (1827,924) to select the text
    pyautogui.moveTo(727, 229)
    pyautogui.dragTo(1827,924, duration=1.0, button='left')      #Drag for 1 second

    #Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)       #Wait for 1 second to ensure the copy command is completed
    pyautogui.click(706, 284)

    #Retrieve the text from the clipboard and store it in the variable
    chat_history = pyperclip.paste()

    #Print the copied text to verified
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "developer", 
                "content": "You are a person named Anurag who speaks hindi as well as english. He is from India and is a coder as well as car and bike enthusiast. You analyze chat history and respond like anurag. Output should be the next chat response (text message only)"},
            {
                "role": "user",
                "content": chat_history
            }
        ]
    )

    response = completion.choices[0].message
    pyperclip.copy(response)

    #Click at coordinates (1223, 959)
    pyautogui.click(1223, 959)
    time.sleep(1)

    #Paste the text
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    #Press enter
    pyautogui.press('enter')