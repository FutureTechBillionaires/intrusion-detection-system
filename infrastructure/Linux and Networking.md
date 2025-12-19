##### Linux and Networking
```
Sən sistemin müdafiəçisisən (defender). Defender-in ən vacib təməli:
```
🔹 Linux bilmək
```
(çünki bütün təhlükə aşkarlanması, loglar, IDS-lər, serverlər Linux üzərindədir)
```
🔹 Network-i başa düşmək
```
(şəbəkə necə işləyir = sonra hücumu tanımaq çox asan olur)
```
Bu həftə hər şey fundamental olmalıdır, çünki gələcəkdə:
 ML-based intrusion detection,
 Suricata/Zeek log analizi,
 real-time anomaly detection,
 automated response
bunların hamısı Linux + network biliklərinə dayanır.
1 week
```
Linux Basics (praktik, 1–2 saat)
```
bütün təhlükə aşkarlanması, loglar, IDS-lər, serverlər Linux üzərindədir
Fayl və direktoriyalar
 pwd – hazırki qovluğun yolunu göstərir
 ls – faylları siyahılayır
 ls -l – ətraflı siyahı
 ls -a – gizli faylları göstərir
 cd – qovluqlar arasında keçid
 cd .. – bir səviyyə yuxarı
 mkdir – qovluq yaratmaq
 rmdir – boş qovluğu silmək
 rm – faylı silmək
 rm -r – qovluğu və içindəkiləri silmək
 cp – fayl/kataloq surəti çıxarmaq
 cp -r – qovluğu surətləmək
 mv – fayl/kataloq köçürmək və ya adını dəyişmək
 touch – boş fayl yaratmaq
 cat – faylın məzmununu göstərmək
 head – faylın əvvəlki sətirlərini göstərmək
 tail – faylın son sətirlərini göstərmək
```
 nano – faylı redaktə etmək (terminal editor)
```
 vi – başqa terminal editor
 find – fayl/kataloq tapmaq
```
 locate – tez tapmaq (database əsaslı)
```
 chmod – fayl icazələrini dəyişmək
 chown – fayl sahibini dəyişmək
 ln – symbolic link yaratmaq
 file – fayl tipi haqqında məlumat
 stat – fayl haqqında ətraflı məlumat
 basename – yolun son hissəsini göstərir
 dirname – yolun qovluq hissəsini göstərir
 tree – qovluq strukturunu ağac kimi göstərir
 history – yazdığın əmrləri göstərir
Fayl məzmunu və axtarış
 grep – fayl məzmununda axtarış
 grep -i – böyük/kiçik hərfə baxmadan axtarış
 grep -r – qovluq daxilində rekursiv axtarış
 wc – söz, sətir, simvol saymaq
 diff – iki faylı müqayisə etmək
 cmp – iki faylı byte-by-byte müqayisə
 sort – faylın sətirlərini sırala
 uniq – unikal sətirləri göstər
 cut – faylın sahələrini seçmək
 head -n – ilk n sətiri göstər
 tail -n – son n sətiri göstər
 less – faylı səhifə-səhifə oxumaq
 more – less-in sadə versiyası
 tac – faylı əks sırayla göstər
 split – faylı hissələrə bölmək
 cat file1 file2 > merged – faylları birləşdirmək
 tee – faylı oxumaq və eyni zamanda yazmaq
 echo – mətn çıxarmaq
 printf – formatlı mətn çıxarmaq
 xargs – əmrləri fayl/datanı oxuyaraq icra etmək
 find . -type f -name "*.txt" – xüsusi faylları tapmaq
 grep "pattern" file.txt – nümunəni faylda tapmaq
 grep -v "pattern" – nümunəsiz sətirləri göstər
 grep -c "pattern" – nümunə sayını göstər
 awk – mətn sahələrini emal etmək
```
 sed – mətn dəyişdirmək (stream editor)
```
 cut -d',' -f1 – CSV fayldan sütun seçmək
 comm – iki faylın fərqini göstərmək
 tail -f logfile.log – real vaxtda faylı izləmək
 watch – əmri müəyyən interval ilə təkrar icra etmək
