

# Netzwerktechnologie

### Wide Area Network (WAN)
- Definition: Ein WAN verbindet Computer über große geografische Entfernungen.
- Verwendung: Es verbindet lokale Netzwerke (LANs) an verschiedenen Standorten.
- Verbindungstechniken: Verbindungen erfolgen über Standleitungen, VPNs oder IP-Tunnel.
- Beispiel: Das Internet ist ein globales WAN.
- Skalierbarkeit: WANs ermöglichen Kommunikation über große Entfernungen und sind für Unternehmen wichtig.


### Metropolitan Area Network (MAN)
- Ein Metropolitan Area Network (MAN) verbindet Computer in einem Ballungsraum.
- Es kann eine Großstadt, mehrere Städte oder ein großes Gebiet mit mehreren Gebäuden umfassen.
- MANs sind größer als Local Area Networks (LAN), aber kleiner als Wide Area Networks (WAN).
- Der Begriff „metropolitan“ bezieht sich auf die Netzgröße, nicht auf die Demographie.
- MANs sind nicht auf städtische Gebiete beschränkt.


### Local Area Network (LAN)
- Definition: Ein LAN ist ein räumlich begrenztes Netzwerk, das Geräte wie Computer, Drucker und Speichergeräte verbindet.
- Verbindung: LANs können kabelgebunden oder kabellos (WLAN) sein.
- Verwendung: Häufig in Heim- oder Firmennetzwerken, um Geräte miteinander zu verbinden und Ressourcen zu teilen.
- Ressourcen: Gemeinsame Nutzung von Druckern, Servern und Daten ist möglich.
- Technologie: Bei größeren LANs wird meist Ethernet für die strukturierte Verkabelung verwendet.


### Personal Area Network (PAN)
- Ein Personal Area Network (PAN) verbindet elektronische Geräte in der unmittelbaren Umgebung eines Nutzers (z. B. bis zu einigen Metern).
- Typische Beispiele sind die Verbindung zwischen Bluetooth-Kopfhörern und Smartphones sowie die Vernetzung von Laptops, Tablets und Druckern.
- PANs können kabelgebunden (z. B. USB, FireWire) oder drahtlos (z. B. Bluetooth, WLAN, IrDA, Zigbee) sein.
- In der Regel enthalten PANs keinen Router und haben keinen direkten Internetzugang.
- Geräte in einem PAN können jedoch mit einem Local Area Network (LAN) verbunden sein, das Internetzugang bietet.

![](.image)


### BUS-Topologie

- Die Bus-Topologie verbindet alle Geräte über einen gemeinsamen Kommunikationskanal, den "Bus".
- Daten werden von einem Endgerät gesendet und können von allen anderen Geräten empfangen.
- Ein Ausfall eines Computers beeinträchtigt nicht die Verbindung der anderen, jedoch blockiert eine Störung im Bus das gesamte Netzwerk.
- Abschlusswiderstände an den Kabelenden verhindern Störungen und Netzwerkausfälle bei Erweiterungen oder Reduktionen.
- Obwohl Bus-Topologien früher in lokalen Netzwerken und alten Ethernet-Netzen verwendet wurden, sind sie heute weniger gebräuchlich, bieten aber  eine kostengünstige und einfache Lösung.


### RING-Topologie
- Die Ringtopologie verbindet Netzwerkteilnehmer über einen Kabelring, wobei jeder Host Daten weiterleitet.
- Jeder Host fungiert als Repeater, was die Überbrückung größerer Entfernungen ermöglicht.
- Die Steuerung erfolgt durch ein Protokoll, das den Zugriff auf den Ring regelt.
- Bei Unterbrechungen des Rings ist die Datenübertragung gestört; ein Ringleitungsverteiler kann helfen.
- In einem Ring mit "Protection" sorgen doppelte Leitungen für Ausfallsicherheit durch parallele Datenwege in entgegengesetzter Drehrichtung.


### STERN-Topologie
- Die Sterntopologie verbindet alle Geräte direkt mit einem zentralen Knotenpunkt (z. B. Switch oder Hub).
- Der zentrale Punkt fungiert als Verteiler und ermöglicht die Kommunikation zwischen den Geräten.
- Jedes Gerät hat eine separate Verbindung, was die Verwaltung und Erweiterung erleichtert.
- Der Ausfall eines Geräts hat normalerweise keine Auswirkungen auf andere Geräte, außer bei Ausfall des zentralen Knotenpunkts.


