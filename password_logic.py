import random
from typing import Optional

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "="]
class Password:
    '''
    class
    '''

    def __init__(self, word_1: str, word_2: str, word_3: Optional[str] = None, word_4: Optional[str] = None, word_5: Optional[str] = None, separator: str = "_"):
        '''
        initializes word variables
        '''
        self.word_1 = word_1
        self.word_2 = word_2
        self.word_3 = word_3
        self.word_4 = word_4
        self.word_5 = word_5
        self.separator = separator
    
    def combine_words(self) -> str:
        '''
        combines words into 1 to make into a string
        '''
        word = self.word_1 + self.separator + self.word_2 + self.separator
        if self.word_3 is not None:
            word += self.word_3 + self.separator
        if self.word_4 is not None:
            word += self.word_4 + self.separator
        if self.word_5 is not None:
            word += self.word_5 + self.separator
        return word

    def randomize_password(self, word: str) -> str:
        '''
        randomizes combined word into a password
        '''
        for i in word:
            if i == "a":
                word = word.replace("a", "@")
            elif i == "o":
                word = word.replace("o", "0")
            elif i == "s":
                word = word.replace("s", "$")
            elif i == "i":
                word = word.replace("i", "!")
        parts_list = word.split(self.separator)
        length = len(parts_list)
        j = 0
        while j < length:
            if j % 2 == 0:
                number = random.randint(0, 100)
                parts_list[j] = parts_list[j].upper() + str(number)
                j = j + 1
            else:
                parts_list[j] = parts_list[j] + symbols[random.randint(0, 12)]
                j = j + 1
        randomized = (self.separator).join(parts_list)
        return randomized

    def password_strength_tester(self, word: str) -> str:
        '''
        tests strength of password
        '''
        security_score = 0
        length = len(word)
        if length >= 12:
            security_score += 1
        symbol_counter = 0
        number_counter = 0
        upper_counter = 0
        lower_counter = 0
        for i in word:
            if i in symbols:
                symbol_counter +=1
            elif i.isnumeric():
                number_counter += 1
            elif i.isupper():
                upper_counter += 1
            elif i.islower():
                lower_counter += 1
        
        if symbol_counter >= 3:
            security_score += 1
        if number_counter >= 3:
            security_score += 1
        if upper_counter >= 3:
            security_score += 1
        if lower_counter >= 3:
            security_score += 1

        if security_score >= 5:
            string = "Very Secure"
        elif security_score >= 3 and security_score < 5:
            string = "Moderately Secure"
        else:
            string = "Not Very Secure"
        return string

    def mock_attack(self, generated_password: str) -> str:
        '''
        simulates realistic password cracking attempts
        '''
        common_passwords = [
            "password", "123456", "qwerty", "admin",
            "welcome", "letmein", "abc123"
            ]
        if generated_password.lower() in common_passwords:
            return "Password cracked instantly (common password)."

        for word in common_passwords:
            if word in generated_password.lower():
                return "Password is weak (contains common word)."

        charset_size = 0
        if any(c.islower() for c in generated_password):
            charset_size += 26
        if any(c.isupper() for c in generated_password):
            charset_size += 26
        if any(c.isdigit() for c in generated_password):
            charset_size += 10
        if any(c in symbols for c in generated_password):
            charset_size += len(symbols)

        length = len(generated_password)

        combinations = charset_size ** length

        guesses_per_second = 1_000_000_000

        seconds = combinations / guesses_per_second

        if seconds < 60:
            return "Password could be cracked in seconds."
        elif seconds < 3600:
            return "Password could be cracked in minutes."
        elif seconds < 86400:
            return "Password could be cracked in hours."
        elif seconds < 31536000:
            return "Password could be cracked in days."
        else:
            return "Password is very strong (would take years to crack)."
        
# def main() -> None:
#     '''
#     runs program
#     '''
#     word_1 = input("Input Word #1: ")
#     word_2 = input("Input Word #2: ")
#     word_3 = input("Input Word #3: ") or None
#     word_4 = input("Input Word #4 ") or None
#     word_5 = input("Input Word #5: ") or None
#     separator = input("Input a Separator: ") or "_"

#     P = Password(word_1,word_2,word_3,word_4,word_5, separator)
#     combined = P.combine_words()
#     randomized = P.randomize_password(combined)
#     checker = P.password_strength_tester(randomized)
#     print(combined)
#     print(randomized)
#     print(checker)

# if __name__ == "__main__":
#     main()