Sistem və proses idarəsi
```
▪ top – real vaxt sistem monitoru (CPU, RAM, proseslər)
```
▪ htop – top-un vizual, daha rahat versiyası
▪ ps – prosesləri göstər
▪ ps aux – bütün prosesləri ətraflı göstər
▪ kill PID – prosesi dayandır
▪ kill -9 PID – zorla prosesi dayandır
▪ pkill process_name – adla prosesi dayandır
▪ jobs – background işləri göstər
▪ fg %1 – background işini ön plana gətir
▪ bg %1 – job-u background-da davam etdir
▪ uptime – sistemin neçə vaxt işlədiyini göstərir
▪ free -h – RAM və swap vəziyyətini göstərir
▪ df -h – disk istifadəsini göstərir
▪ du -sh folder/ – qovluq ölçüsünü göstər
▪ uname -a – sistem haqqında məlumat
▪ hostname – kompyuter adı
▪ whoami – hazırki istifadəçi
▪ id – istifadəçi ID və qrup məlumatı
▪ last – son istifadəçi girişlərini göstər
▪ uptime – sistemin işləmə müddəti və yük
Şəbəkə və əlaqə
→ ping example.com – serverə ping atmaq
→ curl example.com – HTTP sorğu göndərmək
→ wget URL – fayl yükləmək
```
→ ifconfig – şəbəkə interfeyslərini göstər (Linux köhnə)
```
```
→ ip a – şəbəkə interfeysləri (modern)
```
→ netstat -tulnp – açıq portlar və əlaqələr
→ ss -tulnp – netstat alternativi
→ traceroute example.com – paket marşrutunu göstər
→ nslookup example.com – domenin IP-ni tapmaq
→ dig example.com – DNS sorğusu
Paket və sistem idarəsi
```
✓ apt update – paket məlumatlarını yenilə (Debian/Ubuntu)
```
✓ apt upgrade – paketləri yenilə
✓ apt install package_name – paket quraşdır
✓ apt remove package_name – paket sil
✓ dpkg -i package.deb – deb faylı quraşdır
✓ snap install package_name – snap paket quraşdır
✓ systemctl status service – xidmətin vəziyyəti
✓ systemctl start service – xidməti başlat
✓ systemctl stop service – xidməti dayandır
✓ journalctl -xe – sistem loglarını oxumaq
Proses və sistem idarəsi
top – real vaxt sistem monitoru
 CPU, RAM, proseslərin siyahısı və yükünü göstərir
 Canlı olaraq yenilənir
 q → çıxmaq
 Praktik: Terminalda top aç və bax: hansı proseslər çox CPU istifadə edir?
 CPU istifadəsi, sistemdə hansı proqramın nə qədər işlədiyini göstərir.
 RAM istifadəsi göstərir ki, hansı proses nə qədər yaddaş tutur.
htop – vizual sistem monitoru
 top-un daha vizual və rahat versiyası
 Prosesləri seçib dayandırmaq, renklərlə RAM/CPU yükünü görmək mümkündür
 F10 → çıxmaq
ps aux – bütün prosesləri göstər
 Sistemdə çalışan bütün prosesləri göstərir
 USER – prosesi işlədən istifadəçi
 PID – proses ID
 CPU, MEM – istifadə resursları
 Praktik: ps aux | grep firefox – xüsusi proqramın PID-ni tap
kill – prosesi dayandırmaq
 PID ilə prosesi dayandırır
 Zorla dayandırmaq üçün:
pkill – proses adı ilə dayandırmaq
 PID bilmədən prosesin adını yazmaq kifayətdir
jobs / fg / bg – background işləri idarə etmək
 & → proses background-da
 jobs → background prosesləri göstərir
 fg → background-da olan iş ön plana keçir
 bg → job-u background-da davam etdirir
systemctl – xidmətləri idarə etmək
 status → xidmətin vəziyyətini göstərir
 start → xidmət başlat
 stop → xidmət dayandır
 restart → xidmət yenidən başlat
```
Networking Basics (1–2 saat)
```
şəbəkə necə işləyir = sonra hücumu tanımaq çox asan olur?
Bu hissə intrusions-u başa düşmək üçün kritikdir.
IP, MAC, Gateway, DNS — nədir?
IP Address
• Sənin cihazının internetdə ünvanı.
• Evin poçt ünvanı kimidir, hər cihazda fərqli olur.
• Məsələn:
```
 Yerel (local): 192.168.1.10
```
```
 İnternetdə (public): 89.176.45.17
```
```
• Linux terminalında: ip addr show ve ya ifconfig (inet ile baslayan reqemler yerel
```
IP-dir
```
• Windowsda: ipconfig (IPV4 addressi menim yerel IP-dir)
```
• Linuxda Public IP-ni gormek: curl ifconfig.me ve ya curl icanhazip.com
```
(internetde gorsenen public IP-mi gosterecek)
```
```
Practice:
```
 ping 8.8.8.8 # IP-ə ping atmaq, əlaqəni yoxlamaq
 traceroute 8.8.8.8 # IP-ə gedən yol
 whois 8.8.8.8 # IP haqqında məlumat
