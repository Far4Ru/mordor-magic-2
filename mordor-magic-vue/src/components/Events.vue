<template>
  <section>
    <v-row>
      <v-col cols="6" class="mx-auto">
        <h2>События</h2>
        <v-expansion-panels>
          <v-expansion-panel>
            <v-expansion-panel-header>
              Ежедневные
            </v-expansion-panel-header>
            <v-expansion-panel-content
              v-for="(event, i) in events.filter(e => e.period == 'd')"
              :key="i"
            >
              <v-checkbox
                v-model="event.visible"
                :label="`${event.name}`"
              ></v-checkbox>
            </v-expansion-panel-content>
          </v-expansion-panel>
          <v-expansion-panel>
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
    events: [
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
    ],
    checkbox: true
  }),
  methods: {
    async getEvents () {
      try {
        this.axios
          .get(server + 'events/')
          .then(response => {
            // events = response.data
            this.events = response.data
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  created () {
    this.getEvents()
  }
}
</script>

<style>
</style>
