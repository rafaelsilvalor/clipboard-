# 📋 Clipboard++ Overlay Tool

Uma ferramenta Python leve que associa teclas de atalho a frases para copiar na área de transferência, funcionando mesmo em aplicações em tela cheia.

---

## ✅ Funcionalidades implementadas

- Estrutura básica de interfaces montada
- Leitura de arquivo de configuração (`phrases.cfg`) para definir mapeamento de teclas → frases
- Formato simples de `.cfg`: `setphrase: "tecla", "frase"`
- Copiar automaticamente a frase selecionada para a área de transferência no Windows
- Captura de teclas de atalho globais com `pynput`
- Testes unitários para as principais funcionalidades

---

## 🔄 Funcionalidades em desenvolvimento

- Aplicativo de linha de comando interativo para listar, adicionar e remover frases
- Interface gráfica mínima para exibir a última frase copiada na tela
- Suporte a outros formatos de configuração (YAML, TOML)
- Compatibilidade multiplataforma (macOS, Linux)
- Validação de combinações de teclas e mensagens de erro amigáveis

---

