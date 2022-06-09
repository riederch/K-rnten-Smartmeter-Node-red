# Kärnten-Smartmeter-Node-red

<img width="808" alt="grafik" src="https://user-images.githubusercontent.com/11293087/172799554-fecfd276-0d37-4d85-8ccb-0749bd0e53a0.png">

### filterShort
Ab und zu kommen bei mir ungültige Telegramme mit ein paar zufälligen bytes an, dies filtert die heraus

### Split
Teilt die Nachricht in die einzelnen Teile auf: FrameCounter, systemTitle, Encrypted Data,...

### prepareExec, exec und Merge
Um die Nachricht zu entschlüsseln gehe ich momentan den Umweg über Python welches die Lib aus https://github.com/Gurux/Gurux.DLMS.Python verwendet

### split Decrypted
Teilt die entschlüsselten Daten auf, derzeit hardcodierte Längen passend für die Kärntner Smartmeter
