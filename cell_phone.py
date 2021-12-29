class CellPhone:
    def __init__(self, model):
        self.model = model
        self.phone_number = ""
        self.contacts = {
        } #I think this makes it a dictionary, but honestly I'm not sure
        self.messages = []
        self.vibrate = False

    def receive_text(self, message):
        print(f"Incoming text message: \n{message} ")
        self.messages.append(message)

    def toggle_vibrate(self):
        if self.vibrate == True:
            self.vibrate = False
        else:
            self.vibrate = True
    
    def send_message(self, new_message, contact):
        print(f"To: {contact} \n{new_message}")
