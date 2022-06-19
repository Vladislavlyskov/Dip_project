        FROM python:3.8.5-alpine
        # Работаем над системой, которая создана из образа на котором изначльно установлен Питон3

        WORKDIR .
        # указывает на рабочую директорию
        # . (точка) - значит текущая директория

        RUN apk update && apk add \
            gcc \
            musl-dev \
            python3-dev \
            libffi-dev \
            openssl-dev cargo \
            cargo \
            zlib-dev

         # RUN - команда которая выполняет действия которые ей пропишем
         # apk update\add - команда для обновления\ установки программы из контейнера


        RUN python -m install --upgrade pip
        # komanda dlya obnovlenia PIP

        COPY requirements.txt requirements.txt
        # COPY - komanda dla kopirovania s komputera na komteiner
        # sleva vsegda computer | sprava konteiner

        RUN pip install -r requirements.txt
        # ystanovka zavisimostei iz faila 'requirements.txt'

        COPY . .
        # perenosim vse faili

