
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