👉 Intrusion üçün niyə vacibdir?
Attack-ların 99%-i IP-dən gəlir. Log analizində ilk baxdığın şey IP-dir.
MAC Address
```
 Cihazın şəbəkə kartının (NIC) unikal “pasport” nömrəsi.
```
 Unikaldır – hər şəbəkə kartının öz MAC-ı olur.
```
 Heç dəyişmir (əslində spoof olunur, amma default dəyişmir).
```
 Misal: A4:5E:60:AF:21:B9
```
 Adətən dəyişmir, amma spoof etmək olur (yəni saxtalaşdırmaq mümkündür)
```
 Bir çox hücumlar və müdafiə mexanizmləri MAC üzərində qurulur.
```
 Linuxda practice: ip link show ve ya ifconfig (axtardigimiz hisse link/ether ile baslayir)
```
```
misal: link/ether a4:5e:60:af:21:b9 brd ff:ff:ff:ff:ff:ff (Bu — sənin cihazının şəbəkə kartının
```
```
MAC ünvanıdı).
```
```
MAC Spoofing (MAC ünvanını dəyişmək) — praktiki
```
```
(Məlumat üçün göstərirəm, təhlükəli əməliyyat deyil)
```
sudo ip link set dev wlan0 down
sudo ip link set dev wlan0 address 11:22:33:44:55:66
sudo ip link set dev wlan0 up
⚠️Qeyd: Şəbəkə interfeysinin adı wlan0, eth0, enp3s0 və s. ola bilər.
ARP Poisoning
```
→ Hücumçu öz MAC ünvanını “saxtalaşdırıb” (spoof) qurbanın cihazı ilə router arasında özünü
```
```
“gateway” kimi göstərir. Bu, MITM (Man-in-the-Middle) şərait yaradır.
```
MAC Flooding
→ Switch-in MAC cədvəlini tonlarla saxta MAC ünvanları ilə doldururlar → switch “hub” kimi
davranmağa başlayır → bütün trafik yayımlanır → hücumçu sniffing ilə paketi tutur.
Network Access Control
→ Şirkətlərdə bəzən yalnız icazə verilmiş MAC-lər şəbəkəyə qoşula bilər.
```
👉 Niyə vacibdir? Layer 2 hücumları (ARP poisoning, MAC flooding) buna əsaslanır.
```
```
Gateway (Default Gateway)
```
 Sənin kompüterinin internetə “çıxış qapısı”.
 Router-in IP adresi:
o Adətən: 192.168.1.1
o 192.168.0.1
o 10.0.0.1
 Linux-da öz Gateway-ni necə tapacam?
→ route –n
→ ip route show
→ NetworkManager ile : nmcli device show
```
👉 Vacibliyi: Attack-ların çoxu “man-in-the-middle” etmək üçün gateway-ə müdaxilə edir (ARP
```
```
spoofing).
```
```
DNS (Domain Name System)
```
 Domenləri IP-yə çevirən sistem.
 DNS — internetin “telefon kitabıdır”.
 google.com → 142.250.184.238
 Əgər DNS olmasa, hər sayta daxil olmaq üçün IP yazmalı idin.
 Linuxda: cat /etc/resolv.conf
 Bu nəticəyə bənzər bir şey görəcəksən: nameserver 8.8.8.8
nameserver 1.1.1.1
```
 NetworkManager ile: nmcli device show | grep DNS (Bu daha dəqiq göstərir).
```
Hücumçular DNS-lə çox oynayır:
DNS Spoofing
 Hücumçu DNS cavabını dəyişir → sən google.com yazırsan, o isə səni saxta sayta göndərir.
DNS Hijacking
 DNS serverini ələ keçirir → bütün trafik yanlış IP-yə gedir.
Malware DNS dəyişir
```
 Zərərli proqram sənin DNS serverini belə edir: 1.1.1.1 → 185.66.77.23 (malicious). Və bütün
```
websitelər səni yanlış serverə yönləndirir.
👉 Niəyə vacibdir? Çox populyar hücum: DNS spoofing, DNS hijacking. Malware-lər öz “malicious DNS”
serverini qurur.
TCP
 Etibarlı bağlantı
 Paket itərsə yenidən göndərir
 Bağlantı qurmaq üçün 3-way handshake lazımdır
