from encrypt import Cipher
from scrape import Quote

def make_guess(shift=None, encrypted_msg=None, decrypted_msg=None):
    print(f"\tEncrypted sentence: {encrypted_msg} \n")
    print(f"\tGod mode hint: {shift}")

    not_yet_won = True

    while not_yet_won == True:

        try:
            response = input("\tWhat is the shift number to break the cipher? (Enter ## between 1-26.) ")
            try:
                response = int(response)
                try:
                    if response >= 0 and response <= 26:
                        print(f"\tYour value: {response} ... and integer value is in range.")
                        if response == shift:
                            print(f"\tHooray, you solved it!\n")
                            print(f"\tHere's the decrypted quote: {decrypted_msg}\n")
                            not_yet_won = False
                        else:
                            print("\n\t...And value is not the right shift key...")
                    else:
                        raise ValueError("Integer should be between 1 and 26.")
                except ValueError as e:
                    print(f"\tEXCEPTION: {e}")
                    break
            except ValueError:
                print("\tDid not enter an integer value! Pls re-enter.")
                continue
        except KeyboardInterrupt:
            print("\n\t EXCEPTION: Keyboard input interrupted!")
            break


def run():
    # Greetings
    q = Quote()
    c = Cipher()

    # Get author name as hint
    split_quote = q.quote_of_the_day.split('-')
    author = split_quote[1].strip()

    # Program flow
    print("\tWELCOME TO THE QUOTE GUESSING GAME!!\n")
    print(f"\tThis is a quote from {author}...Any guesses?\n")
    make_guess(shift=c.shift, 
            encrypted_msg= c.encrypt(sentence=q.quote_of_the_day),
            decrypted_msg= q.quote_of_the_day
            )

if __name__ == "__main__":
    run()
