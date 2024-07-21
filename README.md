

# Speech Recognizer

Este projeto é uma aplicação Python simples que utiliza reconhecimento de voz e síntese de fala para interagir com o usuário. Ele escuta comandos de voz em português e responde verbalmente algumas frases

## Funcionalidades

- **Reconhecimento de Voz:** Escuta comandos de voz do usuário.
- **Síntese de Fala:** Responde ao usuário com voz sintetizada.

## Dependências

Para executar este projeto, você precisará instalar as seguintes bibliotecas:

- `speech_recognition`: Usada para o reconhecimento de voz.
- `pyttsx3`: Usada para a síntese de fala.

Você pode instalar todas as dependências necessárias com o seguinte comando:

```pip install speech_recognition pyttsx3```

## Como Usar?

Certifique-se de que todas as dependências estão instaladas.
Execute o script speechrecognize.py.
Fale claramente ao microfone quando solicitado.
O programa tentará reconhecer seu comando de voz e responderá verbalmente.
Funções Principais
falar(texto): Recebe um texto e o reproduz usando síntese de fala.
ouvir(): Escuta o ambiente em busca de comandos de voz e tenta reconhecê-los.
run_jarvis(): Inicia o loop principal do programa, escutando e respondendo a comandos de voz continuamente.
Limitações
O tempo de espera para o comando de voz é de 5 segundos.
A aplicação está configurada para entender comandos em português do Brasil (pt-BR).
