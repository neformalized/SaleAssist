import openai

#

class Conversator:
    
    def __init__(self, model):
        
        # openai model
        
        self.model = model
        
        # setup client by api key from file
        
        with open("api.txt", "r", encoding = "utf-8") as file:
            
            self.ai = openai.OpenAI(api_key = file.readline())
        #
        
        # set system info from file
        
        with open("system.txt", "r", encoding = "utf-8") as file:
            
            self.system = "".join(file.readlines())
        #
        
        # messages list
        
        self.messages = list()
        self.messages.append({"role": "system", "content": self.system})
    #
    
    def ask(self, message):
        
        self.messages.append({"role": "user", "content": message})
        
        #
        
        request = self.ai.chat.completions.create(
            
            model = self.model,
            messages = self.messages
        )
        
        #
        
        answer = request.choices[0].message.content
        
        #
        
        self.messages.append({"role": "assistant", "content": answer})
        
        #
        
        print("output: " + answer)
    #
#

if __name__ == "__main__":
    
    #
    
    model = "gpt-4o-mini"
    
    #
    
    c = Conversator(model)
    
    #
    
    while(True):
        
        c.ask(input("input: "))
        print("-=-=-=-=-=-=-")
    #