### MESH-Topologie
- Ein Mesh-Netzwerk verbindet Geräte (Knoten) miteinander und bildet Verzweigungen zu anderen Knoten.
- Es ermöglicht eine effiziente Datenübertragung und konsistente Verbindungen in einem physischen Raum.
- Mehrere Routen sorgen für Resilienz, falls ein Knoten oder eine Verbindung ausfällt.
- Größere Mesh-Netzwerke können viele Router, Switches und andere Geräte als Knoten umfassen.
- Mesh-Netzwerke können hunderte drahtloser Knoten enthalten, um große Bereiche abzudecken.



# Netzwerkgeräte

#### Router
- Ein Router ist ein Netzwerkgerät, das Datenpakete zwischen verschiedenen Netzwerken weiterleitet.
- Er verbindet lokale Netzwerke (z. B. LANs) mit dem Internet oder anderen Netzwerken.
- Router verwenden IP-Adressen, um den besten Pfad für die Datenübertragung zu bestimmen.
- Sie bieten oft zusätzliche Funktionen wie Firewall-Schutz, DHCP-Server und WLAN-Funktionalität.
- Router können entweder kabelgebunden oder drahtlos sein und sind entscheidend für die Netzwerksicherheit und -leistung.


#### Switch
- Ein Switch ist ein Gerät zur Verteilung von Datenströmen in kabelgebundenen Netzwerken.
- Er besitzt mehrere Ports für den Anschluss von Geräten wie Computern und Druckern.
- Im Gegensatz zu einem Hub leitet ein Switch Daten gezielt an bestimmte Geräte weiter und kann gleichzeitig senden und empfangen.
- Switches identifizieren jedes angeschlossene Gerät und verbessern die Netzwerkleistung.
- Sie können nicht die Funktionen eines Routers oder Modems übernehmen und werden oft in großen Netzwerken mit vielen Ports verwendet.


#### HUB
- Ein Hub verbindet mehrere Computer oder Endgeräte in einem Netzwerk, sodass diese untereinander kommunizieren können.
- Die Verbindung erfolgt über ein sternförmiges Ethernet-Netzwerk, bei dem alle Geräte mit dem Hub verbunden sind.
- Hubs arbeiten auf der Bitübertragungsschicht (Schicht 1) des OSI-Modells und haben daher nur eine reine Verteilerfunktion.
- Sie leiten empfangene Datenpakete an alle angeschlossenen Geräte weiter, ohne deren Adressen zu erkennen.
- Hubs sind weniger effizient und sicher als Switches, da sie Daten an alle Ports senden und somit das Risiko von Kollisionen erhöhen.
- Aufgrund ihrer Einfachheit und geringen Kosten werden Hubs heutzutage seltener eingesetzt, da Switches die bessere Wahl für moderne Netzwerke sind.


#### Access-Point
- Ein Access Point (AP) verbindet drahtlose Geräte mit einem kabelgebundenen Netzwerk und erweitert die WLAN-Reichweite.
- Er ermöglicht mobilen Geräten den Zugriff auf das Netzwerk und kann eigenständig oder in Kombination mit einem Router betrieben werden.
- Access Points unterstützen verschiedene WLAN-Standards (z. B. 802.11n, 802.11ac) und bieten Sicherheitsfunktionen wie WPA2 und WPA3.
- In großen Netzwerken sorgen sie für nahtlose Abdeckung und Roaming zwischen verschiedenen Bereichen.
- APs sind strategisch im Gebäude platziert, um eine optimale Signalverteilung und Netzwerkleistung zu gewährleisten.


#### Modem
- Ein Modem (Modulator-Demodulator) wandelt digitale Signale von einem Computer in analoge Signale um, die über Telefonleitungen oder Kabel übertragen werden können, und umgekehrt.
- Es ermöglicht die Verbindung zum Internet, indem es die Datenübertragung zwischen dem lokalen Netzwerk und dem Internetdienstanbieter (ISP) vermittelt.
- Modems können verschiedene Technologien nutzen, wie DSL, Kabel oder Glasfaser, um Internetzugang bereitzustellen.
- Viele moderne Modems sind Kombigeräte und integrieren Routerfunktionen, um mehrere Geräte drahtlos oder kabelgebunden zu verbinden.
- Sie verfügen oft über Sicherheitsfunktionen und unterstützen verschiedene Netzwerkprotokolle zur Optimierung der Verbindung.


