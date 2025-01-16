# Netzwerkprotokolle-und-Sicherheit

- NAT
- DNS
- Private Subnet
- Public Subnet
- Software PORTS


## NAT
NAT (Network Address Translation):
NAT (Network Address Translation) ist ein Verfahren, bei dem private IP-Adressen in eine öffentliche IP-Adresse übersetzt werden. Im IPv4-Adressierungsschema sind öffentliche und private Adressbereiche voneinander getrennt. Die privaten IP-Adressen, die an einzelne Geräte innerhalb eines Netzwerks vergeben werden, werden im Router in eine öffentliche IP-Adresse umgewandelt. Dieser Prozess, die Netzwerkadressübersetzung, ermöglicht es, mehrere private Netzwerke miteinander zu verbinden und gleichzeitig eine begrenzte Anzahl von öffentlichen IP-Adressen mehrfach zu nutzen.

#### Was ist NAT also ?
Im Rahmen der NAT werden private IP-Adressen in öffentliche IP-Adressen übersetzt.

1. Private IP-Adressen werden in öffentliche IP-Adressen übersetzt.
2. Router übernimmt die Aufgabe der Übersetzung und leitet Daten ins Internet weiter.
3. Private IP-Adressen können mehrfach vergeben werden, da sie in unterschiedliche öffentliche IP-Adressen übersetzt werden.
4. NAT sorgt für Privatsphäre, da interne Geräte nicht direkt aus dem Internet adressiert werden können.
5. Datenpakete aus dem Internet erreichen den Router nur, wenn ein entsprechender Port freigeschaltet ist.


## DNS
DNS (Domain Name System):
DNS (Domain Name System) ist ein System, das die Namen von Webseiten, wie z.B. (www.beispiel.de), in IP-Adressen übersetzt, die von Computern verstanden werden können. Wenn eine URL in einem Browser eingegeben wird, fragt der Computer einen DNS-Server nach der entsprechenden IP-Adresse. Der Server liefert daraufhin die Adresse, sodass die Website erreicht werden kann. DNS fungiert somit als eine Art „Telefonbuch“ des Internets, das es ermöglicht, Websites anhand von leicht merkbaren Namen zu erreichen, ohne die numerische IP-Adresse kennen zu müssen.

### Was ist also DNS ?
1. Was ist DNS?: DNS ist ein System, das Webseiten-Namen in IP-Adressen umwandelt.

2. Wie funktioniert es?: Wenn man eine Webseite eingibt, fragt der Computer den DNS nach der passenden IP-Adresse.

3. Warum ist es wichtig?: DNS ermöglicht es, Webseiten mit einfachen Namen statt Zahlen zu erreichen.

4. Beispiel: Statt eine IP-Adresse wie „192.168.1.1“ einzugeben, tippt man einfach „www.beispiel.de“.

5. Vorteil: DNS macht das Surfen im Internet einfach und verständlich.



#### DNS ist eine Umwandlung von Domain-Namen in IP-Adressen, aber dabei werden tatsächlich Datenpakete über das Netzwerk geschickt. Hier ist der Ablauf:
1. DNS-Anfrage: Wenn ein Benutzer eine Webseite aufruft, sendet der Computer ein DNS-Anfrage-Paket an einen DNS-Server, um die IP-Adresse der Domain zu erhalten.

2. DNS-Antwort: Der DNS-Server antwortet mit einem Datenpaket, das die IP-Adresse der angeforderten Webseite enthält.

3. Verbindung zur Webseite: Mit der erhaltenen IP-Adresse kann der Computer dann die Verbindung zur Webseite aufbauen.



## Private Subnet
Ein privates Subnetz bezeichnet einen Bereich in einem Netzwerk, der nicht direkt mit dem öffentlichen Internet verbunden ist. Es wird oft innerhalb von lokalen Netzwerken verwendet und ist durch Sicherheitsmechanismen wie Firewalls vom Internet isoliert.

In einem privaten Subnetz können die Geräte untereinander kommunizieren, aber der Zugriff auf das Internet erfolgt in der Regel nur über spezielle Geräte wie Router oder Gateways, die den Verkehr nach außen steuern.

Solche privaten Subnetze findet man häufig in Cloud-Umgebungen oder bei Unternehmen, um beispielsweise Server oder sensible Daten vor einer direkten Verbindung zum Internet zu schützen. Die für private Subnetze verwendeten IP-Adressen stammen aus speziellen Bereichen, die nur für den internen Gebrauch vorgesehen sind:

10.0.0.0 bis 10.255.255.255 (10.0.0.0/8)
172.16.0.0 bis 172.31.255.255 (172.16.0.0/12)
192.168.0.0 bis 192.168.255.255 (192.168.0.0/16)
Diese Adressen sind im Internet nicht erreichbar, was bedeutet, dass Geräte in einem privaten Subnetz nicht direkt aus dem Internet angesprochen werden können.

### Was ist also privat Subnet?
1. Ein privates Subnetz ist ein Bereich in einem Netzwerk, der nicht direkt mit dem öffentlichen Internet verbunden ist.
2. Geräte innerhalb des privaten Subnetzes können miteinander sprechen, aber nicht direkt auf das Internet zugreifen.
3. Der Internetzugang passiert meist über ein Gateway oder einen Router, der den Datenverkehr steuert.
4. Für private Subnetze werden bestimmte IP-Bereiche verwendet:
* 10.0.0.0 bis 10.255.255.255 (10.0.0.0/8)
* 172.16.0.0 bis 172.31.255.255 (172.16.0.0/12)
* 192.168.0.0 bis 192.168.255.255 (192.168.0.0/16)
5. Der Vorteil: Geräte im privaten Subnetz sind nicht direkt aus dem Internet erreichbar, was das Netzwerk sicherer macht.



## Public Supnet

Ein öffentliches Subnetz ist einfach ein Bereich im Cloud-Netzwerk, in dem Server oder Dienste so eingerichtet sind, dass sie mit dem Internet kommunizieren können. Im Gegensatz zu privaten Subnetzen, die vom Internet abgeschnitten sind, können die Ressourcen in einem öffentlichen Subnetz direkt mit dem Internet reden.

Das bedeutet:

* Internet-Zugang: Instanzen (wie Web-Server) in einem öffentlichen Subnetz haben eine öffentliche IP-Adresse und können mit dem Internet verbunden werden.
* Routen: Der Datenverkehr, der ins Internet geht, wird über ein spezielles Gateway weitergeleitet, das für die Verbindung zum Internet sorgt.
* Sicherheit: Durch Sicherheitsgruppen und Firewalls wird genau festgelegt, wer auf diese Instanzen zugreifen darf.
Ein Beispiel: Wenn du eine Website betreibst, die von Nutzern im Internet besucht werden soll, würdest du diese auf einem Web-Server im öffentlichen Subnetz hosten. Ein Load Balancer, der den Traffic verteilt, könnte ebenfalls dort stehen.

Im Gegensatz dazu würden Dinge wie Datenbanken oder interne Anwendungen, die nicht für das Internet bestimmt sind, in einem privaten Subnetz laufen. Diese Instanzen können das Internet bei Bedarf über ein NAT-Gateway erreichen, das in einem öffentlichen Subnetz steht.












