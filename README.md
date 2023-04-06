# Kärnten-Smartmeter-Node-red

Als Adapter wird ein Usb-Adapter von Amazon verwendet: (FTDI FR232R USB TTL 5 V auf RJ11 6p6c Smart Meter DSMR P1 für ISKRA AM550)

Der Aufbau der Messages ist im [telegram.md](telegram.md) beschrieben


<img width="808" alt="grafik" src="https://user-images.githubusercontent.com/11293087/172799554-fecfd276-0d37-4d85-8ccb-0749bd0e53a0.png">

### filterShort
Ab und zu kommen bei mir ungültige Telegramme mit ein paar zufälligen bytes an, dies filtert die heraus

### Split
Teilt die Nachricht in die einzelnen Teile auf: FrameCounter, systemTitle, Encrypted Data,...

### prepareExec, exec und Merge
Um die Nachricht zu entschlüsseln gehe ich momentan den Umweg über Python welches die Lib aus https://github.com/Gurux/Gurux.DLMS.Python verwendet

### split Decrypted
Teilt die entschlüsselten Daten auf, und ordnet sie in Objekte. In kärnten wird momentan variante1 aus dem [Dokument](https://oesterreichsenergie.at/fileadmin/user_upload/Smart_Meter-Plattform/20200201_Konzept_Kundenschnittstelle_SM.pdf) verwendet
