import sys
import yaml

# A helper to force PyYAML to use block style for multiline strings
class LiteralDumper(yaml.SafeDumper):
    pass

def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

LiteralDumper.add_representer(str, str_presenter)

def format_workflow(input_path, output_path):
    print(f"Reading Dify workflow from {input_path}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Verify graph nodes exist
    nodes = data.get('workflow', {}).get('graph', {}).get('nodes', [])
    print(f"Found {len(nodes)} nodes in the workflow graph.")

    llm_updated_count = 0
    for node in nodes:
        node_data = node.get('data', {})
        node_type = node.get('type') or node_data.get('type')
        node_title = node_data.get('title', 'Unknown')
        
        # Check for LLM nodes
        if node_type == 'llm' or node_data.get('type') == 'llm':
            prompt_templates = node_data.get('prompt_template', [])
            for prompt in prompt_templates:
                if prompt.get('role') == 'system':
                    prompt_text = prompt.get('text', '')
                    
                    # Check if standard variables are missing
                    missing_vars = []
                    if 'unity_version' not in prompt_text:
                        missing_vars.append("unity_version")
                    if 'code_language' not in prompt_text:
                        missing_vars.append("code_language")
                    if 'code_context' not in prompt_text:
                        missing_vars.append("code_context")
                    
                    if missing_vars:
                        print(f"Node '{node_title}' is missing reference to: {missing_vars}. Injecting...")
                        prefix = ""
                        if "unity_version" in missing_vars:
                            prefix += "\n用户当前 Unity 版本：{{#start.unity_version#}}\n"
                        if "code_language" in missing_vars:
                            prefix += "\n用户代码语言：{{#start.code_language#}}\n"
                        if "code_context" in missing_vars:
                            prefix += "\n用户代码上下文：\n{{#start.code_context#}}\n"
                        
                        prompt['text'] = prefix.strip() + "\n\n" + prompt_text
                        llm_updated_count += 1
                    else:
                        print(f"Node '{node_title}' already contains all start variables. Verified.")

    print(f"Writing updated workflow to {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, Dumper=LiteralDumper, default_flow_style=False, allow_unicode=True, width=1000)
    
    print("Optimization completed successfully.")

if __name__ == '__main__':
    format_workflow('Workflows/1.1.0workflow.yml', 'Workflows/1.2.0workflow.yml')
