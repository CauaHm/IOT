import paho.mqtt.client as mqtt

# --- CONFIGURAÇÕES ---
BROKER_ADDRESS = "broker.hivemq.com"
BROKER_PORT = 1883
TOPICO_SENSOR_TEMPERATURA = "estufa/sensor/temperatura"
TOPICO_VENTILACAO_COMANDO = "estufa/ventilacao/comando"
TEMP_MIN_IDEAL = 18.0
TEMP_MAX_IDEAL = 25.0

# --- FUNÇÃO PARA CONECTAR ---
def on_connect(client, userdata, flags, rc, properties=None): # Adicionado 'properties' para nova versão
    if rc == 0:
        print("✅ Conectado ao Broker com sucesso!")
        client.subscribe(TOPICO_SENSOR_TEMPERATURA)
        print(f"👂 Inscrito no tópico do sensor: '{TOPICO_SENSOR_TEMPERATURA}'")
    else:
        print(f"❌ Falha na conexão, código de retorno: {rc}")

# --- FUNÇÃO PARA MANDAR A MENSAGEM ---

def on_message(client, userdata, message):
    temperatura_recebida = message.payload.decode()
    print(f"\n🌡️ Temperatura recebida: {temperatura_recebida}°C")

    try:
        temp_float = float(temperatura_recebida)
        comando_ventilacao = ""

        if temp_float < TEMP_MIN_IDEAL or temp_float > TEMP_MAX_IDEAL:
            comando_ventilacao = "LIGAR ✅"
            print(f"🚨 Alerta! Temperatura fora do ideal. Decisão: {comando_ventilacao} ventilação.")
        else:
            comando_ventilacao = "SISTEMA DESLIGADO, TEMPERATURA IDEAL ❌"
            print(f"👍 Temperatura ideal. Decisão: {comando_ventilacao} ventilação.")

        print(f"📤 Enviando comando '{comando_ventilacao}' para o tópico '{TOPICO_VENTILACAO_COMANDO}'...")
        client.publish(TOPICO_VENTILACAO_COMANDO, comando_ventilacao)

    except ValueError:
        print("⚠️ Erro: A mensagem recebida não é um número válido.")

# --- PROGRAMA ---

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="pneumoutramiscroscopicossilicovulcanoconiotico")

client.on_connect = on_connect
client.on_message = on_message

print("🔌 Conectando ao broker...")
client.connect(BROKER_ADDRESS, BROKER_PORT, 60)

client.loop_forever()