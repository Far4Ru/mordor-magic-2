# API

## Пользователи

Конечная точка для получения списка всех пользователей.

**URL-адрес:** `/api/users/`

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK` <ul><li>`last_login`, `nickname`, `role`, `first_name`, `registration_status`, `user_online_date`, `last_name`, `email`</li></ul>|

## Создание пользователя

**URL-адрес:** `/auth/users/`

Метод | Запрос  | Ответ
---|---|---
`POST` | <ul><li>`'Content-Type': 'multipart/form-data'`</li><li>`username`, `email`,`password`</li></ul> | `HTTP_201_CREATED`


> Username<BR>
    150 characters or fewer. Letters, digits and @/./+/-/_ only.
    
> Password<BR>
    Your password can’t be too similar to your other personal information.
    Your password must contain at least 8 characters.
    Your password can’t be a commonly used password.
    Your password can’t be entirely numeric.

## Вход пользователя

**URL-адрес:** `/auth/token/login/`

Метод | Запрос  | Ответ
---|---|---
`POST` | <ul><li>`'Content-Type': 'multipart/form-data'`</li><li>`username`, `password`</li></ul> | <ul><li>`HTTP_200_OK`, `auth_token`</li></ul>

## Проверка пользователя

**URL-адрес:** `/auth/users/me/`

Метод | Запрос  | Ответ
---|---|---
`GET` | `Authorization` | `200`

> Authorization<BR>
     `Token <auth_token>`

## Изменить пароль
**URL-адрес:** `/auth/users/set_password/`

Метод | Запрос  | Ответ
---|---|---
`POST` | <ul><li>`Authorization`</li><li>`'Content-Type': 'multipart/form-data'`</li><li>`current_password`, `new_password`</li></ul> | `HTTP_204_NO_CONTENT`

## Данные пользователя

**URL-адрес:** `/api/user/`

Метод | Запрос  | Ответ
---|---|---
`GET` | `username` | `HTTP_200_OK` <ul><li>`last_login`, `nickname`, `role`, `first_name`, `registration_status`, `user_online_date`, `last_name`, `email`</li></ul>
`GET` | `Authorization` | `HTTP_200_OK`<ul><li>`last_login`, `nickname`, `role`, `first_name`, `registration_status`, `user_online_date`, `last_name`, `email`</li></ul>
`PATCH` | <ul><li>`Authorization`</li><li>`'Content-Type': 'multipart/form-data'`</li><li>`first_name`, `last_name`, `nickname`</li></ul> | `HTTP_201_CREATED`, `HTTP_204_NO_CONTENT`

## Выход

**URL-адрес:** `/auth/token/logout/`

Метод | Запрос  | Ответ
---|---|---
`POST` | `Authorization` | <ul><li>`HTTP_200_OK`</li><li>`HTTP_204_NO_CONTENT`</li></ul>

## Персонажи

Конечная точка для получения списка всех персонажей.

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK` <ul><li>`type`, `nickname`</li></ul>|

## События

Конечная точка для получения событий.

**URL-адрес:** `/api/events/`

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK`<ul><li>`name`,`description`,`period`,`period_parity`,`period_across`,`start_date`,`start_time`,`end_time`,`max_value`,`color`</li></ul>|
|  `GET` |  `date`:`%d.%m.%Y %H:%M:%S` |  `HTTP_200_OK`<ul><li>`name`,`description`,`period`,`period_parity`,`period_across`,`start_date`,`start_time`,`end_time`,`max_value`,`color`</li></ul>|


## Персонажи и пользователи

Конечная точка для получения пользователей с персонажами.

**URL-адрес:** `/api/character_owners/`

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK`<ul><li>`nickname`</li>`type`, `nickname`<li>`character_user`</li>`last_login`, `nickname`, `role`, `first_name`, `registration_status`, `user_online_date`</ul>|

## Персонажи и события

Конечная точка для получения персонажей с событиями.

**URL-адрес:** `/api/character_events/`

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK`<ul><li>`character`</li>`type`, `nickname`<li>`event`</li>`name`, `description`, `period`, `start_date`, `start_time`, `end_time`, `max_value`, `color`<li>`status`</li><li>`date`</li><li>`value`</li></ul>|