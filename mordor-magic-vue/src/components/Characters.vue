<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        Персонажи
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
    info: ''
  }),
  methods: {
    async getUsers () {
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
    }
  },
  created () {
  }
}
</script>

<style>
</style>
