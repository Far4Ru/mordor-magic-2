<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        <h2>Участники</h2>
        <v-data-table
            :headers="headers"
            :items="changedUserList"
            class="elevation-1"
            @click:row="toUserInfo"
          >
            <template v-slot:header.name="{ header }">
              {{ header.text.toUpperCase() }}
            </template>
          </v-data-table>
          <v-dialog
            v-model="dialog"
            max-width="500px"
          >
            <v-card>
              <v-card-title>
                Участник
              </v-card-title>
              <v-card-text>
                <!-- <v-btn
                  color="primary"
                  dark
                  @click=""
                >
                  Открыть
                </v-btn> -->
                <div>
                  Фарару
                </div>
                <div>
                  Количество персонажей
                </div>
                <v-select
                  :items="roles"
                  label="Роль"
                  item-value="text"
                  v-show="admin"
                ></v-select>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  color="red"
                  text
                  @click="dialog = false"
                  v-show="admin"
                >
                  Исключить
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn
                  color="green"
                  text
                  @click="dialog = false"
                  v-show="admin"
                >
                  Сохранить
                </v-btn>
                <v-btn
                  color="primary"
                  text
                  @click="dialog = false"
                  v-show="!admin"
                >
                  ОК
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import server from '@/server'

export default {
  components: { },
  name: 'Members',
  data: () => ({
    info: '',
    dialog: false,
    admin: false,
    roles: [
      { text: 'Зам. главы' },
      { text: 'Офицер' },
      { text: 'Элита' },
      { text: 'Участник' }
    ],
    headers: [
      {
        text: 'Никнейм',
        align: 'start',
        value: 'nickname'
      },
      { text: 'Роль', value: 'role' },
      { text: 'Онлайн', value: 'last_login' }
    ],
    userList: []
  }),
  computed: {
    changedUserList: {
      get: function () {
        return this.userList
      },
      set: function (list) {
        this.userList = list
        list.forEach((elem) => {
          elem.last_login = this.dateISOtoPastTime(elem.last_login)
        })
        return this.userList
      }
    }
  },
  methods: {
    async getMembers () {
      try {
        this.axios
          .get(server + 'users/')
          .then(response => {
            this.changedUserList = response.data
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    toUserInfo (userData) {
      this.dialog = true
      console.log(userData.id)
    },
    async getInfo (id) {
      try {
        this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
        this.axios
          .get(server + 'users/user', { params: { id: id } })
          .then(response => {
            if (response.status === 200) {
              this.changedFirstName = response.data[0].first_name
            }
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    dateISOtoPastTime (datetime) {
      const date = new Date(datetime)
      const nowDate = new Date()
      if (date.getFullYear() >= nowDate.getFullYear()) {
        if (date.getMonth() >= nowDate.getMonth()) {
          if (date.getDate() >= nowDate.getDate()) {
            if (date.getHours() >= nowDate.getHours()) {
              if (date.getMinutes() >= nowDate.getMinutes()) {
                return 'Онлайн'
              } else {
                return (nowDate.getMinutes() - date.getMinutes()) + ' мин. назад'
              }
            } else {
              return (nowDate.getHours() - date.getHours()) + ' ч. назад'
            }
          } else {
            return date.getDate() + '.' + date.getMonth() + '.' + date.getFullYear()
          }
        } else {
          return date.getDate() + '.' + date.getMonth() + '.' + date.getFullYear()
        }
      } else {
        if (date.getFullYear() === 1970) return 'Не входил'
        return date.getDate() + '.' + date.getMonth() + '.' + date.getFullYear()
      }
    }
  },
  created () {
    this.getMembers()
  }
}
</script>

<style>
</style>
