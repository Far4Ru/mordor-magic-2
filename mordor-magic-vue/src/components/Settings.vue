<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        <h2>Настройки</h2>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Сменить пароль
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-text-field
                v-model="oldPassword"
                :type="'password'"
                label="Старый пароль"
              ></v-text-field>
              <v-text-field
                v-model="newPassword"
                :type="'password'"
                hint="От 8 символов"
                label="Новый пароль"
              ></v-text-field>
              <v-btn
                class="mr-4"
                @click="changePassword"
              >
                Сменить
              </v-btn>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Изменить данные
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-text-field
                v-model="first_name"
                label="Имя"
              ></v-text-field>

              <v-text-field
                v-model="last_name"
                label="Фамилия"
              ></v-text-field>

              <v-text-field
                v-model="nickname"
                label="Никнейм"
              ></v-text-field>
              <v-btn
                class="mr-4"
                @click="changeUserData"
              >
                Изменить
              </v-btn>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </section>
</template>

<script>
const apiUrl = 'http://127.0.0.1:8000/api/'

export default {
  components: { },
  name: 'Members',
  data: () => ({
    info: '',
    oldPassword: '',
    newPassword: '',
    first_name: '',
    last_name: '',
    nickname: '',
    username: '',
    id: -1
  }),
  methods: {
    async getUser () {
      try {
        this.axios
          .get(apiUrl + 'users/')
          .then(response => {
            this.info = response
            console.log(this.info)
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async changePassword () {
      try {
        this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
        const data = new FormData()
        data.set('current_password', this.oldPassword)
        data.set('new_password', this.newPassword)
        const config = {
          header: {
            'Content-Type': 'multipart/form-data'
          }
        }
        this.axios
          .post(apiUrl + 'auth/users/set_password/', data, config)
          .then(response => {
            if (response.status === 204) {
              this.oldPassword = ''
              this.newPassword = ''
              // success
            }
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async changeUserData () {
      try {
        this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
        const data = new FormData()
        data.set('first_name', this.first_name)
        data.set('last_name', this.last_name)
        data.set('nickname', this.nickname)
        const config = {
          header: {
            'Content-Type': 'multipart/form-data'
          }
        }
        this.axios
          .patch(apiUrl + 'user/', data, config)
          .then(response => {
            if (response.status === 204) {
              // success
            }
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async getUserData () {
      try {
        this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
        this.axios
          .get(apiUrl + 'user/', { params: { username: this.username } })
          .then(response => {
            if (response.status === 200) {
              this.first_name = response.data[0].first_name
              this.last_name = response.data[0].last_name
              this.nickname = response.data[0].nickname
              this.id = response.data[0].id
            }
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  created () {
    if (localStorage.getItem('username')) {
      this.username = localStorage.getItem('username')
    }
    this.getUserData()
  }
}
</script>

<style>
</style>
