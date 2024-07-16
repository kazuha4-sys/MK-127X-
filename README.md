# Projeto de Tradutor de Voz e Texto em Tempo Real
# MK 127X¹ V.01

## Objetivo
Desenvolver um dispositivo que permite a tradução de voz em tempo real, com funcionalidades de seleção de idioma via botões e exibição de texto traduzido em um display, sem a necessidade de mostrar a hora.

## Componentes Essenciais

- **Arduino Nano:** A placa principal que controlará todos os componentes.
- **Módulo de Microfone MAX9814:** Captura a entrada de voz do usuário.
- **Botões:** Permitem a seleção das opções de idioma e início da captura de áudio.
- **Display OLED ou LCD:** Exibe o texto traduzido.
- **Módulo WiFi (ESP8266 ou ESP32):** Conexão com serviços de tradução online.
- **Alto-falante:** Reproduz a tradução em áudio.
- **Bateria Recarregável e Circuito de Carregamento:** Alimentação portátil e contínua do dispositivo.

## Conexões

1. **Arduino Nano** é alimentado por uma fonte de energia adequada. Os pinos de alimentação GND e VCC estão conectados corretamente.
2. **Módulo de microfone** tem seu GND conectado ao GND do Arduino, VCC ao pino 3.3V ou 5V, e a saída de áudio ao pino analógico A0 do Arduino.
3. **Botões de seleção** têm um terminal conectado ao GND e o outro aos pinos digitais D2 e D3 do Arduino, com resistores pull-up internos ou externos.
4. **Display OLED ou LCD** está conectado aos pinos A4 e A5 do Arduino para comunicação I2C, com alimentação conectada ao GND e VCC.
5. **Módulo WiFi** está conectado aos pinos TX e RX do Arduino para comunicação serial, com alimentação conectada ao GND e 3.3V ou 5V.
6. **Alto-falante** está conectado ao pino PWM D9 do Arduino através de um transistor ou driver de áudio.
7. **Bateria recarregável** está conectada ao circuito de carregamento, que alimenta o VCC do Arduino.

## Funcionamento

1. O microfone captura a voz do usuário.
2. O Arduino processa o áudio e envia os dados para o módulo WiFi.
3. O módulo WiFi se conecta a um serviço de tradução online, como o Google Translate.
4. O texto traduzido é exibido no display.
5. O alto-falante reproduz o texto traduzido em áudio.
6. Os botões permitem ao usuário selecionar o idioma de entrada e saída ou iniciar a captura de áudio.

## Protótipo de Códigos

```c
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <ESP8266WiFi.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET    -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }

  display.display();
  delay(2000);
  display.clearDisplay();

  pinMode(D2, INPUT_PULLUP);
  pinMode(D3, INPUT_PULLUP);
}

void loop() {
  if (digitalRead(D2) == LOW) {
    // Código para iniciar a captura de áudio
  }

  if (digitalRead(D3) == LOW) {
    // Código para selecionar idioma ou outra função
  }

  // Código para exibir texto no display e reproduzir áudio
}
```

## Estilo CSS para iFrames
Este é um exemplo de CSS para estilizar dois iframes:

```css
/* Estilos gerais para os iframes */
iframe {
  border: 2px solid #ccc; /* Borda ao redor dos iframes */
  border-radius: 10px; /* Cantos arredondados */
  width: 100%; /* Largura completa do contêiner pai */
  height: 500px; /* Altura dos iframes */
  margin-bottom: 20px; /* Espaçamento inferior entre os iframes */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra ao redor dos iframes */
}

/* Estilos específicos para o primeiro iframe */
iframe#iframe1 {
  background-color: #f0f0f0; /* Cor de fundo específica para o primeiro iframe */
}

/* Estilos específicos para o segundo iframe */
iframe#iframe2 {
  background-color: #e0e0e0; /* Cor de fundo específica para o segundo iframe */
}

/* Estilos para o contêiner dos iframes */
.iframe-container {
  display: flex; /* Layout flexível */
  flex-direction: column; /* Coluna para empilhar os iframes verticalmente */
  gap: 20px; /* Espaçamento entre os iframes */
  align-items: center; /* Centralizar iframes horizontalmente */
  padding: 20px; /* Espaçamento interno do contêiner */
}
```
## Você pode incluir esse CSS no seu arquivo de estilos e criar os iframes no seu HTML da seguinte forma:

```html

<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Exemplo de Iframes Estilizados</title>
  <link rel="stylesheet" href="styles.css"> <!-- Link para o arquivo de estilos -->
</head>
<body>
  <div class="iframe-container">
    <iframe id="iframe1" src="https://www.example.com"></iframe>
    <iframe id="iframe2" src="https://www.example2.com"></iframe>
  </div>
</body>
</html>
```

## Certifique-se de ajustar os valores conforme necessário para atender às suas necessidades específicas.
