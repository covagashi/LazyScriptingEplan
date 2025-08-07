# Lazy Eplan Scripting

## Intro

I am doing this project inspired with the agents. In my head is posible but I need to put on practice.

##  Getting Started

Still long way to finish this.... check Dev-log for more info

## 🗺️ Roadmap

### **Phase 1**: Core Infrastructure 
- [x] RAG service with LazyScriptingEplan knowledge base
- [x] JSON examples collection from Suplanus repository
- [x] EPLAN API patterns and templates
- [X] LLM integration for natural language processing

### **Phase 2**: Intelligence Layer 
- [ ] Conversation Agent
- [ ] Execution Agent
- [ ] Feedback Agent
- [ ] Knowledge Agent
- [ ] ProjectManager Agent

### **Phase 3**: EPLAN Integration 

### **Phase 4**: User Interface 


---
# Dev-Log

30/07/2025
My first idea was to build it with C# but I really had difficulties when I try to use a local LLM.
I did a quick test and EplanRemoting works fine with python. So I will use python because is more friendly
when comes with LLM

02/08/2025
I am stuck with the RAG system, I am not sure if the qwen is nnot enought.
I am thinking to pivote towards Geminis 1.5 API instead of a local LLM

04/08/2025
I moved to geminis and it's better but I still struggling with the RAG

05/08/2025
Instead of using a parsing all the json, I changed into 'sentence-transformers/all-MiniLM-L6-v2' 
So the RAG is more effective. Now the  knowledgeAgent find the information and ManagerAgent give the context.
- One of the pending task would be, clean the information of the json. 
- Next step will improve the conversationAgent and text the codeGeneratorAgent.

06/08/2025
After some test, the workflow is not smart and after all if working with case words and small changes
broke others agents. So my desition is change the architecture.

I did recreate the new agents so... the knowledge agent is broke again (RAG) and I need to improve this
new system and findout a balance. 

07/08/2025
Right now I enhanced the agents and I havent test yet everything but probably is not working.
I separated the RAG for improve the search of docs api and example scripts.
There is a new agent for planning but doesnt act as coordinator.
I am not sure if start testing or implement the fallback loop and add the learning from 
feedback.


---

## 🔗 Resources

- **Original Source**: [Suplanus EPLAN Scripting](https://github.com/Suplanus/EPLAN-Scripting/tree/master)
- **EPLAN API Documentation**: Official EPLAN developer resources

## 🙏 Acknowledgments

Special thanks to [Suplanus](https://github.com/Suplanus) for the foundational examples and EPLAN scripting community contributions.

---

Created with ❤️ by covagashi
