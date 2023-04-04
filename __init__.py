
from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class ChatGptSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')
    
    def converse(self, uterrances, lang):
        if uterrances and self.voc_match(uterrances[0], 'understood'):
            self.speak_dialog('great')
            return True
        else
            return False

    def stop(self):
        pass


def create_skill():
    return ChatGptSkill()