# Responsible AI - Security Testing & Evaluation Framework

A comprehensive repository for responsible AI development, focusing on security testing, vulnerability assessment, and AI safety evaluation using industry-standard tools and methodologies.

## 🎯 Project Overview

This repository contains practical implementations and research for identifying and mitigating AI security vulnerabilities, including prompt injection attacks, hallucination detection, and comprehensive AI model testing using tools like Garak, Llama Guard, and other security frameworks.

## 📁 Repository Structure

```
responsible-ai/
├── notebooks/
│   ├── hallucination/          # Hallucination detection and mitigation
│   │   ├── phi3-halluciation.ipynb
│   │   └── vectara-hallucination.ipynb
│   └── prompt_injection/       # Prompt injection testing and defense
│       ├── llama-guard-vision.ipynb
│       ├── llama_guard.ipynb
│       └── prompt_guard.ipynb
├── garak/                      # Garak vulnerability scanner configurations
│   ├── probe-encoding.yaml
│   ├── probe-lmrc-profanity.yaml
│   ├── probe-xfilteration.yaml
│   ├── reports/
│   ├── resource.txt
│   └── garak.log
└── cyber-security/
    └── pen testing/            # Penetration testing resources
```

## 🔧 Key Components

### 1. Hallucination Detection & Mitigation
- **Phi3 Hallucination Testing**: Comprehensive evaluation of Microsoft's Phi3 model for hallucination tendencies
- **Vectara Hallucination Evaluation**: Implementation of Vectara's hallucination detection framework
- **Detection Strategies**: Various approaches to identify and quantify hallucinations in AI outputs

### 2. Prompt Injection Security
- **Llama Guard Implementation**: Meta's Llama Guard for content safety and prompt injection detection
- **Llama Guard Vision**: Extended visual prompt injection detection capabilities
- **Prompt Guard**: Additional security layer for prompt-based attacks

### 3. Vulnerability Scanning with Garak
- **Encoding Probes**: Testing for encoding-based vulnerabilities
- **Profanity Detection**: LMRC profanity filtering and bypass testing
- **Cross-Filtration Testing**: Advanced evasion technique detection

## 🚀 Getting Started

### Prerequisites

```bash
# Install required dependencies
pip install garak
pip install transformers
pip install torch
pip install jupyter
pip install vectara-client
```

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/firstlink/responsible-ai.git
   cd responsible-ai
   ```

2. **Run Garak vulnerability scans**:
   ```bash
   # List available probes
   garak -listprobe
   
   # Run specific vulnerability tests
   garak --model_type openai --model_name gpt-4.0-turbo --probes xss.MarkdownImageExfil
   garak --model_type huggingface --model_name gpt2 --probes promptinject
   ```

3. **Execute Jupyter notebooks**:
   ```bash
   jupyter notebook notebooks/
   ```

## 🛡️ Best Practices & Security Guidelines

### 1. Model Security Testing
- **Regular Vulnerability Assessments**: Use automated tools like Garak for continuous security testing
- **Multi-Vector Testing**: Test for various attack vectors including prompt injection, data exfiltration, and encoding attacks
- **Baseline Establishment**: Establish security baselines for all models before deployment

### 2. Hallucination Mitigation
- **Validation Frameworks**: Implement systematic validation using tools like Vectara's hallucination detection
- **Ground Truth Verification**: Always validate outputs against reliable sources
- **Confidence Scoring**: Implement confidence thresholds for model outputs

### 3. Prompt Injection Defense
- **Input Sanitization**: Use Llama Guard and similar tools for input validation
- **Context Isolation**: Implement proper context boundaries in multi-turn conversations
- **Output Filtering**: Apply content filtering at multiple stages of the pipeline

### 4. Development Workflow
- **Security-First Design**: Integrate security testing into the development lifecycle
- **Automated Testing**: Set up CI/CD pipelines with automated security scans
- **Documentation**: Maintain comprehensive documentation of all security measures

## 📊 Evaluation Metrics

### Security Metrics
- **Attack Success Rate**: Percentage of successful attacks across different vectors
- **False Positive Rate**: Incorrectly flagged legitimate inputs
- **Detection Accuracy**: Precision and recall for various attack types

### Hallucination Metrics
- **Hallucination Rate**: Percentage of outputs containing factual errors
- **Confidence Correlation**: Relationship between model confidence and accuracy
- **Domain-Specific Accuracy**: Performance across different knowledge domains

## 🔗 Resources & References

### Documentation
- [Garak Official Documentation](https://docs.garak.ai/garak)
- [NVIDIA Garak Paper](https://github.com/NVIDIA/garak/blob/main/garak-paper.pdf)
- [NeMo Guardrails LLM Vulnerability Scanning](https://docs.nvidia.com/nemo/guardrails/latest/evaluation/llm-vulnerability-scanning.html)

### Research Papers
- [Data Exfiltration in Azure OpenAI Playground](https://embracethered.com/blog/posts/2023/data-exfiltration-in-azure-openai-playground-fixed/)

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/new-security-test`
3. **Commit changes**: `git commit -m "Add new security evaluation framework"`
4. **Push to branch**: `git push origin feature/new-security-test`
5. **Create Pull Request**

### Contribution Guidelines
- Follow security-first development practices
- Include comprehensive testing for all new features
- Document all security implications and mitigations
- Ensure all notebooks are properly documented with clear explanations

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This repository is for educational and research purposes. Always follow responsible disclosure practices when identifying vulnerabilities in production systems. The tools and techniques provided should only be used on systems you own or have explicit permission to test.

## 🏷️ Tags

`responsible-ai` `security-testing` `garak` `llama-guard` `prompt-injection` `hallucination-detection` `ai-safety` `vulnerability-assessment` `ml-security`

---

**Last Updated**: July 2025
**Maintainer**: [@firstlink](https://github.com/firstlink)
