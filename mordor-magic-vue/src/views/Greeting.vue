<template>
  <section>
    <login @changeLoginPage="changeLoginPage" v-show="isLoginPage" />
    <registration @changeLoginPage="changeLoginPage" v-show="!isLoginPage" />
  </section>
</template>

<script>
import Login from '@/components/Login'
import Registration from '@/components/Registration'

export default {
  name: 'Greeting',
  components: {
    Login,
    Registration
  },
  data: () => ({
    isLoginPage: true,
    username: '',
    savedUsername: ''
  }),
  props: [],
  methods: {
    submitUsername () {
      localStorage.setItem('username', this.username)
      this.savedUsername = this.username
      this.$refs.form.reset()
    },
    changeLoginPage (isLogin) {
      this.isLoginPage = isLogin
    }
  },
  created () {
    if (localStorage.getItem('username')) {
      this.savedUsername = localStorage.getItem('username')
      this.username = this.savedUsername
    }
  },
  mounted () {
  }
}
</script>

<style>
  .greeting-list-wrapper {
    display: flex;
  }
  .greeting-list-wrapper .greeting-list {
    margin: auto
  }
</style>
