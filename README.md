# KI.ENNA
ENNA - (E)in (N)euronales (N)etz zum (A)usprobieren

# Autoren
Prof. Dr. Dennis Klinkhammer

# Voraussetzungen
TensorFlow in Python (Anaconda Cloud); MicroPython (Thony)

# Anleitung
Im Ordner "python" befindet sich ein Datensatz im CSV-Format zur Klassifikation von Diabetes sowie Jupyter Notebooks für zwei Neuronale Netze.
Dieser Datensatz wurde als Grundlage für das Training der Neuronalen Netze mit TensorFlow in Python verwendet.
Die Parameter des Neuronalen Netzes wurden daraufhin als TXT-Datei extrahiert.
Im Ordner "micropython" befindet sich der Code zur Initialisierung des Microcontrollers.
Dieser wird via Thonny auf den Microcontroller kopiert und dieser anschließend neu gestartet.
Bei Bedarf können andere Klassifikationsdaten für das Training in Python verwendet werden.
Als Beispieldatensätze stehen der IRIS Datensatz und der DIABETES Datensatz zur Verfügung.
Entsprechend sind die Parameter im Code zur Initialisierung des Microcontrollers und des Datensatzes anzupassen.
