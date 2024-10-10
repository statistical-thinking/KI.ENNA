# KI-ENNA
ENNA - (E)in (N)euronales (N)etz zum (A)usprobieren

# Autoren
Prof. Dr. Dennis Klinkhammer

# Voraussetzungen
TensorFlow in Python (Anaconda Cloud); MicroPython (Thony)

# Anleitung
Im Ordner "python" befindet sich jeweils ein Datensatz im CSV-Format sowie Jupyter Notebooks für zwei Neuronale Netze zur Klassifikation.
Die Datensätze wurden jeweils als Grundlage für das Training der Neuronalen Netze mit TensorFlow in Python verwendet.
Die Parameter der Neuronalen Netze wurden daraufhin als TXT-Datei extrahiert.
Im Ordner "micropython" befindet sich der Code zur Initialisierung des Microcontrollers.
Dieser wird via Thonny auf den Microcontroller kopiert und dieser anschließend neu gestartet.
Als Beispieldatensätze stehen der IRIS Datensatz und der DIABETES Datensatz zur Verfügung.
Beim IRIS Datensatz stehen 'ReLU', 'Sigmoid' und 'Tanh' als Aktivierungsfunktionen zur Verfügung.
Aufgrund des begrenzten Ressourcen sind es beim DIABETES Datensatz lediglich 'ReLU' und 'Sigmoid'.
Bei Bedarf können andere Klassifikationsdaten für das Training in Python verwendet werden.
Bei anderen Datensätzen sind die Parameter der Neuronalen Netze entsprechend anzupassen.

# KI-ENNA mit Zubehör
![KI-ENNA](https://github.com/statistical-thinking/KI.ENNA/blob/main/KI-ENNA.jpg?raw=true)
