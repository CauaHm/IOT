Sistema de Coordenação de Ações com MQTT para Estufa Agrícola

Este repositório contém o código e a documentação de um sistema de Internet das Coisas (IoT) projetado para monitorar e controlar a temperatura de uma estufa agrícola, utilizando o protocolo MQTT para comunicação. O projeto demonstra o poder do modelo 

Publish/Subscribe (Pub/Sub) para criar soluções de IoT desacopladas e escaláveis.

O objetivo principal é coordenar uma ação—

acionar um sistema de ventilação—com base em informações coletadas por um sensor de temperatura simulado.

🚀 Arquitetura e Componentes

O sistema é estruturado em três componentes principais que se comunicam de forma assíncrona através de um 

Broker MQTT central.

Componente	Função	Tópico de Comunicação	Simulação
Sensor de Temperatura	

Publica o valor da temperatura ambiente (entre 
	

0∘C e 40∘C).

		

estufa/sensor/temperatura 
	

	

Aplicativo móvel 
	

IoT MQTT Panel com um painel tipo "Slider".

Cliente de Lógica e Controle	

O "cérebro" do sistema. Assina o tópico do sensor, aplica a lógica de controle e publica o comando para o atuador.
	

	

Assina: estufa/sensor/temperatura. Publica: 
	

estufa/ventilacao/comando.
	

	

Script em 
	

Python utilizando a biblioteca paho-mqtt.

Sistema de Ventilação (Atuador)	

Atua como atuador, recebendo e executando o comando de ação ("LIGAR" ou "DESLIGAR").
	

	

Assina: 
	

estufa/ventilacao/comando.
	

	

Aplicativo móvel 
	

IoT MQTT Panel com um painel tipo "Text Log".

    Broker Utilizado: broker.hivemq.com (Porta 1883).

⚙️ Lógica de Controle

Cliente de Lógica e Controle (o script Python) é responsável por manter a temperatura da estufa dentro de um intervalo ideal, que foi definido entre 18∘C e 25∘C.

    Se a temperatura for menor que 18∘C ou maior que 25∘C: o sistema publica o comando "LIGAR" (indicando que o sistema de ventilação, ou um sistema de aquecimento, deve ser ativado para corrigir a temperatura).

Se a temperatura estiver dentro do intervalo ideal (inclusive 18∘C e 25∘C): o sistema publica o comando "DESLIGAR".

🛠️ Guia de Configuração e Execução Rápida

Para rodar o sistema, siga os passos abaixo, divididos entre o computador (onde roda a lógica de controle) e o celular (para simular o sensor e o atuador).

Passo 1: Preparação no Computador

    Instale Python 3 (se ainda não tiver).

    Instale a biblioteca MQTT (paho-mqtt) no seu terminal:
    Bash

pip install paho-mqtt

Crie um arquivo chamado 

cliente_logica.py e adicione o código-fonte do cliente de lógica.

Passo 2: Configuração no Celular (App IoT MQTT Panel)

Configure o aplicativo para simular a conexão, o sensor de temperatura e o status da ventilação.

    Crie a Conexão com o Broker:

        Connection name: Conexão Estufa 

Broker address: broker.hivemq.com 

Port: 1883 

Crie o Painel do Sensor (Tipo: Slider):

    Panel name: Sensor de Temperatura 

Topic: estufa/sensor/temperatura 

IMPORTANTE: Marque a caixa "Disable dashboard prefix topic".

Range: Min 0, Max 40.

Crie o Painel de Status (Tipo: Text Log):

    Panel name: Status Ventilação 

Subscribe Topic: estufa/ventilacao/comando 

IMPORTANTE: Marque a caixa "Disable dashboard prefix topic".

Passo 3: Execução e Teste

    No Computador: Abra um terminal na pasta do arquivo cliente_logica.py e execute:

Bash

python cliente_logica.py

Deixe este terminal aberto.

No Celular: Abra o dashboard da Conexão Estufa e mova o slider do Sensor de Temperatura.

Verifique os Resultados:

    Terminal do PC: Você verá as leituras de temperatura e os comandos (LIGAR ou DESLIGAR) publicados.

App do Celular: O painel Status Ventilação atualizará em tempo real, exibindo o comando recebido.

📝 Estrutura de Tópicos (Hierárquica)

Foi adotada uma estrutura de tópicos hierárquica para organização e expansão futura, que facilita a adição de novos sensores e atuadores.

Tópico Completo	Propósito	Estrutura
estufa/sensor/temperatura	

Publicação dos dados de temperatura.
	

		

Contexto/Dispositivo/Dado.

estufa/ventilacao/comando	

Envio de comandos de ação ao atuador.
	

		

Contexto/Atuador/Ação.
