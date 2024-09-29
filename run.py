import openai

#

class Conversator:
    
    def __init__(self, model):
        
        # openai model
        
        self.model = model
        
        # setup client by api key from file
        
        self.ai = openai.OpenAI(api_key = "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")
        
        # set system info from file
        
        with open("/content/SaleAssist/system.txt", "r", encoding = "utf-8") as file:
            
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