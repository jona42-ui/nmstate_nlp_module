import spacy
import yaml

def parse_input(input_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input_text)
    
    bridge_name = None
    interface_names = []
    
    for token in doc:
        if token.dep_ == "dobj" and token.head.pos_ == "VERB":
            bridge_name = token.text
        elif token.dep_ == "pobj" and token.head.dep_ == "prep":
            interface_names.append(token.text)
    
    return bridge_name, interface_names

def generate_yaml(bridge_name, interface_names):
    yaml_data = {
        "interfaces": [
            {
                "name": bridge_name,
                "type": "linux-bridge",
                "state": "up",
                "bridge": {
                    "ports": [{"name": iface} for iface in interface_names]
                }
            }
        ]
    }
    return yaml_data

def main():
    print("Please provide a natural language input to create a Linux bridge configuration:")
    user_input = input("\nUser Input: ")
    
    bridge_name, interface_names = parse_input(user_input)
    yaml_data = generate_yaml(bridge_name, interface_names)
    
    print("\nGenerated YAML Configuration:")
    print(yaml.dump(yaml_data))

if __name__ == "__main__":
    main()
