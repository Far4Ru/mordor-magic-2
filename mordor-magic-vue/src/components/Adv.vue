<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        Объявления
        <v-sheet rounded="lg">
          <v-list color="transparent">
            <v-list-item
              v-for="advItem in advList"
              :key = advItem
            >
              <v-list-item-content>
                <v-list-item-title>
                  {{ advItem.title }}
                </v-list-item-title>
                <v-list-item-subtitle>
                {{ advItem.text }}
                </v-list-item-subtitle>
                <v-list-item-subtitle>
                {{ advItem.date }}
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-sheet>
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
    advList: {
      1: {
        title: 'a name',
        text: 'a text',
        date: '12'
      },
      2: {
        title: 'b name',
        text: 'b text',
        date: '13'
      }
    }
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
    this.getUsers()
  }
}
</script>

<style>
</style>
