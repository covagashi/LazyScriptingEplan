# Lazy Eplan Scripting

## Intro

I am doing this project inspired with manus. In my head is posible but I need to put on practice.

##  Getting Started

Feed the LLM with the JSON files and it will help to create the scripts.
Remember to give the right instructions to the agents for prevent failures.
For example, to dont created message box or use "$" for variable, only for pathmaps.

## 🗺️ Roadmap

### **Phase 1**: Core Infrastructure 
- [] RAG service with LazyScriptingEplan knowledge base ---> stuck here
- [x] JSON examples collection from Suplanus repository
- [x] EPLAN API patterns and templates
- [X] LLM integration for natural language processing

### **Phase 2**: Intelligence Layer 
- [ ] Context-aware script generation
- [ ] Actioname script for eplan
- [ ] Smartlog Eplan
- [ ] EPLAN API code validation

### **Phase 3**: EPLAN Integration 

### **Phase 4**: User Interface 


---
30/07/2025
My first idea was to build it with C# but I really had difficulties when I try to use a local LLM.
I did a quick test and EplanRemoting works fine with python. So I will use python because is more friendly
when comes with LLM

02/08/2025
I am stuck with the RAG system, I am not sure if the qwen is nnot enought.
I am thinking to pivote towards Geminis 1.5 API instead of a local LLM

---

## 🔗 Resources

- **Original Source**: [Suplanus EPLAN Scripting](https://github.com/Suplanus/EPLAN-Scripting/tree/master)
- **EPLAN API Documentation**: Official EPLAN developer resources

## 🙏 Acknowledgments

Special thanks to [Suplanus](https://github.com/Suplanus) for the foundational examples and EPLAN scripting community contributions.

---

Created with ❤️ by covagashi
