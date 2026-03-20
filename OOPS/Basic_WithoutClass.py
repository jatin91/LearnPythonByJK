
# Lets say we are building a system where we have two agents, an assistant and a researcher, who are having a conversation. we want to keep track of their converstion and the number of tokens they have used.
# Here we are maintaing the conversation and token count for both agents in a simple way. and we want to include the third agent our code will not able mangagable.
#since we are already copy pasting the methods and variable in a similar fashion.
agent1_name = "Assistant"
agent1_model = "claude-opus-4-6"
agent1_conversation = []
agent1_tokens = 0

agent2_name = "Researcher"
agent2_model = "claude-opus-4-6"
agent2_conversation = []
agent2_tokens = 0

def add_message_agent1(role, content):
    agent1_conversation.append({"role": role, "content": content})
    #print(agent1_conversation + "Total tokens used: " + str(agent1_tokens))

def add_message_agent2(role, content):
    agent2_conversation.append({"role": role, "content": content})
    #print(agent2_conversation + "Total tokens used: " + str(agent2_tokens))

add_message_agent1("user", "What is the capital of France?")
add_message_agent2("assistant", "The capital of France is Paris.")
agent1_tokens += 5
agent2_tokens += 7

print(f"{agent1_conversation}Total tokens used: {agent1_tokens}")
print(f"{agent2_conversation}Total tokens used: {agent2_tokens}")
# This approach is not scalable and maintainable. We can use OOPS to create a class for the agents and manage their conversation and token count in a more organized way.

