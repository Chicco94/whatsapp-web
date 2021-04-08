import time

from selenium import webdriver

from simon.accounts.pages import LoginPage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.header.pages import HeaderPage


# Creating the driver (browser)
driver = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")

# Login
#	   and uncheck the remember check box
#	   (Get your phone ready to read the QR code)
login_page = LoginPage(driver)
login_page.load()
time.sleep(7)


# 1. Get all opened chats
#	   opened chats are the one chats or conversations
#	   you already have in your whatsapp.
#	   IT WONT work if you are looking for a contact
#	   you have never started a conversation.
pane_page = PanePage(driver)

# get all chats
opened_chats = pane_page.opened_chats

# iterating over them
print("chat:")
for oc in opened_chats:
	print("name:", oc.name)  # contact name (as appears on your whatsapp)
	print("last_message:", oc.last_message)
	print("has_notifications:", oc.has_notifications())  # are there unread messages?
	print("notifications:", oc.notifications)  # returns a integer with the qty of new messages, if there are.
	print("\n")


# 2. Go into the chat
#	   just click on one to open the chat page
#	   (where the conversation is happening)
first_chat = opened_chats[0]
first_chat.click()

# 3. Read the last 10 messages from your contact
chat_page = ChatPage(driver)
msgs = chat_page.messages.newest(10, filterby='contact')

print("messaggi di una chat:")
for msg in msgs:
	print(msg.contact) # name (all should be the same)
	print(msg.date)
	print(msg.text)
	print(msg.status)


# 4. Reply to the most recent message
#msg = msgs[0]  # get the first of the messages query done in previous step
#msg = chat_page.messages.newest(filterby='contact')
# Be careful as library can only now reply to text message
# Replying to a msg type (video, image, giff, etc) is not implemented yet. 
#msg.reply("This a reply to a specific text msg.")


# Logout
header_page = HeaderPage(driver)
header_page.logout()

# Close the browser
driver.quit()