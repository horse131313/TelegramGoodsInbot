# TelegramGoodsInbot
**The store in Telegram** |
**Магазин в Телеграм**

Торговый модуль поддерживает три режима работы:
- digital - торговля цифровыми товарами и услугами.
- real - торговля материальными товарами и услугами.
- hybrid - торговля цифровыми и материальными товарами и услугами.


**Модуль афишы**
- каталог событий, мест и творческих коллективов.
- рекомендации для подписчиков конкретного города по событиям их локации.


**Функции всей площадки**
- рассылки мультимедиа, в том числе запланированные.
- карточка продавца.
- карточка магазина.
- индивидуальные реквизиты продавцов.
- безопасная сделка и корзина.
- справочник городов - 192 города России.


**Функции для пользователя магазина**
- каталог двух уровней, категория - товар.
- корзина.
- поддержка (контакты) - ссылка в диалог с администратором.
- FAQ - сообщение для пользователей с HTML разметкой.
- подробная Статистика бота: кол-во пополнений, покупок, пользователей, позиций, категорий, чистой прибыли.
- определение местонахождения пользователя.


**Функции для пользователя афишы**
- каталог четырех срезов, город - место - артист - событие


**Функции продавца**
- управление товарами
- добавление собственных реквизитов QIWI, YooMoney


**Функции администратора афишы**
- управление артистами, местами, событиями.


**Функции администратора места**
- управление местом, событиями.


**Функции администратора**
- режим технических работ
- проверка наличия обнолвения при запуске
- активация/деактивация функций продажи и оплаты
- добавление неограниченного количества глобальных администраторов
- согласование запросов на роль администратора магазина, управляющего своими товарами в каталоге
- добавление неограниченного количества администраторов магазинов
- удобная и многофункциональная админ панель
- определение и хранение города нахождения товара
- поиск покупателей и просмотр профилей
- поиск чеков покупок
- рассылка сообщений всем пользователям бота
- изменение и пополнение баланса пользователя
- отчет о продажах продавцов
- уведомления о событиях (создании товаров продавцами, продажах пользователям)


**Оплата товаров**
- используется библиотеки QIWI и YooMoney
- настраивается администратором бота через админку
- проверка работоспособности из админки
- вывод баланса кошелька QIWI
- индивидуальные реквизиты у каждого продавца


**Каталог и товары**
- User-friendly каталог
- товары имеют одно изображение
- гибкое управление товарами администраторами
- выгрузка всех товаров


**Защита**
- админ-фильтры на все хендлеры, гарантирующие приватность админ функционала
- защита от оплаты в тенге при пополнении баланса
- защита от неправильного HTML синтаксиса
- защита от повторной выдачи баланса
- защита от спама в боте (Middlewares)


**Настройки settings.ini**
- установить токен Бота, полученный у @BotFather
- установить Telegram ID администратора площадки(admin_id)


**Настройка**
1. Скопируйте папку бота. Перейдите в папку бота.
2. Выполните в командной строке "pip install -r requirements.txt".
3. Заполните файл settings.ini.
4. Стартовать бот. 
5. Заполнить информационные поля. 
6. Наполнить каталог товарами, реквизиты для получения оплаты за товары.
7. Наполнить каталог афишы.
8. Привлекать пользователей в каталог.


**Процесс администрирования площадки**
1. Согласование продавцов
2. Администрирование каталога
3. Администрирование денежных средств
4. Поддержка и ведение сделок, разрешение споров


**Процесс покупки для покупателя**
1. Выбор товара. 
2. Пополнение счета.
3. Оформление заказа(переписка с продавцом, ввод данных достаки). 
4. Получение товара. 
5. Подтверждение получения.
6. Отправка отзыва о покупателей.


**Процесс продажи для продавца**
1. Получение сообщения о заказе. 
2. Звонок покупателю. 
3. Отправка товара покупателю.
4. Получение отзыва о покупателей.


**PRO версия:**
- функция по запросу


**TODO:**
- вывод средств продавцами.
- рекомендательная система каталогов.


По вопросам пишите пожалуйста в Телеграм: @raclear.
Скриншоты экранов и описание меню: 
https://github.com/rashidovich2/TelegramGoodsInbot/wiki


Группа: https://t.me/shoptelegramg
Канал: https://t.me/godsinbot_releases


Чтобы торговать своими товарами в текущем экземпляре,
отправьте запрос на продавца из бота, нажав "Я продавец".
Работающий экземпляр системы: https://t.me/Goodsinbot.



**Развертывание своего экземпляра:**

Придумайте наименование для Вашего бота: 
Имя.
И «имя пользователя» ИмяBot.

Распределите товары по категориям или группам по какому-либо признаку:
Предметы интерьера
Китайский чай

Подготовьте данные Ваших товаров в формате:

Наименование
Описание
Цена
Количество в остатке
Фото

Зарегистрируйте бота в Телеграм:
- Найдите в Телеграм бота: @Botfather.
- Зайдите и создайте нового бота.
- Заполните данные бота.
- Скопируйте в безопасное место токен.

Зайдите в своего бота.
Заполните данные каталога.
Введите платежные реквизиты QIWI, YooMoney.
Можете начать торговать.
