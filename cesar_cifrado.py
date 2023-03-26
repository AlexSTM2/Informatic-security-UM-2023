#Im going to cypher a text with the Cesar cypher and Fibonacci sequence.

class Cypher():
    def __init__(self, text=str, positions=int, action=bool):
        self.text = text
        self.positions = positions
        self.action = action
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"

    def run(self):
        if self.action == True:
            self.cipher()
        else:
            self.decipher()

    def cipher(self):
        print(f"Text to cipher: {self.text}")
        alpabeth = self.alphabet
        text = self.text.lower()
        positions = self.positions
        text_cyphered = "" #This is the Ceasar cypher text.
        text_cyphered_fibonacci = "" #This is the Fibonacci sequence text.
        for letter in text: 
            if letter in alpabeth: #This is the Ceasar cypher
                index = alpabeth.index(letter)
                new_index = (index + positions ) % len(alpabeth) 
                text_cyphered += alpabeth[new_index]
        
            else:
                print(f"Letter {letter} not in alphabet. Continue with the next letter.")
                text_cyphered += letter

        for letter in text_cyphered: #This is the Fibonacci sequence
            if letter in alpabeth:
                cypher_index = alpabeth.index(letter)
                try:
                    if cypher_index >= 2:
                        new_index = (cypher_index-1) + (cypher_index-2)
                        text_cyphered_fibonacci += alpabeth[new_index]
                
                except IndexError:
                    text_cyphered_fibonacci += letter
                    print("Index out of range.")
                    

        print(f"Text cyphered: {text_cyphered_fibonacci}")

if __name__ == "__main__":
    text = "Casa"
    positions = 2
    action = True
    cypher = Cypher(text, positions, action)
    cypher.run()