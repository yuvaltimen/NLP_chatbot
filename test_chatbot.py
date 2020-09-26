import unittest
import hw1_chatbot  # import your solution

# Starter code for unit tests for HW 1, part 2 - chatbot
# make sure that this file and your hw1_chatbot.py file
# are in the same directory, then run this file with the
# command `python test_chatbot.py`

# Starter code
# Write your name
# and a file comment here

class ChatbotTest(unittest.TestCase):

    # Provided tests
    def test_provided(self):
        examples = {
            "My friend came to Northeastern today.": "Your friend came to Northeastern today.",
            "I am happy.": "You are happy.",
            "Why did I wait to do my homework?": "Why did you wait to do your homework?",
            "My friend Devon had his halloween party. I went as a zebra.": "Your friend Devon had his halloween party. You went as a zebra.",
            "We found a new tree. We named our tree \"Sam\".": "You found a new tree. You named your tree \"Sam\".",
            "I like talking to you. Your interface is friendly.": "You like talking to me. My interface is friendly."
        }

        chatter = hw1_chatbot.Chatbot()
        for ex_input in examples:
            response = chatter.respond(ex_input)
            self.assertEqual(examples[ex_input].lower(), response.lower(), msg = "Expected string on left, but got string on right.")

    # Tests that the bot correctly switches between first and second person pronouns.
    # Includes switching from first to second, second to first, and one and two sentences.
    def test_first_second_person(self):
        examples = {
            "I test code. I have two sentences.": "You test code. You have two sentences.",
            "I tried really hard for this assignment.": "You tried really hard for this assignment.",
            "Did you give me the proper set of tests? I do not see them.": "Did I give you the proper set of tests? You do not see them.",
            "You did what I told you.": "I did what you told me.",
            "We went to the park.": "You went to the park."
        }

        chatter = hw1_chatbot.Chatbot()
        for ex_input in examples:
            response = chatter.respond(ex_input)
            self.assertEqual(examples[ex_input].lower(), response.lower(),  msg="Expected string on left, but got string on right.")
            
    
    #Tests that the bot correctly switches between first and second possessive pronouns.
    
    def test_first_second_possessive(self):
        examples = {
            "We offer our services. You can refuse our help.": "You offer your services. I can refuse your help.",
            "I tried my best for this assignment.": "You tried your best for this assignment.",
            "Our biggest strength is our compassion.": "Your biggest strength is your compassion.",
            "I gave my item to your friend.": "You gave your item to my friend.",
            "You gave us your word. Did you think we would forget?": "I gave you my word. Did I think you would forget?",
            "Here you go.": "Here I go.",
        }
    
        chatter = hw1_chatbot.Chatbot()
        for ex_input in examples:
            response = chatter.respond(ex_input)
            self.assertEqual(examples[ex_input].lower(), response.lower(),
                             msg="Expected string on left, but got string on right.")

    # Tests that the bot correctly conjugates 'to be' when switching between first and second person.
    def test_verb_conjugation(self):
        examples = {
            "I am the best in the world and you are the next.": "You are the best in the world and I am the next.",
            "We are our brothers' keepers.": "You are your brothers' keepers.",
            "Eat a Snickers. You are not you when you are hungry.": "Eat a Snickers. I am not me when I am hungry.",
            "I am you. You are me.": "You are me. I am you.",
            "I gave you everything that you wanted.": "You gave me everything that I wanted.",
            "You often are more involved than you should be.": "I often am more involved than I should be.",
            "Where are they now?": "Where are they now?",
            "Where am I?": "Where are you?",
            "Where are you?": "Where am I?"
        }

        chatter = hw1_chatbot.Chatbot()
        for ex_input in examples:
            response = chatter.respond(ex_input)
            self.assertEqual(examples[ex_input].lower(), response.lower(),
                             msg="Expected string on left, but got string on right.")

    # Tests that the bot correctly deals with contracted words.
    def test_contractions(self):
        examples = {
            "I'm the best in the world.": "You're the best in the world.",
            "We're our brothers' keepers.": "You're your brothers' keepers.",
            "Eat a Snickers. You're not you when you're hungry.": "Eat a Snickers. I'm not me when I'm hungry.",
            "I'm you. You're me.": "You're me. I'm you.",
            "I'd give anything to solve this problem!": "You'd give anything to solve this problem!",
            "My fo'c's'le is at the front of the ship.": "Your fo'c's'le is at the front of the ship.",
            "There aren't any other examples here.": "There aren't any other examples here."
        }

        chatter = hw1_chatbot.Chatbot()
        for ex_input in examples:
            response = chatter.respond(ex_input)
            self.assertEqual(examples[ex_input].lower(), response.lower(),
                             msg="Expected string on left, but got string on right.")

    # Tests that the bot correctly deals with contracted words.
    def test_special_response(self):
        examples = {
            "I have 8-4 siblings. They each have 4*7 children.": "You have 4 siblings. They each have 28 children.",
            "I can add forever, look! 1+2 + 3+ 4+5 +6": "You can add forever, look! 21",
            "I can do multiplication also! Did you know that 8*5 = 40?":
                "You can do multiplication also! Did I know that 40 = 40?",
            "Let's try a division: 40 / 6 is a decimal.": f"Let's try a division: {40/6} is a decimal.",
            "Let's try a hard one. 12 * 11 = 11 * 3 * 4": "Let's try a hard one. 132 = 132"
        }

        chatter = hw1_chatbot.Chatbot()
        for ex_input in examples:
            response = chatter.special_respond(ex_input)
            self.assertEqual(examples[ex_input].lower(), response.lower(),
                             msg="Expected string on left, but got string on right.")
        

if __name__ == "__main__":
    unittest.main()
