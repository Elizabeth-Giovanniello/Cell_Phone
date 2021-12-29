class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = ""
        self.contacts = {}
        self.messages = []
        self.vibrate = False

    def receive_text(self, message):
        print(message)
        self.messages.append(message)

    def toggle_vibrate(self):
        if self.vibrate == True:
            self.vibrate = False
        else:
            self.vibrate = True
    
    def send_message(self, contact):
        new_message = input("Type your message: ")
        print(f"To: {contact} \n {new_message}")
