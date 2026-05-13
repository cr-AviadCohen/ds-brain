# Phoenix Review Hebrew.docx

main

# **Phoenix**

Phoenix היא מערכת **EDR/XDR**:

* EDR = מנטרת מה קורה על מחשבים (מחשבים של לקוחות)
* XDR = מוסיפה גם מידע חיצוני (ענן, SaaS, לוגים)
* המטרה: **לזהות מתקפות בזמן אמת ולהגיב אוטומטית**

# **איך המערכת בנויה ?**

יש 3 שכבות עיקריות:

## **1. 🖥️ שכבת האג’נט (Endpoint)**

זה מה שרץ על המחשב של הלקוח:

* נקרא: **Sunbird Agent**
* כתוב ב־Rust

תפקידים:

* אוסף כל מה שקורה במחשב:
  + תהליכים (process)
  + קבצים
  + רשת
  + התחברויות
  + registry (Windows)
* עושה קצת בדיקות מקומיות (Sigma/YARA בסיסי)
* יכול לחסום דברים מיד (inline prevention)
* שולח הכל לשרת

## **2. ☁️ שכבת השרת (Phoenix Backend)**

זה הלב של המערכת (עשרות microservices)

### **🔌 כניסה למערכת**

* sensor-gateway → מקבל את כל המידע מהאג’נטים

### **📦 העברת נתונים**

* Kafka (Redpanda) → “אוטובוס הודעות פנימי”

### **🧠 זיהוי מתקפות**

* cep-service → מפעיל חוקי Sigma
* מזהה “אירוע חשוד” → נקרא **Detection**

### **🔗 קורלציה (חשוב!)**

* correlation-service
* מחבר כמה detections לאירוע אחד גדול:
   👉 נקרא **Malop (מתקפה מלאה)**

## **🗄️ אחסון מידע**

* ClickHouse → כל האירועים הגולמיים (מאוד מהיר)
* PostgreSQL → נתונים עסקיים (משתמשים, התקפות, חוקים)
* Redis → מידע זמני (מצב פעולות, cache)

## **🎛️ שליטה ותגובה**

* command-service → שולח פקודות למחשבים
* dispatcher-service → מעביר בפועל לאג’נטים (MQTT / WNS)

פקודות לדוגמה:

* kill process
* isolate machine
* quarantine file
* run script

## **🧑‍💻 ממשק אנליסטים (Portal)**

* Next.js web app
* מציג:
  + מתקפות (Malops)
  + מכונות
  + לוגים
  + גרפים של תקיפה
* דרכו האנליסטים שולחים פעולות

## **🌐 XDR (נתונים חיצוניים)**

* xdr-worker
* מושך לוגים ממערכות חיצוניות (AWS, SIEM וכו’)
* מעביר אותם למערכת כאילו הגיעו מהאג’נט

# **🔁 Data Flow כללי**

****Agent → Gateway → Kafka → CEP → Correlation → Storage → Portal

# **🔥 דוגמת Flow אמיתית (מתקפה בעולם האמיתי)**

נניח שיש מתקפה על מחשב של עובד:

## **🧨 שלב 1: התחלה על המחשב**

האקר מריץ:

* powershell.exe
* מוריד קובץ חשוד
* מנסה לגנוב credentials

📡 האג’נט רואה:

* process start
* file write
* network connection

ושולח הכל לשרת.

## **📥 שלב 2: הגעה לשרת**

* sensor-gateway מקבל את האירועים
* שולח ל־Kafka (raw-events)
* שומר ב־ClickHouse

## **🧠 שלב 3: זיהוי חשד (CEP)**

cep-service רואה:

* PowerShell + הורדה + ביצוע חשוד

👉 מפעיל Sigma rule

📌 תוצאה:

Detection נוצר:

* “Suspicious PowerShell execution”

## **🔗 שלב 4: קורלציה (השלב הקריטי)**

correlation-service מקבל כמה detections:

* PowerShell execution
* File drop
* Network C2 connection

הוא מחבר אותם יחד:

👉 יוצר **Malop אחד:**

“Possible credential theft attack”

## **📊 שלב 5: הצגה לאנליסט**

ב־Portal:

* מופיע אירוע אחד גדול
* לא 3 אירועים נפרדים
* עם timeline מלא של התקיפה

## **🚨 שלב 6: תגובה**

האנליסט לוחץ:

* “Isolate machine”

זה קורה:

Portal → command-service → Kafka → dispatcher-service → agent

האג’נט:

* חוסם רשת
* עוצר תקשורת
* שולח אישור חזרה

# **🧠 תמונה מנטלית פשוטה**

אפשר לחשוב על המערכת ככה:

[ מחשבים של לקוח ]

↓

(עיניים)

Sunbird Agent

↓

(כביש מהיר)

Kafka

↓

(מוח)

CEP + Correlation

↓

(מערכת ניהול)

Portal

↓

(ידיים)

Command → Agent actions

# 

# **🧩 סיכום רכיבים לפי תפקיד**

## **🖥️ Endpoint**

* Sunbird Agent
* collectors (ETW / eBPF / macOS ES)
* local detection

## **🚪 Ingestion**

* sensor-gateway
* sensor-auth

## **🧠 Detection**

* cep-service (Sigma rules)
* Flink (CEP מתקדם)

## **🔗 Correlation**

* correlation-service (Malops)

## **🗄️ Storage**

* ClickHouse (events)
* PostgreSQL (state)
* Redis (cache)

## **🎛️ Control**

* command-service
* dispatcher-service

## **🧑‍💻 UI**

* Next.js portal

## **🌍 XDR**

* xdr-worker
* integration-proxy
