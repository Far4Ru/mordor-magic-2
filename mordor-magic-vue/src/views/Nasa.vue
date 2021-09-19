<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        <epic-item-card
          v-for="epicItem in epicItems"
          :key="epicItem.identifier"
          :epic-item="epicItem"
          class="my-2"
        />
      </v-col>
    </v-row>
  </section>
</template>

<script>
import EpicItemCard from '@/components/EpicItemCard.vue'
const apiUrl = 'http://127.0.0.1:8000/api/'

export default {
  components: { EpicItemCard },
  name: 'Greeting',
  data: () => ({
    epicItems: [],
    info: ''
  }),
  methods: {
    async getEpicItems () {
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
    this.getEpicItems()
  }
}
</script>

<style>
</style>
