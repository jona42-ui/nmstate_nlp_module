# nmstate_nlp_module
https://github.com/nmstate/nmstate/issues/2583

This small module basically demonstrates the power of NLP in network configuration I.e
Our demo project aims to develop a natural language interface that allows users to create Linux bridge configurations using simple, human-readable commands. The interface will leverage natural language processing (NLP) techniques to parse user input and generate YAML configurations compatible with nmstate, a declarative API for host network management in Linux.

[nlpdemo.webm](https://github.com/jona42-ui/nmstate_nlp_module/assets/78595738/ba6fac02-8bca-4466-88aa-cdf16c2dd3ab)


Currently, it's only extracting the interface name (eth1) from the natural language input and generating a configuration entry for it, but it's missing the bridge name (br0) and the second interface (eth2).

TODO: improving the output

# usage
1. clone the repo
2. install the dependencies
3. spaCy requires language models forexample for English language processing, you can download the small English model by running:
   python -m spacy download en_core_web_sm
4. Execute the script : 
python nmstate_nlp_demo.py
5. on prompt put an input like: Please create a linux bridge br0 using eth1 and eth2
6. analyse the output


NB:  we are parsing  and interpreting  user intentions directly from textual descriptions using NLP parsing not regex parsing on input


