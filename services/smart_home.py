import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT

def control_device(topic, payload):
    """Sends an MQTT command to a smart device."""
    
    try:
        # Create a new MQTT client instance
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "VoiceAssistantClient")
        
        # Connect to the broker
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        
        # Publish the command
        client.publish(topic, payload)
        
        # Disconnect
        client.loop(timeout=1.0)
        client.disconnect()
        
        return (True, f"Command sent to {topic}.")
        
    except Exception as e:
        return (False, f"Could not connect to MQTT broker ({MQTT_BROKER}): {e}")

