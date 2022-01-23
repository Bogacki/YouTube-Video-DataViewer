# YouTube-Video-DataViewer

Aby oprogramowanie działało należy pobrać chrome_driver, zawarłem go w repozytorium, standardowo chrome driver znajduje się w folderze projektu oraz ścieżka jest ustawiona w ten sposób aby od razu go wykrywała, jednak można go również umieścić w dowolnym innym miejscu na dysku, jednak wtedy trzeba podmienić ścieżkę w zmiennej chrome_driver_path w pliku youtube.py

Oprogramowanie korzysta z Selenium, które otwiera przeglądarke i wykonuje w niej akcje na podstawie działań w kodzie. Z początku projekt miał być ambitniejszy dlatego użyłem Selenium a nie na przykład BeautifulSoup.

Po otwarciu programu widzimy pole typu Input do którego wpisujemy frazę, którą chcemy wyszukać w YouTube, po wciśnięciu Search pojawi się 5 przycisków, które zawierają informacje z 5 pierwszych filmów znalezionych w YT. Po wciśnięciu przycisku z filmem ponieżej pojawią się podstawowe informacje o filmie jak tytuł, autor, długość, data publikacji, adres do linku. Oprogramowanie mogłoby być wykorzystane, aby w szybki sposób pobierać tego typu dane do excela w większej ilości. Nie wykorzystałem samego selenium, do pobierania tych informacji tylko osobną biblioteke, która posiada metodę pozwalającą pobrać tego typu informacje dzięki linkowi filmu.