```
→ SYN → (müştəri serverə “başlayaq?” deyir)
```
```
→ SYN-ACK → (server “hə, başlayaq” deyir)
```
```
→ ACK → (müştəri “ok, başladıq” deyir)
```
 Langış yoxdur
👉 Harada istifadə olunur?
```
→ Web (HTTP/HTTPS) → 80, 443 -web saytlar
```
→ SSH → 22 -servere uzaqdan giris
→ FTP → 21 - fayl transferi
→ SMTP / IMAP / POP3 25 / 143 / 110 -Email
→ Email protokolları
SYN Flood Attack
 Sonsuz SYN paket göndərir → server cavab verə bilmir → çökür.
```
Half-Open Scan (SYN Scan)
```
Hücumçu belə edir:
 SYN göndərir
```
 SYN/ACK gəldikdən sonra ACK göndərmir (bağlantını tamlamır)
```
Bu, portun açıq/açıq olmadığını öyrənmək üçündür.
Nmap-də ən məşhur skandır: nmap -sS 192.168.1.10
```
Linuxda: netstat –tn ve ya ss –t
```
SYN paketlərini izləmək: sudo tcpdump tcp[tcpflags] & 2 != 0
Özün SYN scan et: nmap -sS <target-ip>
📌 Intrusion dünyasında TCP log-ları çox olur
Çünki hücumçular port scan edəndə SYN flood, half-open scan və s. görünür.
UDP
 UDP = sürətli, amma etibarsız şəbəkə protokolu.
 Bağlantı yoxdur. TCP-də olduğu kimi 3-way handshake yoxdur.
 Paket itərsə “problem deyil”. Yəni paket itməsinə nəzarət etmir.
 Handshake YOXDUR. Çünki heç bir təsdiqləmə, yoxlama, yenidən göndərmə prosesi yoxdur.
 Linuxda UDP portali: ss –u –1
 DNS UDP sorğusu sınağı: dig google.com +notcp
 UDP trafikini canlı izləmək: sudo tcpdump udp
👉 Harada istifadə olunur?
Servis Port Səbəb
DNS 53 Sürətli sorğu-cavab
DHCP 67/68 IP avtomatik verilməsi
```
VoIP (Zənglər) - Təxirəsalınmazdır, gecikmə kritikdir
```
Online oyunlar - Real-time hərəkət lazımdır
```
Streaming (bəziləri) - Sürət önəmlidir
```
📌 Intrusion üçün kritik:
```
UDP ilə DDoS (UDP flood) çox edilir.
```
Port Protokol İstifadə Niyə vacibdir?
22 SSH Server idarəsi Brute force hücumlar burada
80 HTTP Web XSS, SQLi, attacks burada
443 HTTPS Secure Web MITM və SSL üzrə hücumlar
53 DNS Domain resolver DNS poisoning
3389 RDP Windows remote Bruteforce + malware giriş nöqtəsi
445 SMB Windows file share EternalBlue, WannaCry burada
25 / 587 SMTP Email Spam attacks
3306 MySQL Database SQL brute force
8080 / 8000 Alt-web ports Proxies, APIs Proxy misuse
✔ Port = “qapı”
✔ Xidmət = o qapının arxasındakı proqram
Hücumçu ilk scan etdiyi şey → portlardır.
Common protocols
Gəldik şəbəkə və cybersecurity üçün ən kritik 5 protokola. Bunları 100% anlamaq → sənə log analizi,
intrusion detection, packet capture, SOC işində böyük üstünlük verəcək.
 HTTP/HTTPS
 SSH
 DNS
 DHCP
 ARP
