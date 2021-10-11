# API

## Пользователи

Конечная точка для получения списка всех пользователей.

**URL-адрес:** `/api/users/`

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK` <ul><li>`id`, `nickname`, `role`, `user_online_date`</li></ul>|

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

## Изменить данные пользователя

**URL-адрес:** `/api/user/`

Метод | Запрос  | Ответ
---|---|---
`PATCH` | <ul><li>`Authorization`</li><li>`'Content-Type': 'multipart/form-data'`</li><li>`first_name`, `last_name`, `nickname`</li></ul> | `HTTP_204_NO_CONTENT`

## Выход

**URL-адрес:** `/auth/token/logout/`

Метод | Запрос  | Ответ
---|---|---
`POST` | `Authorization` | <ul><li>`HTTP_200_OK`</li><li>`HTTP_204_NO_CONTENT`</li></ul>

## Персонажи

Конечная точка для получения списка всех персонажей пользователя.

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK` <ul><li>`id`</li></ul>|

## События

Конечная точка для получения событий.

**URL-адрес:** `/api/events/`

|  Метод | Запрос  | Ответ | 
|---|---|---|
|  `GET` |   |  `HTTP_200_OK`<ul><li>`name`,`description`,`start_time`,`end_time`</li></ul>|

## Прогресс

<table>
    <thead>
        <tr>
            <th>План</th>
            <th>Реализация</th>
            <th>URL-адрес</th>
        </tr>
    </thead>
    <tbody align="center">
        <tr>
            <td colspan=3><b>READ</b></td>
        </tr>
        <tr>
          <td>User
          </td>
          <td>
            Пользователи
          </td>
          <td>
            /api/users/
          </td>
        </tr>
        <tr>
          <td>
              CharacterOwner
          </td>
          <td>
            -
          </td>
          <td>
            /api/character_owners/
          </td>
        </tr>
        <tr>
          <td>
             Character
          </td>
          <td>
            -<br>Персонажи
          </td>
          <td>
            /api/characters/
          </td>
        </tr>
        <tr>
          <td>
             CharacterEvent
          </td>
          <td>
            -
          </td>
          <td>
            /api/character_events/
          </td>
        </tr>
        <tr>
          <td>
             Event
          </td>
          <td>
            События
          </td>
          <td>
            /api/events/
          </td>
        </tr>
        <tr>
          <td colspan="3">
             <b>RELATED<b>
          </td>
        </tr>
        <tr>
          <td>
             Character + {User}
          </td>
          <td>
            -
          </td>
          <td>
            /api/character/users/
          </td>
        </tr>
        <tr>
          <td>
             User + {Character}
          </td>
          <td>
            -
          </td>
          <td>
            /api/user/characters/
          </td>
        </tr>
        <tr>
          <td>
             Character + {Event}
          </td>
          <td>
            -
          </td>
          <td>
            /api/character/events/
          </td>
        </tr>
        <tr>
          <td>
             Event + {Character}
          </td>
          <td>
            -
          </td>
          <td>
            /api/event/characters/
          </td>
        </tr>
        <tr>
          <td colspan="3">
             <b>CREATE<b>
          </td>
        </tr>
        <tr>
          <td>
             CREATE User
          </td>
          <td>
            Создание пользователя
          </td>
          <td>
            /auth/users/
          </td>
        </tr>
        <tr>
          <td>
             CREATE Character
          </td>
          <td>
            -
          </td>
          <td>
            /api/character/create/
          </td>
        </tr>
        <tr>
          <td>
             CREATE Event
          </td>
          <td>
            -
          </td>
          <td>
            /api/event/create/
          </td>
        </tr>
        <tr>
          <td colspan="3">
             <b>UPDATE<b>
          </td>
        </tr>
        <tr>
          <td>
             UPDATE User
          </td>
          <td>
            -<br>Изменить данные пользователя
          </td>
          <td>
            /user/update/
          </td>
        </tr>
        <tr>
          <td>
             UPDATE User Password
          </td>
          <td>
            Изменить пароль
          </td>
          <td>
            /auth/users/set_password/
          </td>
        </tr>
        <tr>
          <td>
             UPDATE Character
          </td>
          <td>
            -
          </td>
          <td>
            /api/character/update/
          </td>
        </tr>
        <tr>
          <td>
             UPDATE Event
          </td>
          <td>
            -
          </td>
          <td>
            /api/event/update/
          </td>
        </tr>
        <tr>
          <td colspan="3">
             <b>DELETE<b>
          </td>
        </tr>
        <tr>
          <td>
             DELETE User
          </td>
          <td>
            -
          </td>
          <td>
            /api/user/delete/
          </td>
        </tr>
        <tr>
          <td>
             DELETE Character
          </td>
          <td>
            -
          </td>
          <td>
            /api/character/delete/
          </td>
        </tr>
        <tr>
          <td>
             DELETE Event
          </td>
          <td>
            -
          </td>
          <td>
            /api/event/delete/
          </td>
        </tr>
        <tr>
          <td colspan="3">
             <b>TOKEN</b>
          </td>
        </tr>
        <tr>
          <td>
             Login
          </td>
          <td>
            Вход пользователя
          </td>
          <td>
            /auth/token/login/
          </td>
        </tr>
        <tr>
          <td>
             Logout
          </td>
          <td>
            Выход
          </td>
          <td>
            /auth/token/logout/
          </td>
        </tr>
        <tr>
          <td>
             Check
          </td>
          <td>
            Проверка пользователя
          </td>
          <td>
            /auth/users/me/
          </td>
        </tr>
    </tbody>
</table>