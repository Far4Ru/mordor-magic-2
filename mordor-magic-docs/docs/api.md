# API


## Пользователи

**Default URL:** `/users/`

|  Method | Request  | Response | 
|---|---|---|
|  `POST` | `uid`  |  `404` |

## Персонажи

Method | Request | Response
--- | --- | ---
GET |  | asd<BR>sda<BR> * fgf<BR> * dfsdf

Список пользователей
/users/
get
id, nickname, role, user_online_date

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
