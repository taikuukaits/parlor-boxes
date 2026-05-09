# parlor-boxes
Physical blue prince parlor boxes

# Setup
Install Arduino IDE
Install WifiManager

```
#include <ESP8266WiFi.h>
#include <WiFiManager.h>
#include <ArduinoOTA.h>

void setup() {
  Serial.begin(115200);

  WiFiManager wm;

  if (!wm.autoConnect("ParlorBoxes-Setup")) {
    Serial.println("Failed to connect, restarting...");
    ESP.restart();
  }
  Serial.println("WiFi connected!");

  ArduinoOTA.setHostname("parlor-boxes");

  ArduinoOTA.onStart([]() { Serial.println("OTA Start"); });
  ArduinoOTA.onEnd([]()   { Serial.println("OTA Done");  });
  ArduinoOTA.onError([](ota_error_t e) { ESP.restart(); });

  ArduinoOTA.begin();
  Serial.println("OTA ready");
}

void loop() {
  ArduinoOTA.handle();
}
```
