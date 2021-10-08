# API

## Пользователи

Конечная точка для получения списка всех пользователей.

**URL-адрес:** `/api/users/`

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK` <ul><li>`{{ User.id }}`</li><li>`{{ User.nickname }}`</li><li>`{{ User.role }}`</li><li>`{{ User.user_online_date }}`</li></ul>|

## Персонажи

Конечная точка для получения списка всех персонажей пользователя.

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK` <ul><li>`{{ User.id }}`</li></ul>|

## События по дате

Конечная точка для получения событий по заданной дате.

**URL-адрес:** `/api/events/`

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` | `date`  |  `HTTP_200_OK`<ul><li>`{{ Event.name }}`</li><li>`{{ Event.description }}`</li><li>`{{ Event.start_time }}`</li><li>`{{ Event.end_time }}`</li></ul>|

## Остальное

Удалить пользователя
@admin
/user/delete/<id>

Информация о пользователе
/user/<id>
get
nickname, role,user_online_date,first_name
characters:
  character
sum reputation today

Профиль пользователя
/user/
get
?nickname=
nickname, role,user_online_date,first_name, last_name, email
characters:
  character
sum reputation today

Изменить поля у пользователя
/user/<id>
patch


Список персонажей

Создать персонажа

Удалить перонажа

Добавить персонажу событие

Изменить состояние события

Список событий на сегодня


Username
150 characters or fewer. Letters, digits and @/./+/-/_ only.

Password
Your password can’t be too similar to your other personal information.
Your password must contain at least 8 characters.
Your password can’t be a commonly used password.
Your password can’t be entirely numeric.