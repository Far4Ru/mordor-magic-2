<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        Профиль
        {{ changedFirstName }}
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
    username: '',
    firstName: ''
  }),
  computed: {
    changedFirstName: {
      get: function () {
        return this.firstName
      },
      set: function (name) {
        this.firstName = name
        return this.firstName
      }
    }
  },
  methods: {
    async getInfo () {
      try {
        this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
        this.axios
          .get(apiUrl + 'users/user', { params: { username: this.username } })
          .then(response => {
            if (response.status === 200) {
              this.changedFirstName = response.data[0].first_name
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
