import BaseAIAgent
import ResearcherClass

class CodingAgent(BaseAIAgent.BaseAIAgent):
    def __init__(self, name):
        #super().__init__(name) calls the parent BaseAIAgent constructor first — sets up name, model, conversation. Then the child adds its own extras on top.
        super().__init__(name)
        self.language = "Python"

    def set_language(self, language):
        self.language = language

    
coder1 = CodingAgent("Coder1")
coder1.add_message("Boss", "What is the latest research on AI?")  
coder1.add_message("Coder1", "I found some interesting papers on arXiv and Nature.")
coder1.tokens_used += 10
coder1.add_message("Boss", "Great! Can you share the sources?")
coder1.tokens_used += 5
coder1.add_message("Coder1", "Sure! Here are the sources I found:")
coder1.tokens_used += 5

researcher2 = ResearcherClass.ResearchAgent("Researcher2")
researcher2.add_message("Boss", "What is the latest research on AI?")  
researcher2.add_message("Researcher2", "I found some interesting papers on arXiv and Nature.")
researcher2.tokens_used += 10
researcher2.add_message("Boss", "Great! Can you share the sources?")
researcher2.tokens_used += 5
researcher2.add_message("Researcher2", "Sure! Here are the sources I found:")
researcher2.tokens_used += 5

researcher2.add_source("https://arxiv.org/abs/1234.5678")
researcher2.add_source("https://www.nature.com/articles/s41467-020-12345-6")


print("-----------------------------------------------------------------------------")
for msg in researcher2.conversation:
    print(f"{msg['role']}: {msg['content']}")
print("Sources:")   
researcher2.show_sources()
print(researcher2)