class AIAgent:

    def __init__(self, name, model="claude-opus-4-6"):
        self.name = name
        self.model = model
        self.conversation = []
        self.tokens_used = 0
#--------------------------------------------------------------------------------------------------------------

# We can also add methods to the class to manage the conversation and token count. This way we can encapsulate the functionality related to the agents within the class itself, making our code more organized and maintainable.

    def add_message(self,role,content):
        self.conversation.append({"role": role, "content": content})

# Lets call this method for both agents to add messages to their conversation history and update their token count.
# 
# This is creation of objects of the class AIAgent. Each agent has its own name, model, conversation history, and token count. This way we can easily manage multiple agents without having to copy and paste code for each one.
assistant = AIAgent("Assistant")
researcher = AIAgent("Researcher")
coder = AIAgent("Coder", model="claude-opus-4-5")


assistant.add_message("Boss","get me the latest sales report")  
researcher.add_message("Boss","what is the latest research on AI?")    

print(assistant.conversation)
print(researcher.conversation)