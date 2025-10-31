# Video RAG with Gemini

Aplicação de exemplo em Streamlit para realizar Video RAG (Retrieval-Augmented Generation) usando a API Gemini (Google Generative AI). O projeto permite enviar um vídeo, aguardar o processamento pela API do Gemini e conversar com o conteúdo do vídeo via prompts (chat interativo).

A UI do Streamlit pode ser acessado [aqui](https://dso-chat-video.streamlit.app/)

# Recursos

- Upload de vídeo e envio para a API Gemini
- Interface de chat interativa (Streamlit)
- Estrutura modular (models, views, utils)

# Requisitos

- Python 3.10+ (recomendado)
- Dependências listadas em `requirements.txt` (ex.: `streamlit`, `google-generativeai`, `python-dotenv`, `pillow`)
- Uma chave de API Gemini (defina `GEMINI_API_KEY` no arquivo `.env` ou informe na sidebar da UI)

# Instalação

1. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` na raiz com sua chave:

```env
GEMINI_API_KEY=your_api_key_here
```

# Como executar

1. Interface web (Streamlit):

```bash
streamlit run main.py
```

Abra o navegador no endereço que o Streamlit imprimir (por padrão http://localhost:8501).


# Uso (UI)

- Insira sua chave Gemini na sidebar (ou coloque em `.env`).
- Faça upload de um vídeo (MP4, AVI, MOV, MKV, WEBM). Há aviso para arquivos grandes.
- Após o processamento, use a caixa de chat para perguntar sobre o vídeo. Exemplos já disponíveis na UI.
- Botões para limpar chat e resetar o estado também estão disponíveis na sidebar.

# Estrutura do projeto

- `main.py` — controlador que usa `views/` para renderizar a interface (recomendado)
- `models/video_processor.py` — classe responsável pelo upload/espera por processamento e interações com Gemini
- `views/` — componentes da UI (chat, sidebar, footer, etc.)
- `utils/` — utilitários auxiliares

# Observações e resolução de problemas

- GEMINI_API_KEY faltando: defina no `.env` ou informe na sidebar antes de enviar vídeos.
- Limites de tamanho: vídeos muito grandes podem falhar no upload/processing. Comprima se necessário.
- Erros da API: verifique a saída da Streamlit e o console para mensagens de erro retornadas pela biblioteca `google-generativeai`.

# Contribuição

Pull requests são bem-vindos. Para contribuições pequenas: abra uma issue descrevendo o problema/feature e envie um PR com um teste/descrição clara.

# Licença

MIT — consulte o arquivo `LICENSE` se quiser alterar o tipo de licença ou incluir uma nota de direitos autorais.

# Contato

Para dúvidas ou melhorias, abra uma issue neste repositório ou entre em contato pelo e-mail do mantenedor (adapte conforme necessário).


