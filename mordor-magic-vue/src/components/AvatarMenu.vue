<template>
  <v-menu
    bottom
    min-width="200px"
    rounded
    offset-y
  >
    <template v-slot:activator="{ on }">
      <v-btn
        icon
        x-large
        v-on="on"
      >
        <v-avatar
          color="blue"
          size="42"
        >
          <span class="white--text text-h5">{{ changedInitials }}</span>
        </v-avatar>
      </v-btn>
    </template>
    <v-card>
      <v-list-item-content class="justify-center">
        <div class="mx-auto text-center">
          <v-container>
            <v-row>
              <v-col>
                <v-avatar
                  color="blue"
                >
                  <span class="white--text text-h5">{{ changedInitials }}</span>
                </v-avatar>
              </v-col>
              <v-col>
                <h4>{{ changedFullName }}</h4>
                <p class="text-caption mt-1">
                  {{ changedEmail }}
                </p>
              </v-col>
            </v-row>
          </v-container>
          <v-divider class="my-3"></v-divider>
          <v-btn
            block
            text
            @click="changePageToSettings"
          >
            Настройки
          </v-btn>
          <v-divider class="my-3"></v-divider>
          <v-btn
            block
            text
            v-on:click="logout"
          >
            Выйти
          </v-btn>
        </div>
      </v-list-item-content>
    </v-card>
  </v-menu>
</template>
<script>
import server from '@/server'
export default {
  name: 'AvatarMenu',
  data: () => ({
    initials: '',
    fullName: '',
    email: ''
  }),
  computed: {
    changedEmail: {
      get: function () {
        return this.email
      },
      set: function (email) {
        this.email = email
        return this.email
      }
    },
    changedFullName: {
      get: function () {
        return this.fullName
      },
      set: function (name) {
        this.fullName = name
        return this.fullName
      }
    },
    changedInitials: {
      get: function () {
        return this.fullName.charAt(0)
      }
    }
  },
  methods: {
    async getUserInfo () {
      this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
      this.axios
        .get(server + 'auth/users/me/')
        .then(response => {
          if (response.status === 200) {
            this.changedFullName = response.data.username
            this.changedEmail = response.data.email
          }
        })
        .catch(e => {
          console.error('AN API ERROR', e)
        })
    },
    async logout () {
      this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
      this.axios
        .post(server + 'auth/token/logout/')
        .then(response => {
          this.info = response
          if (response.status === 200 || response.status === 204) this.$router.push('/')
        })
        .catch(e => {
          console.error('AN API ERROR', e)
          // this.$router.push('/')
        })
    },
    changePageToSettings () {
      this.$emit('changePage', 'settings', false)
    }
  },
  created () {
    this.getUserInfo()
  }
}
</script>
