from mycroft import MycroftSkill, intent_file_handler


class Techx(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('techx.intent')
    def handle_techx(self, message):
        self.speak_dialog('techx')


def create_skill():
    return Techx()

