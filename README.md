# Introduction 
Dieses Projekt enthält Skripte für folgende Aufgaben:

    - Aufzeichnung von Objektbildern
    - Entfernen des Hintergrundes der Objektbilder
    - Abspeichern von einzelnen Frames aus einem Video für Hintergrundbilder
    - Überlappung von mehreren Objekte über ein Hintergrundbild mit:
        - Anpassung der Bounding Boxen
        - Bildbearbeitungen (Unschärfe, Geräuschinjektion, Helligkeitsanpassung, Farbraumtransformation, Zufälliges Entfernen eines Teilbereichs)

# Getting Started
1.	Installation der requirements.txt


### Skripte

    # save_multiple_camera_frames.py
    Skript zur Erstellung der Objektbilder mit Anlegen der Ordnerstruktur für Objektbilder mit Hintergrund und mit ausgeschnittenem Hintergrund. 
    - Eingabe:
        - 4 stellige Produktnummer
        - Produktname


    # save_video_frames.py
    Speichert jeden 25. Frame des gewählten Videos ab.
    - Eingabe:
        - Name des Videos eingeben


    # multiple_overlapping.py
    Alter Stand der frühen Experimentreihen bei dem ein Hintergrundbild mit einem bereits eingefügten Objekt weitere Objekte erhält.
    - Eingabe:
        - Videonummer eingeben (vid, vid1, vid2 oder vid3)
        - "m" eingeben für m das 2. Objekt übereinanderlegen, ansonsten wird das erste Objekt eingefügt


    # generate_dataset.py
    Zusammenführen der erstellten kleinen Datensätze zur Erstellung eines großen Datensatzes
    - Eingabe:
        - Anzahl der kleinen Datensätze angeben
        - Namen der kleinen Datensätze angeben


    # exp8_final_dataset.py
    Neuester Stand der Überlappung der Objektbilder auf den Hintergrund. Überlappung zwischen 4 und 8 Objekten. Erstellt 2 Datensätze, einer enthält unbearbeitete Objektbilder, einer enthält Unschärfe Effekt, Helligkeitsanpassung und Farbraumtransformation.
    - Eingabe:
        - Anzahl der erwünschten, zufälligen Videos (aus vid, vid1, vid2 oder vid3)


    # exp8_generate_dataset.py
    Zusammenlegen der erstellten Datensätze aus exp8_final_dataset.py aufgrund der Videoanzahl.
    - Eingabe:
        - Anzahl der kleinen Datensätze angeben
        - Namen der kleinen Datensätze angeben


    # exp7_with_adjust_bbs.py
    Experimentreihe 7 mit Anpassung der Bounding Boxen bei Überlappung von Objekten und Einführung der Bildbearbeitungen mit Unschärfe Effekt, Geräuschinjektion, Helligkeitsanpassung, Farbraumtransformation und dem Zufälligen Entfernen eines Teilbereichs des Objektes
    - Eingabe:
        - Anzahl der erwünschten, zufälligen Videos (aus vid, vid1, vid2 oder vid3)


    # exp7_without_adjust_bbs.py
    Experimentreihe 7 ohne Anpassung der Bounding Boxen bei Überlappung von Objekten und Einführung der Bildbearbeitungen mit Unschärfe Effekt, Geräuschinjektion, Helligkeitsanpassung, Farbraumtransformation und dem Zufälligen Entfernen eines Teilbereichs des Objektes
    - Eingabe:
        - Anzahl der erwünschten, zufälligen Videos (aus vid, vid1, vid2 oder vid3)


    # exp6_adjust_bbs.py
    Experimentreihe 6 mit Anpassung der Bounding Boxen bei Überlappung von Objekten. Die Objekte werden bis zum vorletzen überprüft, ob sie von einem Objekt überlagert werden, falls dies der Fall ist wird die Bounding Box angepasst.
    - Eingabe:
        - Anzahl der erwünschten, zufälligen Videos (aus vid, vid1, vid2 oder vid3)


    # overlapping_images.py
    Alter Stand der Experimentreihe 6 für die Überlappung der Objektbilder auf den Hintergrund. Überlappt zwischen 4 und 8 Objekte übereinandern. 
    - Eingabe:
        - Anzahl der erwünschten, zufälligen Videos (aus vid, vid1, vid2 oder vid3)


    # problem_check_result_images_for_transparency.py
    Die Objektbilder mit Hintergrund von den angegebenen Objektnummer werden zu Testzwecken ausgeschnitten und in einem neuen Ordner abgelegt.


    # problem_crop_again.py
    Skript zur Fehlerbehebung eines übrig gebliebenen transparenten Bereichs im finalen Objektbild. Ein erneutes Ausschneiden kann diesen Problem lösen.
    - Eingabe:
        - Produktnummer des Objektbilders zum erneuten Ausschneiden eingeben
        - Kamera des fehlerhaften Bildes eingeben


    # problem_replace_area.py
    Skript zur Fehlerbehung von sichtbaren Kameras im finalen Objektbild. Durch das Ausschneiden eines ausgewählten Bereichs kann dieser Bereich geschwärzt werden und durch das Skript problem_crop_again.py das Objektbild final ausschneiden.
    - Eingabe:
        - Produktnummer des Objektbilders zum Schwärzen eines Teilbereichs eingeben
        - Kamera des fehlerhaften Bildes eingeben