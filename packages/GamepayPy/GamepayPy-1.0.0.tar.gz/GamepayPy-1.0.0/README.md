# GamepayPy — удобный способ для работы с GamePay API

![logo](https://i.imgur.com/vC01Lug.png)

**GamepayPy** упрощает взаимодействие с GamePay API (gamepay.best)

# Инструкция:
Установка модуля **GamepayPy** с **pypi.org**:
> pip3 install GamepayPy

# Использования модуля:
Импортирование модуля **GamepayPy**:
```python
from GamepayPy import *
```
Подключение вашего API-токена:
```python
test = GamepayPy(token="ВАШ_ТОКЕН")
```
Доступные методы:
```python
# Создание ссылки для оплаты:
test.createOrder(unique_id, amount, shop_id, description)
>> https://gamepay.best/pay/xxxx-xxxx-xxxx-xxxx

# Проверка статуса заказа:
test.checkStatus(order_id)
>> 0 (другое значение, в случае успеха)

# Получение баланса аккаунта:
test.checkBalance()
>> 0.0
```
Список параметров:

> **token** (str) - Ваш токен от аккаунта.
>
> **unique_id** (int) - Уникальный ID заказа в вашей системе.
>
> **amount** (int) - Сумма пополнения (в рублях).
>
> **shop_id** (int) - ID вашего магазина.
>
> **description** (str) - описание к пополнению/заказу.
>
> **order_id** (int) - ID заказа.

#### Официальная документация API GamePay.best: https://gamepay.best/doc