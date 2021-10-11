<template>
  <section>
    <v-row>
      <v-col cols="7" class="mx-auto">
        <h2>Персонажи</h2>
        <template>
          <v-data-table
            :headers="headers"
            :items="characterList"
            sort-by="calories"
            class="elevation-1"
          >
            <template v-slot:top>
              <v-toolbar
                flat
              >
                <v-spacer></v-spacer>
                <v-dialog
                  v-model="dialog"
                  max-width="500px"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="primary"
                      dark
                      class="mb-2"
                      v-bind="attrs"
                      v-on="on"
                    >
                      Добавить
                    </v-btn>
                  </template>
                  <v-card>
                    <v-card-title>
                      <span class="text-h5">{{ formTitle }}</span>
                    </v-card-title>

                    <v-card-text>
                      <v-container>
                        <v-text-field
                          v-model="editedItem.name"
                          label="Никнейм персонажа"
                        ></v-text-field>
                      </v-container>
                      <v-container>
                        <v-text-field
                          v-model="editedItem.email"
                          label="Эл. почта"
                        ></v-text-field>
                      </v-container>
                      <v-container>
                        <v-select
                          :items="character_types"
                          label="Тип"
                          item-value="text"
                        ></v-select>
                      </v-container>
                    </v-card-text>

                    <v-card-text>
                      <v-container>
                        Ивенты персонажа
                      </v-container>
                      <v-chip
                        v-for="(event, i) in changedEvents"
                        close
                        :key="i"
                        class="ma-2"
                        color="event.color"
                        @click:close="event.character = false"
                        v-show="event.character"
                      >
                        {{ event.name }}
                      </v-chip>
                    </v-card-text>

                    <v-card-text>
                      <v-container>
                        Все ивенты
                      </v-container>
                      <v-chip
                        v-for="(event, i) in changedEvents"
                        :key="i"
                        class="ma-2"
                        color="event.color"
                        @click="event.character = true"
                        v-show="!event.character"
                      >
                        {{ event.name }}
                      </v-chip>
                    </v-card-text>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="close"
                      >
                        Отмена
                      </v-btn>
                      <v-btn
                        color="blue darken-1"
                        text
                        @click="save"
                      >
                        Сохранить
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
                <v-dialog v-model="dialogDelete" max-width="500px">
                  <v-card>
                    <v-card-title class="text-h5">Удалить персонажа?</v-card-title>
                    <v-card-actions>
                      <v-btn color="blue darken-1" text @click="closeDelete">Отменить</v-btn>
                      <v-spacer></v-spacer>
                      <v-btn color="blue darken-1" text @click="deleteItemConfirm">Да</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </v-toolbar>
            </template>
            <template v-slot:item.0="{ item }">
              <v-simple-checkbox
                v-model="item[0]"
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.1="{ item }">
              <v-simple-checkbox
                v-model="item[1]"
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.2="{ item }">
              <v-simple-checkbox
                v-model="item[2]"
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.3="{ item }">
              <v-simple-checkbox
                v-model="item[3]"
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.4="{ item }">
              <v-simple-checkbox
                v-model="item[4]"
              ></v-simple-checkbox>
            </template>
            <template v-slot:item.actions="{ item }">
              <v-icon
                small
                class="mr-2"
                @click="editItem(item)"
              >
                mdi-pencil
              </v-icon>
              <v-icon
                small
                @click="deleteItem(item)"
              >
                mdi-delete
              </v-icon>
            </template>
            <template v-slot:no-data>
              <v-btn
                color="primary"
                @click="getCharacters"
              >
                Обновить
              </v-btn>
            </template>
          </v-data-table>
        </template>
      </v-col>
    </v-row>
  </section>
</template>

<script>
import server from '@/server'

export default {
  components: { },
  name: 'Characters',
  data: () => ({
    info: '',
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: 'Никнейм',
        align: 'start',
        sortable: true,
        value: 'name'
      },
      { text: 'Дозор', value: 'Дозор' },
      { text: 'Жертва богам', value: 'Жертва богам' },
      { text: 'Задание наемника', value: 'Задание наемника' },
      { text: 'Действия', value: 'actions', sortable: false }
    ],
    characterList: [],
    editedIndex: -1,
    editedItem: {
      name: '',
      email: ''
    },
    defaultItem: {
      name: '',
      email: ''
    },
    character_types: [
      'Основа',
      'Твин',
      'Репутация'
    ],
    chip1: true,
    events: [
      {
        name: 'Охота на элиту',
        color: 'primary',
        character: true
      },
      {
        name: 'Дозор',
        color: 'red',
        character: true
      },
      {
        name: 'Подземелье',
        color: 'green',
        character: false
      }
    ]
  }),
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'Новый персонаж' : 'Изменить персонажа'
    },
    changedEvents: {
      get: function () {
        return this.events
      },
      set: function (events) {
        events.forEach((event) => {
          event.character = false
        })
        this.events = events
        return this.events
      }
    }
  },
  methods: {
    editItem (item) {
      this.editedIndex = this.characterList.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = this.characterList.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },

    deleteItemConfirm () {
      this.characterList.splice(this.editedIndex, 1)
      this.closeDelete()
    },

    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },

    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.characterList[this.editedIndex], this.editedItem)
      } else {
        this.characterList.push(this.editedItem)
      }
      this.close()
    },
    createCharacter () {
      try {
        this.axios
          .get(server + 'characters/create/')
          .then(response => {
            console.log(response.data)
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    getCharacters () {
      try {
        var today = new Date()
        var date = `${today.getFullYear()}-${today.getMonth() + 1}-${today.getDate()}`
        this.axios.defaults.headers.common.Authorization = 'Token ' + localStorage.getItem('user-token')
        this.axios
          .get(server + 'user/characters/events/', { params: { date: date } })
          .then(response => {
            var eventList = []
            var array = response.data.map(item => [{ name: item.character.nickname }, item.character.character_events.map(item => [item.event.name, item.status])])
            var res = []
            for (var i = 0; i < array.length; i++) {
              res.push(array[i][0])
              for (var j = 0; j < array[i][1].length; j++) {
                var eventItem = {}
                eventItem[array[i][1][j][0]] = array[i][1][j][1]
                res[i] = Object.assign({}, res[i], eventItem)
                if (eventList.indexOf(array[i][1][j][0]) < 0) {
                  eventList.push(array[i][1][j][0])
                }
              }
            }
            this.characterList = res
            var m = []
            for (i = 0; i < eventList.length; i++) {
              var d = {}
              d.text = eventList[i]
              d.value = i
              m.push(d)
            }
            this.headers = [].concat(this.headers[0], m, this.headers[this.headers.length - 1])
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    getEvents () {
      try {
        this.axios
          .get(server + 'events/')
          .then(response => {
            // events = response.data
            this.changedEvents = response.data
            console.log(this.events)
          })
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    }
  },
  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    }
  },
  created () {
    this.getCharacters()
    this.getEvents()
  }
}
</script>

<style>
</style>
