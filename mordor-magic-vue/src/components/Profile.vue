<template>
  <section>
    <v-row>
      <v-col cols="7" class="mx-auto">
        <h2>Профиль</h2>
        <v-card
            class="mx-auto"
            tile
            align="left"
        >
          <v-list-item>
            <v-list-item-content>
              <v-list-item-subtitle>Никнейм</v-list-item-subtitle>
              <v-list-item-title>
                {{ userData.nickname }}
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-content>
              <v-list-item-subtitle>Имя</v-list-item-subtitle>
              <v-list-item-title>
                {{ userData.first_name }}
              </v-list-item-title>
            </v-list-item-content>
            <v-list-item-content>
              <v-list-item-subtitle>Фамилия</v-list-item-subtitle>
              <v-list-item-title>
                {{ userData.last_name }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-subtitle>Роль</v-list-item-subtitle>
              <v-list-item-title>
                {{ userData.role }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-subtitle>Эл. почта</v-list-item-subtitle>
              <v-list-item-title>
                {{ userData.email }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-subtitle>Гильдия</v-list-item-subtitle>
              <v-list-item-title>
                MORDOR
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-card-text
            align='center'
          >
            <p>Мордор - великий и вечный</p>
            <div align='right'>
              <a href='https://discord.gg/kRfyMp8' target='_blank'>Дискорд</a>
            </div>
            <div align='right'>
              <a href='https://eternalmagic.ru/' target='_blank'>Сайт игры</a>
            </div>
          </v-card-text>

        </v-card>
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
    username: '',
    userData: []
  }),
  computed: {
  },
  methods: {
    async getInfo () {
      try {
        this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
        this.axios
          .get(server + 'user/')
          .then(response => {
            if (response.status === 200) {
              this.userData = response.data[0]
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
    this.getInfo()
  }
}
</script>

<style>
</style>
