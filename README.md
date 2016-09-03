Object detection (нахождение объектов).
Для того чтобы находить объекты на видеопотоке с камеры необходимо:
- Python 2.7
- Scipy и Numpy (желательно последних версий)
- Библиотека OpenCV http://opencv.org/downloads.html  
В примере используется
- Python 2.7.12
- Scipy 0.9.0 (python2.7)
- Numpy 1.10.1 (python2.7)
- OpenCV 3.0.0

Установка библиотеки:
- Устанавливаем Python
- Устанавливаем Scipy и Numpy (Необходимо для нормальной работы библиотеки)
- Распаковываем OpenCV
- Открываем C:\"Папка с OpenCV"\opencv\build\python\2.7\x86\  
или C:\"Папка с OpenCV"\opencv\build\python\2.7\x64\  
В зависимости от версии Python //Рекомендую x86
- Копируем файл cv2.pyd 
Вставляем в: C:\"Папка с Python"\Lib\site-packages\  
// Обычно: C:\Python27\Lib\site-packages\
- Библиотека установлена, осталось импортировать библиотеку в скрипт
import cv2


