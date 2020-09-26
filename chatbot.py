# import any modules here
import re
import operator

# Yuval Timen
# Let's get this chatbot chattin'


class Chatbot:


    def __init__(self):
        # If you want to load in any lexicons, do it here and use relative file
        # paths. You'll upload these files as well.
        # Absolute file paths will break the autograder.
        # Let us know if you are using very large (> 1MB) files.
        pass
    

    def respond(self, input):
        """
        Prompts the chatbot to respond to the given string.
        Parameters:
            input - string utterance from the user to respond to
        Return: string bot response
        """
        
        # Convert the entire input to lower case
        input_lower = input.lower()
        
        # Split the input into distinct sentences based on punctuation
        match = re.findall(r'[.!?]', input_lower)
        
        if not match:
            # No punctuation in the input, then we're dealing with 1 sentence
            input_list = [input_lower]
        else:
            input_list = input_lower.split(match[0], 1)
            
        replaced_list = []
        
        # We deal with each sentence separately here
        for idx, sentence in enumerate(input_list):
            tmp = sentence
        
            # Replace all first person pronouns contracted with token '{second_person_contracted}'
            # I'm, I've, I'd,
            tmp = re.sub(r'i\'m', '{second_person_contracted}', tmp)
            # Replace all second person pronouns contracted with token '{first_person_contracted}'
            tmp = re.sub(r'you\'re', '{first_person_contracted}', tmp)
            # Replace all first person pronouns (subject) with token '{second_person_pronoun_subject}'
            tmp = re.sub(r'(\bi\b|\bwe\b)', '{second_person_pronoun_subject}', tmp)
            # Replace all first person pronouns (object) with token '{second_person_pronoun_object}'
            tmp = re.sub(r'(\bme\b|\bus\b)', '{second_person_pronoun_object}', tmp)
            # Replace all second person pronouns with token '{first_person_pronoun}'
            # We don't include subject or object because of the ambiguity
            tmp = re.sub(r'\byou\b', '{first_person_pronoun}', tmp)
            # Replace all first person possessive pronouns with token '{second_person_possessive}'
            tmp = re.sub(r'(\bmy\b|\bour\b)', '{second_person_possessive}', tmp)
            # Replace all second person possessive pronouns with token '{first_person_possessive}'
            tmp = re.sub(r'\byour\b', '{first_person_possessive}', tmp)
            # Replace all first person possessive plural with token '{second_person_possessive_plural}'
            tmp = re.sub(r'(\bmine\b)', '{second_person_possessive_plural}', tmp)
            # Replace all second person possessive plural with token '{first_person_possessive_plural}'
            tmp = re.sub(r'(\byours\b)', '{first_person_possessive_plural}', tmp)
            # Replace all instances of 'to be' with '{to be}'
            tmp = re.sub(r'(\bam\b|\bare\b|\bwas\b|\bwere\b)', r'{\1}', tmp)
            
            # Now we fill in all of our placeholder tokens with their correct words
            tmp = re.sub(r'{first_person_pronoun}(.*?){are}', r'I\1am', tmp)
            tmp = re.sub(r'{first_person_pronoun}(.*?){were}', r'I\1was', tmp)
            tmp = re.sub(r'{are}(.*?){first_person_pronoun}', r'am\1I', tmp)
            tmp = re.sub(r'{were}(.*?){first_person_pronoun}', r'was\1I', tmp)
            tmp = re.sub(r'{second_person_pronoun_subject}(.*?){am}', r'you\1are', tmp)
            tmp = re.sub(r'{second_person_pronoun_subject}(.*?){was}', r'you\1were', tmp)
            tmp = re.sub(r'{am}(.*?){second_person_pronoun_subject}', r'are\1you', tmp)
            tmp = re.sub(r'{was}(.*?){second_person_pronoun_subject}', r'were\1you', tmp)

            # Replace all '{second_person_contracted}' with "you're"
            tmp = re.sub(r'{second_person_contracted}', 'you\'re', tmp)
            # Replace all '{first_person_contracted}' with "I'm"
            tmp = re.sub(r'{first_person_contracted}', 'i\'m', tmp)
            
            tmp = re.sub(r'{(am|are)}', r'\1', tmp)
            
            tmp = re.sub(r'{second_person_possessive_plural}', 'yours', tmp)
            tmp = re.sub(r'{first_person_possessive_plural}', 'mine', tmp)
            
            tmp = re.sub(r'({second_person_pronoun_subject}|{second_person_pronoun_object})', r'you', tmp)
            
            # TODO: Attempt to solve the subject-object ambiguity of 'you'
            # If it ends the sentence, then it's probably the object
            tmp = re.sub(r'{first_person_pronoun}(\.*?)$', r'me\1', tmp)
            # Otherwise it's probably the subject
            tmp = re.sub(r'{first_person_pronoun}', r'i', tmp)
            
            tmp = re.sub(r'{second_person_possessive}', 'your', tmp)
            tmp = re.sub(r'{first_person_possessive}', 'my', tmp)
            
            # If we missed anything thus far, keep it as is but remove the curly braces
            tmp = re.sub(r'(\{|\})', '', tmp)
            
            # Add the punctuation
            if match:
                if idx == 0:
                    tmp = tmp + match[idx]
            
            # Build up the final answer
            replaced_list.append(tmp)
        
        # Join together the sentences
        return ''.join(replaced_list)
        
        
    def special_respond(self, input):
        """
        Prompts the chatbot to respond to the given string.
        Implements arithmetic - the bot will respond as in the respond function,
        but any arithmetic phrase will be evaluated in the response.
        Parameters:
            input - string utterance from the user to respond to
        Return: string bot response
        """
        # We start with our basic response
        basic_response = self.respond(input)
        
        # Search out all occurrences of the arithmetic pattern
        arith = re.findall(r"[1-9][0-9]*(?:\s*[+\-*/]\s*[1-9][0-9]*)+", basic_response)
        
        # If we get a match, let's substitute in the evaluated forms
        if arith:
            # First, create a list with the evaluated expressions
            evaluated = [eval(a) for a in arith]
            for ev in evaluated:
                # We sub in 1 at a time from the evaluated list
                basic_response = re.sub(r"[1-9][0-9]*(?:\s*[+\-*/]\s*[1-9][0-9]*)+", str(ev), basic_response, 1)
        
        # Voila! Return the final response
        return basic_response
        
        
        

    def greeting(self):
        """
        Prompts the chatbot to give an initial greeting.
        Return: string bot initial greeting
        """
        return "Ello govnah!"

    def __str__(self):
        return "Sir Chatterton Bott"

def main():
    # Create a new chatbot
    cb = Chatbot()
    # the chatbot always begins by greeting the user
    begin = cb.greeting()
    print(cb, ":", begin)
    user_input = input("> ")

    # Any case of writing the word "exit" will cause the program to stop
    while user_input.lower() != "exit":
        bot_phrase = cb.special_respond(user_input)
        print(cb, ":", bot_phrase)
        user_input = input("> ")

    print("Goodbye!")


# This makes it so that the main function only runs when this file
# is directly run and not when it is imported as a module
if __name__ == "__main__":
    main()
