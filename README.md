![KI-ENNA](https://github.com/statistical-thinking/KI.ENNA/blob/main/KI-ENNA.png?raw=true)

# KI-ENNA
(E)in (N)euronales (N)etz zum (A)usprobieren

# Autoren
Prof. Dr. habil. Dennis Klinkhammer

# Voraussetzungen
TensorFlow in Python (Anaconda Cloud); MicroPython (Thonny)

# Materialien und Kurzanleitung
Im Ordner "python" befindet sich jeweils ein Datensatz im CSV-Format sowie Jupyter Notebooks für zwei Neuronale Netze zur Klassifikation.
Die Datensätze wurden jeweils als Grundlage für das Training der Neuronalen Netze mit TensorFlow in Python verwendet.
Die Parameter der Neuronalen Netze wurden daraufhin als TXT-Datei extrahiert.
Im Ordner "micropython" befindet sich der Code zur Initialisierung des Microcontrollers.
Dieser wird via Thonny auf den Microcontroller kopiert und dieser anschließend neu gestartet.
Als Beispieldatensätze stehen der IRIS Datensatz und der DIABETES Datensatz zur Verfügung.
'ReLU', 'Leaky ReLU', 'Sigmoid', 'Softmax' und 'Tanh' stehen als Aktivierungsfunktionen zur Verfügung.
Bei Bedarf können andere Klassifikationsdaten für das Training in Python verwendet werden.
Bei anderen Datensätzen sind die Parameter der Neuronalen Netze entsprechend anzupassen.
KI-ENNA-B(asic) funktioniert direkt in Thonny und benötigt weder Display noch RGB-Matrix.

# Lizenz
In der aktuellen Version 2.0 steht KI-ENNA unter der German Free Software License zur Verfügung.
