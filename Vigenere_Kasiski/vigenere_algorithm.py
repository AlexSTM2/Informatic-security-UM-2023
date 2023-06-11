#Vigenere cypher
#The Vigenere cypher is a polyalphabetic cypher. It uses a key to cypher the text.
#The key is a word that is repeated until it has the same length as the text.
def main():
    text = str(input("Text to cypher: ").lower())
    key = str(input("Key: ").lower())
    cypher = Vigenere(text, key)
    cypher.run()

class Vigenere():

    def __init__(self, text=str, key=str, cyphered = ""):
        self.text = text
        self.key = key
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.cyphered = cyphered
    
    def cypher(self):
        i = 0
        while len(self.key) < len(self.text):
            for letter in self.key:
                if len(self.key) < len(self.text):
                    self.key += letter
                else:
                    break
                
        for letter in self.text:
            if letter in self.alphabet:
                index = self.alphabet.index(letter)
                key_index = self.alphabet.index(self.key[i])
                new_index = (index + key_index) % len(self.alphabet)
                self.cyphered += self.alphabet[new_index]
                i += 1
        
    def run(self):
        self.cypher()
        print(f"Cyphered text: {self.cyphered}")
        


if __name__ == "__main__":
    main()