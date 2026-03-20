import BaseAIAgent

class ResearchAgent(BaseAIAgent.BaseAIAgent):
    def __init__(self, name):
        #super().__init__(name) calls the parent AIAgent constructor first — sets up name, model, conversation. Then the child adds its own extras on top.
        super().__init__(name)
        self.sources = []

    def add_source(self, url):
        self.sources.append(url)

    def show_sources(self):
        for source in self.sources:
            print(source)


researcher1 = ResearchAgent("Researcher1")
researcher1.add_message("Boss", "What is the latest research on AI?")  
researcher1.add_message("Researcher1", "I found some interesting papers on arXiv and Nature.")
researcher1.tokens_used += 10
researcher1.add_message("Boss", "Great! Can you share the sources?")
researcher1.tokens_used += 5
researcher1.add_message("Researcher1", "Sure! Here are the sources I found:")
researcher1.tokens_used += 5

researcher2 = ResearchAgent("Researcher2")
researcher2.add_message("Boss", "What is the latest research on AI?")  
researcher2.add_message("Researcher2", "I found some interesting papers on arXiv and Nature.")
researcher2.tokens_used += 10
researcher2.add_message("Boss", "Great! Can you share the sources?")
researcher2.tokens_used += 5
researcher2.add_message("Researcher2", "Sure! Here are the sources I found:")
researcher2.tokens_used += 5

researcher1.add_source("https://arxiv.org/abs/1234.5678")
researcher1.add_source("https://www.nature.com/articles/s41467-020-12345-6")


print(researcher1.get_token_count())
for msg in researcher1.conversation:
    print(f"{msg['role']}: {msg['content']}")
#print(researcher1.conversation)
print("Sources:")
researcher1.show_sources()
print(researcher1)
print("-----------------------------------------------------------------------------")
for msg in researcher2.conversation:
    print(f"{msg['role']}: {msg['content']}")
print("Sources:")   
researcher2.show_sources()
print(researcher2)