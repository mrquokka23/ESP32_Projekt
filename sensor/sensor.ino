#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "SINU_WIFI_NIMI_SIIA";
const char* password = "SINU_WIFI_PAROOL_SIIA";

//Siia sisesta enda pythonanywhere lehe aadress
String serverName = "http://mrquokka.pythonanywhere.com/data";

unsigned long lastTime = 0;
unsigned long timerDelay = 60000/2;

void setup(){
    Serial.begin(9600);
    pinMode(14, INPUT);
    WiFi.begin(ssid);
    Serial.println("Connecting");
    while(WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("");
    Serial.print("Connected to WiFi network with IP Address: ");
    Serial.println(WiFi.localIP());
}
void loop() {
  //Saadame HTTP POST päringu iga 30 sekundi tagant
  if ((millis() - lastTime) > timerDelay) {
    //Kontrollime WiFi ühenudst
    if(WiFi.status()== WL_CONNECTED){
      WiFiClient client;
      HTTPClient http;
    
      http.begin(client, serverName);

      // Määrame postituse sisu tüübi
      http.addHeader("Content-Type", "application/json");
      // Andmed mida saata HTTP POST päringuga
      String httpRequestData = "{\"moisture\":\"";
      httpRequestData += touchRead(14);
      httpRequestData += "\"}";
      // Saadame HTTP POST päringu
      int httpResponseCode = http.POST(httpRequestData);
     
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);

      // Lõpetame ühenduse veebilehega
      http.end();
    }
    else {
      // Kui WiFi ühendus katkeb, proovime uuesti ühendada
      Serial.println("WiFi Disconnected");
      while(WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    }
    lastTime = millis();
  }
}