HTTP / HTTPS
Nədir?
▪ HTTP = Web səhifələrinin protokolu. Saytlar, API-lər, browser–server arasında bütün
məlumat bununla gedir.
```
▪ HTTPS = Şifrələnmiş HTTP (TLS/SSL ilə).
```
```
http://example.com → təhlükəsiz deyil
```
```
https://example.com → şifrələnmiş
```
Necə işləyir?
```
▪ Brauzer → serverə request göndərir (GET, POST).
```
```
▪ Server → cavab verir (HTML, JSON və s.).
```
▪ HTTPS-də hər şey şifrələnir.
▪ Linuxda:
```
Web server log oxumaq (Apache/Nginx) : sudo tail -f /var/log/nginx/access.log
```
Ve ya sudo tail -f /var/log/apache2/access.log
Curl ilə HTTP sorğusu göndərmək: curl -I https://google.com
Şübhəli sorğunu test etmək: curl
"http://testphp.vulnweb.com/listproducts.php?cat=1' OR '1'='1"
Məsələn, bir sayta daxil olursan:
GET /index.html HTTP/1.1
```
Host: google.com
```
User-Agent: Chrome
Server response qaytarır:
HTTP/1.1 200 OK
Content-Type: text/html
və HTML, JSON, fayl və s. göndərilir.
Niyə vacibdir?
▪ XSS, SQLi, CSRF, Session hijacking kimi hücumlar burada olur.
▪ Intrusion detection-də URL-ləri, header-ləri, status kodlarını oxuyursan.
```
SSH (Port 22)
```
Nədir?
▪ Serverə uzaqdan giriş üçündür.
▪ Bütün trafik tam şifrəlidir.
Niyə vacibdir?
▪ Bruteforce hücumlarının 90%-i SSH portuna gəlir.
▪ Loglar: /var/log/auth.log
```
DNS (Port 53)
```
Nədir?
Ad → IP çevirir.
google.com → 142.250.184.238
Niyə vacibdir?
 DNS spoofing
 DNS cache poisoning
 Malware-lərin ən çox istifadə etdiyi ərazi
DHCP
Nədir?
Şəbəkəyə qoşulan cihazlara avtomatik IP verən protokoldur.
DHCP cihazlara verir:
 IP
 Gateway
 DNS
 Subnet mask
Niyə vacibdir?
```
▪ DHCP spoofing (attacker fake DHCP server qurur)
```
▪ Man-in-the-middle başlatmaq olur
```
ARP (Layer 2 protokolu)
```
Nədir?
IP → MAC çevrilməsi.
Yəni: “Bu IP kimdədir? MAC ünvanını ver.”
```
ARP = Local networkdə “address book”.
```
Niyə vacibdir?
⚠️Burada ən məşhur hücum var:
ARP Spoofing → Man-in-the-middle
Attacker özünü gateway kimi göstərir.
Protokol Komanda Nə görəcəksən
HTTP curl example.com Raw HTML
HTTPS curl -I https://google.com Header-lər + 200 OK
SSH ssh localhost SSH bağlantısı
DNS nslookup google.com DNS record
DHCP journalctl -u NetworkManager Verilən IP logları
ARP arp -a IP–MAC cədvəli
```
✔️Paket analizi (başlanğıc)
```
Wireshark-la 5 dəqiqəlik təcrübə:
 bir ping paketi aç,
 bir HTTP sorğusuna bax.
```
🛡️Niyə sənə bunlar lazımdır? (Layihə üçün izah)
```
Sən gələcəkdə:
 Suricata/Zeek log-larından feature çıxaracaqsan,
 pcap-ları analiz edəcəksən,
 “bu trafik normaldır ya anormal?” deyə qərar verəcəksən,
 ML modeli üçün real intrusions-ları ayıracaqsan.
