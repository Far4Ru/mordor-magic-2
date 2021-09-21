<template>
  <section>
    <h2>Это простой проект на Vue.</h2>
    <login />
    <registration />
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
    username: '',
    savedUsername: ''
  }),
  methods: {
    submitUsername () {
      // сохраним username в localStorage
      localStorage.setItem('username', this.username)
      // сохраним его в отдельную переменную,
      // для дальнейшей передачи в компоненту
      // GreetingCard
      this.savedUsername = this.username
      // очистим форму
      this.$refs.form.reset()
    }
  },
  created () {
    // если localStorage содержит значение по ключу
    // username, то запишем его в наши переменные
    if (localStorage.getItem('username')) {
      this.savedUsername = localStorage.getItem('username')
      this.username = this.savedUsername
    }
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
