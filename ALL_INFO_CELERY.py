"""

 Самое Важное!!!
 Всегда ДУМАТЬ! перед тем, как что-либо сделать, необходимо всё тщательно обдумать

 Радоваться Жизни  Радоваться разным мелочам

 Ценить:         Ценить то что есть и стремиться к лучшему, Ценить сегодняшний день и брать МАКСИМУМ
 Быть проще:     Ко всему относиться Проще и Спокойнее без Волнения
 Слушать Других: Прислушиваться к мнению других людей они могут быть правы  И делать выводы
 Время:          Тайм-менеджмент   Грамотное распределение времени, Контроль Времени, Правильно раставлять Приоритеты
 Уверенность:    Быть уверенным в себе НО Оценивать свои силы!
 Развития:       Развиваться, Учиться, учиться и ещё раз - учиться, Саморазвитие
 Не Надеяться:   Надеяться только на себя
 Контроль:       Быть менее Эмоциональным, Совладать с Эмоциями, Контролировать свои эмоции в любой ситуации
 Внимательность: Быть Внимательным
 Спокойствие:    Быть Спокойнее, Перестать Нервничать , Быть Расслабленным, Не Злиться на себя и на других
 Режим:          Правильный Сон, Пить Воду
 Зарядка:        Бег, Тренировки, Стойка на Голове
 Тельце в тепле: НЕ переохлаждаться

 Молчание золото:  Лучше промолчать, чем сказать и потом жалеть о том, что сказал
 Соломон:          Все пройдёт, и это тоже пройдёт
 Вообще это замечательный подход: осознать, что проблема не такая уж и проблема, и вполне решаема.
 Кто ищет-тот всегда найдет!
 Искать Другие способы
 Не спеши, а то успеешь...   Успеешь, но не туда куда хотел...
 Подумай, нужно ли тебе ЭТО и для Чего
 Надо принимать вещи такими, как они есть, и пользоваться ими с наибольшей для себя выгодой.
 Если научиться принимать вещи как они есть, страдание исчезнет.
________________________________________________________________________________________________________________________


 Celery - это асинхронная очередь задач, используемая для распределенной обработки сообщений.
 Он позволяет выполнять задачи в фоновом режиме, не загружая основной поток выполнения

 Celery — это программа, которая отслеживает задачи (tasks), которые необходимо выполнить,
 и в которой есть набор обработчиков (workers), которые будут выполнять эти задачи.
 Основной смысл в том, что она (программа) может выполнять несколько задач параллельно
 и что она не блокирует поставщиков (producers) этих самых задач.

 Celery на самом деле не хранит все эти задачи в памяти. Для хранения задач есть отдельный сервис,
 называемый брокером сообщений (message broker), который по сути своей является очередью. Обычно это либо Redis,
 либо RabbitMQ. Celery следит за тем, что происходит в очереди, но хранится она внутри Redis/RabbitMQ.

 1) Рабочие процессы Celery — это рабочие процессы, которые выполняют задачи независимо друг от друга и вне контекста
 вашего основного сервиса.

 2) Celery beat — это планировщик, который определяет, когда запускать задачи. Вы также можете использовать его для
 планирования периодических задач.
 Scheduler - Планировщик

 celery Beat — планировщик; Он запускает задачи через регулярные промежутки времени, которые затем выполняются
 доступными рабочими узлами в кластере.

 Рабочие процессы составляют основу Celery. Даже если вы хотите запланировать повторяющиеся задачи с помощью
 Celery beat, процесс Celery примет ваши инструкции и выполнит их в запланированное время. Celery beat добавляет
 к этому миксу планировщик для рабочих процессов Celery.

 Создание асинхронной задачи начинается с определения функции, которая будет выполняться асинхронно.
 Для этого используем декоратор       @task

 Сценарий 1: выполнение задачи в фоновом режиме:

 import time
 from celery import Celery

 app = Celery('myapp', broker='pyamqp://guest@localhost//')

 @app.task
 def generate_report_task(arg1, arg2):
     print("Start generating report")
     time.sleep(10)
     print("Report generated")

 1) generate_report_task.apply_async(args=[arg1_value], kwargs={'key': 'value'})
 2) generate_report_task.delay(arg1_value, arg2_value)
 3) generate_report_task(arg1_value, arg2_value)

 Как запустить:
 1) apply_async - это метод, который предоставляет максимальную гибкость при запуске задачи и принимает большое количество аргументов.
 2) delay - в отличие от apply_async имеет ограниченный список принимаемых аргументов. Такой способ запуска
 мы рассматриваем, когда нужно просто запустить задачу без необходимости передавать именованные аргументы и другие параметры.
 3) Это обычный вызов функции. В таком случае задача будет выполнена сразу же, а не назначена в очередь.
------------------------------------------------------------------------------------------------------------------------
 Сценарий 2: Выполнить задачу через час:
 from datetime import datetime

 @app.task
 def publish_article(arg1, arg2):
     print(f"Publish time: {datetime.now()}")

 publish_article_after = 60 * 60 # 60 минут
 result = publish_article.apply_async(args=[article_id], countdown=publish_article_after) # countdown

 Самый простой - аргумент countdown - в переводе "обратный отсчёт".
 Он позволяет задать время в секундах, через которое задача станет доступна для выполнения.

 Важно для Redis Backend:
 Данный способ не подойдет, если вы используете Redis в качестве брокера.

 Важно для RabbitMQ Backend:
 Параметр consumer_timeout по умолчанию равен 30 минутам. Не желательно устанавливать countdown больше этого времени, иначе
 будет возбуждено исключение PRECONDITION_FAILED. Если есть такая необходимость, необходимо увеличить время в rabbitmq.conf.
------------------------------------------------------------------------------------------------------------------------
 Сценарий 3: Выполнить задачу завтра в полдень:

 from datetime import datetime

 # Получим время для примера. В нормальной ситуации -
 # нам придет аргумент с временем публикации
 now = datetime.now()
 tomorrow = now + timedelta(days=1)

 publish_article_datetime = datetime(tomorrow.year, tomorrow.month, tomorrow.day, 12, 0, 0)

 result = publish_article.apply_async(args=["some_value"], eta=publish_article_datetime) # eta

 eta - это не точное время, в которое будет выполнена задача. Указывая время, мы говорим Celery - "задача должна
 быть выполнена не раньше этого времени". Как только это время наступит - задача будет выполнена в порядке очереди
 и будет зависеть от количества задач в очереди.
------------------------------------------------------------------------------------------------------------------------
 Сценарий 4: Выставить максимальное время выполнения задачи:

 Для этого мы будем использовать аргументы soft_time_limit и time_limit. После наступления soft_time_limit в задаче
 будет возбуждено исключение SoftTimeLimitExceeded. Если задача не завершилась и наступает time_limit,
 выполнение задачи будет приостановлено.

 1) Первый вариант - передать аргументы в apply_async:

 @app.task()
 def generate_report():

     try:
         time.sleep(60 * 2)
     except SoftTimeLimitExceeded:
         print("Soft time limit exception")
         time.sleep(60 * 3)

 soft_time_limit = 60 * 1

 hard_time_limit = 60 * 2

 result = my_task.apply_async(args=[some_value], soft_time_limit=soft_time_limit, time_limit=hard_time_limit )

 2) Второй вариант - сразу указать ограничения в аргументах декоратора:

 @app.task(time_limit=60 * 60, soft_time_limit=59 * 60) # 60/59 min
 def generate_report():
     try:
         time.sleep(60 * 2)
     except SoftTimeLimitExceeded:
         print("Soft time limit exception")
         time.sleep(60 * 3)

 result = my_task.apply_async(args=[some_value])

 В результате, после запуска задачи через одну минуту мы увидим в консоли "Soft time limit exception",
 а еще через минуту задача будет принудительно завершена.
------------------------------------------------------------------------------------------------------------------------
 Сценарий 5: Отмена выполнения задачи по истечение времени:

 # Генерация будет отменена через час
 generate_report.apply_async((10, 10), expires=3600)

 # Генерация будет отменена, если через день задача не начнет выполняться
 from datetime import datetime, timedelta, timezone
 generate_report.apply_async((10, 10), kwargs,
                 expires=datetime.now(timezone.utc) + timedelta(days=1))


 Задача попала в очередь и за час ни один обработчик не смог её обработать. В таком случае нам нужно отменить
 "просроченную" задачу. Для этого применяется аргумент expires. Он принимает либо число в секундах, либо объект datetime.
------------------------------------------------------------------------------------------------------------------------
Сценарий 6: Повторное выполнение задачи при возникновении ошибки:

 Для начала разберем аргументы, которые помогут нам с детальной настройкой. Декоратор @app.task принимает:

 default_retry_delay[int]: время до следующей попытки в секундах.

 max_retries[int]: максимальное количество попыток.

 autoretry_for[list | tuple]: Принимает список или кортеж с исключениями. Автоматический повтор при возникновении
 ошибки из переданного списка.

 retry_backoff[bool|int]:при включении, задержка будет расти экспотенциально. Первая повторная попытка будет иметь
 задержку 1 секунду, вторая повторная попытка будет иметь задержку 2 секунды, третья будет иметь задержку в 4 секунды,
 четвертая будет иметь задержку в 8 секунд,

 retry_backoff_max[int]: устанавливает максимальную задержку в секундах. Рекомендуется использовать всегда при
 использовании retry_backoff, чтобы избежать слишком больших задержек.

 retry_jitter[bool]: задает случайную задержку. Принцип расчета new_num_of_seconds = random.randrange(retry_backoff + 1).
 Соответственно время задержки будет случайным числом от 0 до retry_backoff

 Теперь перейдем к коду. Есть два основных способа задействовать механизм retry.

 1) Первый способ - использовать метод .retry(). Мы можем вызывать его по какому-либо условию:

 @app.task(default_retry_delay=30, max_retries=3) # 60/59 min
 def generate_report():
    some_condition = some_logic()
    if some_condition:
      generate_report.retry()

 result = my_task.apply_async(args=[some_value])

 2) Второй способ - это передать список ошибок при которых нужно выполнить задачу повторно:
 @celery_app.task(autoretry_for=(GenerateReportError, SaveReportError, ), default_retry_delay=30,  max_retries=5)
 def generate_report():
    ...
------------------------------------------------------------------------------------------------------------------------

 Чтобы получать задачи от вашей программы и отправлять результаты в серверную часть, Celery требуется брокер сообщений
 для связи. Redis и RabbitMQ — это два брокера сообщений, которые разработчики часто используют вместе с Celery.

 Брокер сообщений - это архитектурный паттерн в распределённых системах, где элементы системы общаются через посредника
 Брокер упрощает работу веб-сервисов, отвечая за пересылку сообщений и все связанные задачи.

 В работе брокера сообщений участвуют два ключевых элемента: producer (создатель сообщений) и consumer (получатель/подписчик).
 Один элемент создает сообщения и отправляет их другому элементу-получателю. В процессе отправки брокер обеспечивает
 промежуточный этап, сохраняя сообщения от продюсера в определенной папке файловой системы.

 Для чего нужны брокеры сообщений?
 1) Гарантии доставки сообщений.
 2) Повышение производительности.
 3) Отказоустойчивость и масштабируемость.
 4) Разделение слоев.

 ИЗ ЧЕГО СОСТОИТ БРОКЕР СООБЩЕНИЙ:
 В работе любого брокера сообщений используются две основные сущности:
 Producer / Publisher — занимается отправкой сообщения в брокер;
 Consumer / Subscriber — получает и обрабатывает сообщения из брокера;

 Есть два основных алгоритма передачи сообщений в очередь:
 1) Есть Producer, который направляет сообщения в брокер, и есть Consumer, который их получает.
 2) Есть Publisher, который закидывает сообщения в очередь, и есть n-ое количество Subscriber'ов, которые их обрабатывают в дальнейшем.

 Паттерны обмена информации:
 --- 1) Request-Response (Запрос-Ответ);
 --- 2) One-Way (Односторонний) или Fire and Forget (Отправил и забыл);
 --- 3) Publish-Subscribe (Публикация-Подписка) или сокращённо Pub-Sub;
 --- 4) Point-to-Point (Точка-Точка).

 1) В интернете Request-Response — это работа HTTP: клиент выполняет запрос на сервер, ждёт и получает ответ.
 2) One-Way, когда приложение по сети отправляет UDP (User Datagram Protocol) пакет на сервер без ожидания ответа
 3), 4) Publish-Subscribe, Point-to-Point - связаны с брокерами сообщений,
 В паттернах Pub-Sub и Point-to-Point происходит асинхронное общение через посредника.

 Брокер сообщений — это программная система полностью или частично реализующая паттерны Pub-Sub и Point-to-Point.
 Взаимодействие программ через брокер упрощает процесс разработки.Нет необходимости в каждом сервисе реализовывать
 механизмы доставки, маршрутизации, хранения сообщений — всем этим занимается «посредник». Общение через «посредника»
 помогает навести порядок и внести ясность в потоки данных, а значит, упростить разработку и снизить вероятность появление ошибок.

 -- At most once (Не более одного раза):
 Самый простой вариант — отправка в стиле Fire and Forget (Отправил и забыл).
 Большая часть сообщений доходит до получателя, но часть теряется из-за сбоев.

 -- At least once (Хотя бы один раз):
 Чтобы все данные достигли цели, могут предприниматься повторные отправки. Хотя бы одна попытка будет успешной.
 В таком случае сообщения не теряются, но могут дублироваться.

 Обычно реализуется через механизм подтверждений (ACK, acknowledgment). Сообщение повторяется, если не получено
 подтверждение о доставке. Возможны дубли, если подтверждение потерялось или не было отправлено из-за сбоя.

 -- Exactly once (Строго один раз):
 Самый труднодостижимый вариант — максимальная гарантия доставки. Сообщения никогда не теряются и не дублируются,
 каждое доставляется ровно один раз.

 Очередь и Топик:
 Брокер, реализующий шаблон Point-to-Point, ассоциируется с термином Queue (Очередь). Сообщения отправителя попадают в
 очередь, получатель извлекает сообщения из очереди. После извлечения сообщение становится больше никому не доступными.
 Данные в очереди хранятся, пока они не будут прочитаны или не истечёт срок их действия.

 В Pub-Sub ассоциируется с темой, топиком (Topic). Сообщения попадают в топик. Система распределяет каждое сообщение
 между всеми подписчиками топика (Broadcast, вещание). Сообщения могут храниться в топике, до тех пор, пока это
 необходимо для распространения данных между всеми подписчиками.


 Популярные Брокеры Сообщений:
 --- Apache Kafka: Очень быстрый, позволяет обрабатывать более 1 млн сообщений в секунду
 Kafka используется для обработки больших объёмов данных, сотен тысяч сообщений в секунду, которые подолгу хранятся
 на диске и много раз читаются сотнями или даже тысячами подписчиков. Kafka — это легко масштабируемая система,
 обладающая повышенной отказоустойчивостью, что очень важно в крупных проектах.

 Для Kafka принцип «Тупой брокер, умный потребитель» означает, что, в отличие от RabbitMQ, он не занимается контролем и
 распределением сообщений. Потребители сами опрашивают брокер и решают, какие сообщения им читать, брокер только хранит данные.

 --- RabbitMQ: Около 50 тысяч сообщений в секунду (зависит от конфигурации)
 RabbitMQ более простой в установке и настройке, успешно справляется с асинхронным обменом данными в микросервисной
 архитектуре. Не требует дополнительных компонентов и затрат на дисковые ресурсы, так как все сообщения после чтения
 из очереди удаляются. По сравнению с Kafka обладает большими возможностями по настройке шаблонов обмена сообщениями.
 Отличный выбор, если нет завышенных требований к отказоустойчивости и пропускной способности.

 Принцип «Умный брокер, тупой потребитель» по отношению к RabbitMQ означает, что брокер берёт на себя много
 дополнительных действий. Например, следит за прочитанными сообщениями и удаляет их из очереди. Или сам организует
 процесс распределения сообщений между подписчиками

 --- Redis: До 1 млн сообщений в секунду

 Выбор брокера:
 Celery требует решения для отправки и получения сообщений; обычно это происходит в виде отдельной службы,
 называемой message broker.

 RabbitMQ:
 обладает полным набором функций, стабильностью, долговечностью и простотой установки.
 Это отличный выбор для производственной среды

 RabbitMQ - это брокер.

 Как брокер: RabbitMQ обрабатывает большие сообщения лучше, чем Redis, однако если много сообщений поступает очень быстро,
 масштабирование может стать проблемой, и следует рассмотреть Redis или SQS, если только RabbitMQ не работает в очень больших масштабах.

 Redis:
 также обладает полным набором функций, но более подвержен потере данных в случае резкого завершения работы или сбоев питания
 Redis может быть как бэкендом, так и брокером.

 Как брокер: Redis хорошо работает для быстрой передачи небольших сообщений. Большие сообщения могут перегрузить систему.

 --- Особенности Apache Kafka ---
 Один из самых популярных брокеров, который достаточно активно используется и имеет очень много возможностей.

 Подписчики должны сами «забирать» сообщения;
 Постоянное хранение данных. Все сообщения хранятся ограниченное количество времени, которое конфигурируется на уровне брокера.
 Позволяет перечитывать сообщения.
 Гарантирует порядок сообщений в разрезе топика.В каком порядке publisher прислал сообщения, в таком порядке subscriber их и получит.

 --- Особенности Rabbit MQ ---
 Тоже один из популярных брокеров. Он менее производительный, по сравнению с Kafka, но у него есть свои плюсы.

 Гибкая маршрутизация. Здесь мы можем выстраивать такие системы, которые требуют передачи данных в множество частей
 или микросервисов. За счет него можно облегчить эту задачу путем использования всех возможностей.
 Удаляет сообщение после доставки его получателю.
 Есть сложности при горизонтальном масштабировании в кластере.

  --- Особенности Redis ---
 Резервное копирование на определенный момент времени;

 Имеет ограниченный функционал по сравнению с другими брокерами.

 Apache Kafka:
 - когда нужно обработать большой объем данных, которые очень быстро генерируются   нет большого потока данных
 - при реализации транзакционных или конвейерных систем
 - при построении событийно-ориентированной архитектуры
 - идеально подходит в тех случаях, где требуется персистентность.

 RabbitMQ:
 - когда нужно обработать большой объем данных, которые очень быстро генерируются	нет большого потока данных
 - важна гибкость маршрутизации сообщений внутри системы
 - важен факт доставки сообщений

 Redis:
 - необходима обработка больших объемов данных
 - не требуется персистентность
 - необходима высокая скорость доставки сообщений

 Персистентность в программировании означает способность состояния существовать дольше, чем процесс, создавший его.
 персистентность - возможность долговременного хранения состояния
 Персистентные структуры данных (англ. persistent data structures) — это структуры данных, которые при внесении в них
 изменений сохраняют доступ ко всем своим предыдущим состояниям.

 Уровни персистентности:
 - Частичная — к каждой версии можно делать запросы, но изменять можно только последнюю.
 - Полная — можно делать запросы к любой версии и менять любую версию.
 - Конфлюэнтная — помимо этого можно объединять две структуры данных в одну (например, сливать вместе кучи или деревья поиска).
 - Функциональная — структуру можно реализовать на чистом функциональном языке: для любой переменной значение может
   быть присвоено только один раз и изменять значения переменных нельзя.


 SQLAlchemy:
 SQLAlchemy является бэкендом.

 Он позволяет Celery взаимодействовать с MySQL, PostgreSQL, SQlite и другими. Это ORM, и это способ, с помощью которого
 Celery может использовать SQL DB в качестве бэкенда результатов.Исторически SQLAlchemy не является самым стабильным
 бэкендом результатов, поэтому при его выборе следует проявлять осторожность.

 Установка Celery:
 pip install celery

"""