➡️ Bunların hamısının kökü network + Linuxdur.
Bu həftə bunları rahatca öyrənsən, növbəti həftələr çox asan keçəcək.
```
Results;
```
1️⃣Linux = Bütün cybersecurity dataları & loglar Linux-dadır.
```
2️⃣Networking =Hücumlar şəbəkəyə gəlir (request, paket, trafik).
```
Bu ikisi sənin “super gücün” olacaq.
Linux and Networking
You are the system's defender.
The defender's most important foundation:
Know Linux
```
(because all threat detection, logs, IDS-s, servers are on Linux)
```
Understand networking
```
(how networks work = then detecting attacks becomes very easy)
```
This week everything should be fundamental, because in the future:
ML-based intrusion detection,
Suricata/Zeek log analysis,
real-time anomaly detection,
automated response
all of these are based on Linux + networking knowledge.
```
1 Week: Linux Basics (Practical, 1–2 hours)
```
All threat detection, logs, IDS-s, servers are on Linux
Files and Directories
• pwd – shows the path of the current directory
• ls – lists files
• ls -l – detailed list
• ls -a – shows hidden files
• cd – navigate between directories
• cd .. – go up one level
• mkdir – create a directory
• rmdir – remove empty directory
• rm – remove a file
• rm -r – remove directory and its contents
• cp – copy file/directory
• cp -r – copy directory
• mv – move/rename file or directory
• touch – create empty file
• cat – display file content
• head – show first lines of file
• tail – show last lines of file
```
• nano – edit file (terminal editor)
```
• vi – another terminal editor
• find – find file/directory
```
• locate – find quickly (database-based)
```
• chmod – change file permissions
• chown – change file owner
• ln – create symbolic link
• file – get information about file type
• stat – detailed file information
• basename – show the last part of a path
• dirname – show the directory part of a path
• tree – display directory structure as a tree
• history – show commands you've typed
File Content and Search
• grep – search in file content
• grep -i – case-insensitive search
• grep -r – recursive search within directory
• wc – count words, lines, characters
• diff – compare two files
• cmp – byte-by-byte comparison of two files
• sort – sort file lines
• uniq – show unique lines
• cut – select fields from file
• head -n – show first n lines
• tail -n – show last n lines
• less – read file page by page
• more – simple version of less
• tac – display file in reverse order
• split – split file into parts
• cat file1 file2 > merged – merge files
• tee – read file and write simultaneously
• echo – output text
• printf – formatted text output
• xargs – execute commands by reading file/data
• find . -type f -name "*.txt" – find specific files
• grep "pattern" file.txt – find pattern in file
• grep -v "pattern" – show lines without pattern
• grep -c "pattern" – count pattern occurrences
• awk – process text fields
```
• sed – modify text (stream editor)
```
• cut -d',' -f1 – select column from CSV file
• comm – show difference between two files
• tail -f logfile.log – monitor file in real-time
• watch – repeat command at intervals
System and Process Management
```
• top – real-time system monitor (CPU, RAM, processes)
```
• htop – visual, more comfortable version of top
• ps – show processes
• ps aux – show all processes in detail
• kill PID – stop process
• kill -9 PID – force kill process
• pkill process_name – stop process by name
• jobs – show background jobs
• fg %1 – bring background job to foreground
• bg %1 – continue job in background
• uptime – show how long system has been running
• free -h – show RAM and swap status
• df -h – show disk usage
• du -sh folder/ – show folder size
• uname -a – show system information
• hostname – computer name
• whoami – current user
• id – user ID and group information
• last – show last user logins
• uptime – system runtime and load
Network and Communication
• ping example.com – ping a server
• curl example.com – send HTTP request
• wget URL – download file
```
• ifconfig – show network interfaces (old Linux)
```
```
• ip a – show network interfaces (modern)
```
• netstat -tulnp – open ports and connections
• ss -tulnp – netstat alternative
• traceroute example.com – show packet route
• nslookup example.com – find domain's IP
• dig example.com – DNS query
Package and System Management
```
• apt update – update package information (Debian/Ubuntu)
```
• apt upgrade – upgrade packages
• apt install package_name – install package
• apt remove package_name – remove package
• dpkg -i package.deb – install deb file
• snap install package_name – install snap package
• systemctl status service – service status
• systemctl start service – start service
• systemctl stop service – stop service
• journalctl -xe – read system logs
```
Process and System Management (Detailed)
```
top – Real-time System Monitor
Shows CPU, RAM, processes list and load. Updates live. q → exit
```
Practical: Open top in terminal and look: which processes use a lot of CPU?
```
CPU usage shows how much the program in the system is running. RAM usage shows how
much memory each process is holding.
htop – Visual System Monitor
More visual and comfortable version of top. You can select and stop processes, see
RAM/CPU load with colors. F10 → exit
ps aux – Show All Processes
Shows all processes running in the system
• USER – user running the process
• PID – process ID
• CPU, MEM – resource usage
```
Practical: ps aux | grep firefox – find specific program's PID
```
kill – Stop Process
Stops process by PID
Force stop: kill -9 PID
pkill – Stop Process by Name
Stop process without knowing PID, just write the process name
jobs / fg / bg – Manage Background Jobs
• & → run process in background
• jobs → show background processes
• fg → bring background job to foreground
• bg → continue job in background
systemctl – Manage Services
• status → show service status
• start → start service
• stop → stop service
• restart → restart service
```
Networking Basics (1–2 hours)
```
How networks work = then detecting attacks becomes much easier?
This section is critical for understanding intrusions.
IP, MAC, Gateway, DNS — What Are They?
IP Address
Your device's address on the internet.
Like your home mailing address, different for each device.
For example:
• Local: 192.168.1.10
```
• On Internet (public): 89.176.45.17
```
```
In Linux terminal: ip addr show or ifconfig (numbers starting with inet are local IP)
```
```
On Windows: ipconfig (IPv4 Address is my local IP)
```
```
To see Public IP on Linux: curl ifconfig.me or curl icanhazip.com (will show the
```
```
public IP seen on internet)
```
```
Practice:
```
ping 8.8.8.8 # Ping an IP, check connection
traceroute 8.8.8.8 # Route to IP
whois 8.8.8.8 # Information about IP
Why important for intrusion? 99% of attacks come from an IP. In log analysis, the first
thing you check is the IP.
MAC Address
```
Unique "passport" number of device's network card (NIC).
```
Unique – each network card has its own MAC.
```
Doesn't change (actually can be spoofed, but doesn't change by default).
```
```
Example: A4:5E:60:AF:21:B9
```
```
Usually doesn't change, but can be spoofed (faked).
```
Many attacks and defense mechanisms are based on MAC.
```
In Linux practice: ip link show or ifconfig (look for section starting with link/ether)
```
```
Example: link/ether a4:5e:60:af:21:b9 brd ff:ff:ff:ff:ff:ff (This is your
```
```
device's network card MAC address).
```
```
MAC Spoofing (Change MAC Address) – Practical
```
```
(Showing for information, not a dangerous operation)
```
sudo ip link set dev wlan0 down
sudo ip link set dev wlan0 address 11:22:33:44:55:66
sudo ip link set dev wlan0 up
```
Note: Network interface name can be wlan0, eth0, enp3s0, etc.
```
ARP Poisoning
Attacker "spoofs" their MAC address and presents themselves as "gateway" between
```
victim's device and router. This creates MITM (Man-in-the-Middle) situation.
```
MAC Flooding
Flood switch's MAC table with tons of fake MAC addresses → switch starts behaving like a
"hub" → all traffic is broadcast → attacker captures packets through sniffing.
Network Access Control
In companies, sometimes only authorized MACs can connect to the network.
```
Why important? Layer 2 attacks (ARP poisoning, MAC flooding) are based on this.
```
```
Gateway (Default Gateway)
```
Your computer's "exit gate" to the internet.
Router's IP address:
```
Usually: 192.168.1.1, 192.168.0.1, 10.0.0.1
```
How to find your Gateway on Linux?
route –n
ip route show
```
nmcli device show (with NetworkManager)
```
```
Importance: Many attacks "man-in-the-middle" the gateway (ARP spoofing).
```
```
DNS (Domain Name System)
```
System that converts domains to IPs.
DNS is the internet's "phone book".
google.com → 142.250.184.238
If DNS didn't exist, you'd have to type IP for every site.
On Linux: cat /etc/resolv.conf
You'll see something like:
nameserver 8.8.8.8
nameserver 1.1.1.1
```
With NetworkManager: nmcli device show | grep DNS (shows more accurately).
```
Attackers mess with DNS a lot:
DNS Spoofing
Attacker changes DNS response → you type google.com, but gets sent to fake site.
DNS Hijacking
Attacker takes over DNS server → all traffic goes to wrong IP.
Malware Changes DNS
Malicious program changes your DNS server like this: 1.1.1.1 → 185.66.77.23
```
(malicious). And all websites redirect you to wrong server.
```
Why important? Very popular attack: DNS spoofing, DNS hijacking. Malware sets up
its own "malicious DNS" server.
TCP
Reliable connection.
Resends packet if lost.
Requires 3-way handshake to establish connection:
```
• SYN → (client says "shall we start?")
```
```
• SYN-ACK → (server says "yes, let's start")
```
```
• ACK → (client says "ok, we started")
```
No hand-waving.
Where is it used?
Service Port Purpose
```
Web (HTTP/HTTPS) 80, 443 web sites
```
SSH 22 remote server access
FTP 21 file transfer
SMTP / IMAP / POP3 25 / 143 / 110 Email
SYN Flood Attack
Send infinite SYN packets → server can't respond → crashes.
```
Half-Open Scan (SYN Scan)
```
Attacker does this:
1. Sends SYN
2. After SYN/ACK arrives, doesn't send ACK (doesn't complete connection)
This is to discover if port is open/closed.
Most famous scan in Nmap: nmap -sS 192.168.1.10
On Linux: netstat –tn or ss –t
Monitor SYN packets: sudo tcpdump tcp[tcpflags] & 2 != 0
Do your own SYN scan: nmap -sS <target-ip>
In intrusion world, TCP logs are everywhere Because when attackers port scan, SYN
flood, half-open scan etc. appear.
UDP
```
UDP = fast, but unreliable network protocol.
```
No connection. No 3-way handshake like TCP.
If packet is lost "no problem". Doesn't monitor packet loss.
No handshake. Because there's no confirmation, checking, resend process.
On Linux UDP ports: ss –u –1
DNS UDP query test: dig google.com +notcp
Monitor UDP traffic live: sudo tcpdump udp
Where is it used?
Service Port Reason
DNS 53 Fast query-response
DHCP 67/68 Auto IP assignment
```
VoIP (Calls) - No delay, latency critical
```
Online games - Real-time movement needed
```
Streaming (some) - Speed matters
```
```
Critical for intrusion: UDP DDoS (UDP flood) is very common.
```
Ports Summary
Port Protocol Usage Why Important?
22 SSH Server management Brute force attacks here
80 HTTP Web XSS, SQLi, attacks here
443 HTTPS Secure Web MITM and SSL attacks
53 DNS Domain resolver DNS poisoning
3389 RDP Windows remote Bruteforce + malware entry point
445 SMB Windows file share EternalBlue, WannaCry here
25 / 587 SMTP Email Spam attacks
3306 MySQL Database SQL brute force
8080 / 8000 Alt-web ports Proxies, APIs Proxy misuse
✔ Port = "door" ✔ Service = the program behind that door
First thing attacker scans → ports.
Common Protocols
We've reached the 5 most critical protocols for networking and cybersecurity.
Understanding these 100% → will give you big advantage in log analysis, intrusion
detection, packet capture, SOC work.
1. HTTP/HTTPS
2. SSH
3. DNS
4. DHCP
5. ARP
HTTP / HTTPS
What is it?
```
HTTP = Web pages protocol. Sites, APIs, browser–server communication all go through
```
this.
```
HTTPS = Encrypted HTTP (with TLS/SSL).
```
```
http://example.com → not secure https://example.com → encrypted
```
How does it work?
```
Browser → sends request to server (GET, POST). Server → responds (HTML, JSON, etc.). In
```
HTTPS, everything is encrypted.
On Linux:
```
Read web server logs (Apache/Nginx):
```
sudo tail -f /var/log/nginx/access.log
or
sudo tail -f /var/log/apache2/access.log
Send HTTP request with curl:
curl -I https://google.com
Test suspicious request:
curl "http://testphp.vulnweb.com/listproducts.php?cat=1' OR '1'='1"
For example, when you visit a site:
GET /index.html HTTP/1.1
```
Host: google.com
```
User-Agent: Chrome
Server returns response:
HTTP/1.1 200 OK
Content-Type: text/html
and HTML, JSON, file, etc. is sent
Why important?
XSS, SQLi, CSRF, Session hijacking attacks happen here.
In intrusion detection you read URLs, headers, status codes.
```
SSH (Port 22)
```
What is it?
For remote access to servers.
All traffic is fully encrypted.
Why important?
90% of brute force attacks come to SSH port.
```
Logs: /var/log/auth.log
```
```
DNS (Port 53)
```
What is it?
Converts name → IP.
google.com → 142.250.184.238
Why important?
DNS spoofing DNS cache poisoning Most used area by malware
DHCP
What is it?
Protocol that automatically assigns IPs to devices connecting to network.
DHCP gives devices:
• IP
• Gateway
• DNS
• Subnet mask
Why important?
```
DHCP spoofing (attacker creates fake DHCP server) Can initiate man-in-the-middle
```
```
ARP (Layer 2 Protocol)
```
What is it?
IP → MAC conversion. That is: "Which IP is this? Give me MAC address."
```
ARP = "address book" on local network.
```
Why important?
Most famous attack is here: ARP Spoofing → Man-in-the-Middle
Attacker presents themselves as gateway.
Protocol Commands Summary
Protocol Command What you'll see
HTTP curl example.com Raw HTML
HTTPS curl -I https://google.com Headers + 200 OK
SSH ssh localhost SSH connection
DNS nslookup google.com DNS record
DHCP journalctl -u NetworkManager Assigned IP logs
ARP arp -a IP–MAC table
```
✔️Packet Analysis (Beginning)
```
5-minute practice with Wireshark:
• Open a ping packet,
• Look at an HTTP request.
```
🛡️Why Do You Need All This? (Project Explanation)
```
In the future you will:
• Extract features from Suricata/Zeek logs,
• Analyze pcap files,
• Decide "is this traffic normal or abnormal?",
• Separate real intrusions for ML model.
The root of all these is network + Linux. If you learn these comfortably this week, the
coming weeks will be much easier.
```
Results:
```
```
Linux = All cybersecurity data & logs are on Linux.
```
```
Networking = Attacks come to network (request, packet, traffic).
```
These two will be your "super powers".