# Subnetze

### 2.1 Subnetzmaske

Eine Subnetzmaske trennt den Teil einer IP-Adresse, der das Netzwerk identifiziert (Netzwerk-ID), von dem Teil, der ein bestimmtes Gerät im Netzwerk beschreibt (Host-ID). Zum Beispiel zeigt die IP-Adresse 192.168.1.10 mit der Subnetzmaske 255.255.255.0, dass das Netzwerk die ersten drei Teile (192.168.1) sind und die Hausnummer (Host-ID) die 10.
2.2 Routing außerhalb des Subnetzes

Wenn ein Computer eine Adresse außerhalb seines Subnetzes erreichen will:

    Prüfen: Er vergleicht die Zieladresse mit seiner Subnetzmaske.
    Router kontaktieren: Wenn die Zieladresse außerhalb ist, schickt der Computer die Daten an den Router.
    Router suchen: Der Router nutzt seine Tabelle, um den besten Weg zum Ziel zu finden. Wenn er es nicht weiß, leitet er die Daten an einen größeren Router weiter.
    Daten reisen: Die Daten bewegen sich von Router zu Router, bis sie ihr Ziel erreichen.

Zusammengefasst: Der Computer schickt die Daten an den Router, wenn das Ziel außerhalb des Subnetzes liegt. Der Router sucht den besten Weg, um die Daten zum Ziel zu leiten.

## Subnetze
Was ist eine Subnetzmaske?
Eine Subnetzmaske ist eine Zahl, die in Netzwerken verwendet wird, um festzulegen,
welcher Teil einer IP-Adresse das Netzwerk (Netzwerk-ID) und welcher Teil das spezifische
Gerät im Netzwerk (Host-ID) darstellt. Man kann sich eine IP-Adresse wie eine Adresse für
ein Haus vorstellen: Die Netzwerk-ID entspricht der Stadt, während die Host-ID die
Hausnummer repräsentiert. Die Subnetzmaske trennt diese beiden Bereiche.
Zum Beispiel:
● IP-Adresse: 192.168.1.10
● Subnetzmaske: 255.255.255.0
In diesem Beispiel zeigt die Subnetzmaske an, dass die ersten drei Teile der IP-Adresse
(192.168.1) das Netzwerk beschreiben, während der letzte Teil (10) das spezifische Gerät
identifiziert.

Wie funktioniert das Routing zu einer Adresse außerhalb meines
Subnetzes?
Wenn ein Computer eine Adresse außerhalb seines eigenen Subnetzes erreichen möchte,
geschieht Folgendes:

1. Überprüfung: Der Computer vergleicht die Zieladresse mit seiner Subnetzmaske
und erkennt, dass die Adresse nicht im eigenen Subnetz liegt.
2. Daten an den Router senden: Der Computer sendet die Daten an den Router (auch
bekannt als "Gateway"). Der Router prüft seine Routing-Tabellen, um eine direkte
Verbindung zum Ziel zu finden.
3. Direkte Verbindung: Wenn die Zieladresse in der Routing-Tabelle des Routers steht,
leitet er die Daten direkt dorthin.
4. Standard-Gateway: Wenn die Adresse nicht direkt bekannt ist, verwendet der
Router das Standard-Gateway, um die Daten an einen größeren Router
weiterzuleiten, der über mehr Verbindungen verfügt.
5. Routenfindung: Der Router ermittelt den besten Weg für die Datenübertragung.
Falls er den Weg nicht kennt, gibt er die Daten an einen anderen Router weiter.
6. Datenübertragung: Die Daten reisen von Router zu Router, bis sie schließlich ihr
Ziel erreichen.
Zusammengefasst: Ein Computer leitet die Daten an den Router weiter, wenn das Ziel
außerhalb seines Subnetzes liegt. Der Router verwendet seine Routing-Tabellen und
gegebenenfalls andere Router, um die effizienteste Route zum Ziel zu bestimmen.