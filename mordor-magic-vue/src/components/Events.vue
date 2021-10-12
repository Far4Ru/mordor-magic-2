<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        <h2>События</h2>
        <v-expansion-panels>
          <v-expansion-panel
            v-show="events.filter(e => e.period == 'd').length"
          >
            <v-expansion-panel-header>
              Ежедневные
            </v-expansion-panel-header>
            <v-expansion-panel-content
              v-for="(event) in events.filter(e => e.period == 'd')"
              :key="event.start_time"
            >
              <v-checkbox
                v-model="event.visible"
                :label="`${event.name}`"
              ></v-checkbox>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel
            v-show="events.filter(e => e.period == 'w').length"
          >
            <v-expansion-panel-header>
              Еженедельные
            </v-expansion-panel-header>
            <v-expansion-panel-content
              v-for="(event, i) in events.filter(e => e.period == 'w')"
              :key="i"
            >
              <v-checkbox
                v-model="event.visible"
                :label="`${event.name}`"
              ></v-checkbox>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
        <v-timeline>
            <v-timeline-item
              v-for="(event, i) in events"
              :key="i"
              :color="event.color"
              small
              v-show="event.visible"
            >
              <template v-slot:opposite>
                <span
                  :class="`headline font-weight-bold ${event.color}--text`"
                  v-text="`${event.start_time} - ${event.end_time}`"
                  v-show="!isWholeDay(event.start_time)"
                ></span>
                <span
                  :class="`headline font-weight-bold ${event.color}--text`"
                  v-text="`Весь день`"
                  v-show="isWholeDay(event.start_time)"
                ></span>
              </template>
              <div class="py-4">
                <h2 :class="`headline font-weight-light mb-4 ${event.color}--text`">
                  {{ event.name }}
                </h2>
                <div>
                  {{ event.description }}
                </div>
              </div>
            </v-timeline-item>
          </v-timeline>
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
    info: '',
    events: [],
    checkbox: true
  }),
  computed: {
  },
  methods: {
    async getEvents () {
      try {
        var today = new Date()
        var date = `${today.getDate()}.${today.getMonth() + 1}.${today.getFullYear()} ${today.getHours()}:${today.getMinutes()}:${today.getSeconds()}`
        this.axios
          .get(server + 'events/', { params: { date: date } })
          .then(response => {
            this.events = response.data
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    isWholeDay (eventTime) {
      if (eventTime === '05:00:00') return true
      else return false
    }
  },
  created () {
    this.getEvents()
  }
}
</script>

<style>
</style>
