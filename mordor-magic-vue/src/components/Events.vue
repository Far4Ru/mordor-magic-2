<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        <h2>События</h2>
        <v-timeline>
            <v-timeline-item
              v-for="(year, i) in years"
              :key="i"
              :color="year.color"
              small
            >
              <template v-slot:opposite>
                <span
                  :class="`headline font-weight-bold ${year.color}--text`"
                  v-text="year.year"
                ></span>
              </template>
              <div class="py-4">
                <h2 :class="`headline font-weight-light mb-4 ${year.color}--text`">
                  Lorem ipsum
                </h2>
                <div>
                  Lorem ipsum dolor sit amet, no nam oblique veritus. Commune scaevola imperdiet nec ut, sed euismod convenire principes at. Est et nobis iisque percipit, an vim zril disputando voluptatibus, vix an salutandi sententiae.
                </div>
              </div>
            </v-timeline-item>
          </v-timeline>
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
    years: [
      {
        color: 'cyan',
        year: '12:00'
      },
      {
        color: 'green',
        year: '15:00'
      },
      {
        color: 'pink',
        year: '19:30'
      },
      {
        color: 'amber',
        year: '20:00'
      },
      {
        color: 'orange',
        year: '21:00'
      }
    ]
  }),
  methods: {
    async getEvents () {
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
