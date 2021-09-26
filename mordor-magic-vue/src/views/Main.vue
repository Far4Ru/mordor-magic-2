<template>
  <v-app id="inspire">
    <v-app-bar
      app
      color="white"
      flat
    >
      <v-container class="py-0 fill-height">
        <v-avatar color="grey" @click="page = 'profile'; leftPanel = true">
          <v-icon>
            mdi-transmission-tower
          </v-icon>
        </v-avatar>
        <v-spacer></v-spacer>

        <v-btn
          v-for="(val, link) in links"
          :key="link"
          text
          @click="page = val; leftPanel = val == 'profile' ? true : false"
        >
          <v-badge
            bordered
            :value="0"
            dot
          >
            {{ link }}
          </v-badge>
        </v-btn>

        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>

        <!-- <v-responsive max-width="260">
          <v-text-field
            dense
            flat
            hide-details
            rounded
            solo-inverted
          ></v-text-field>
        </v-responsive> -->
        <v-spacer></v-spacer>
        <avatar-menu />
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2" v-show='leftPanel'>
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <v-list-item
                  v-for="(val, pageName) in pages"
                  :key = pageName
                  link
                >
                  <v-list-item-content>
                    <v-list-item-title @click="page = val">
                      <v-badge
                        color="blue"
                        :content="0"
                        :value="0"
                        inline
                      >
                        {{ pageName }}
                      </v-badge>
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet
              min-height="70vh"
              rounded="lg"
            >
              <members v-show="page == 'members'"/>
              <characters v-show="page == 'characters'"/>
              <adv v-show="page == 'adv'"/>
              <events v-show="page == 'events'"/>
              <messages v-show="page == 'messages'"/>
              <profile v-show="page == 'profile'"/>
              <settings v-show="page == 'settings'"/>
              <tasks v-show="page == 'tasks'"/>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import AvatarMenu from '@/components/AvatarMenu'
import Members from '@/components/Members'
import Characters from '@/components/Characters'
import Adv from '@/components/Adv'
import Events from '@/components/Events'
import Messages from '@/components/Messages'
import Profile from '@/components/Profile'
import Settings from '@/components/Settings'
import Tasks from '@/components/Tasks'
export default {
  name: 'App',
  data: () => ({
    links: {
      Главная: 'profile',
      // Объявления: 'adv',
      Участники: 'members',
      // 'Библиотека',
      События: 'events'
    },
    pages: {
      Профиль: 'profile',
      // 'Новости',
      // Сообщения: 'messages',
      Персонажи: 'characters'
      // 'Мои задачи': 'tasks'
      // 'Закладки'
    }
  }),
  props: ['page', 'leftPanel'],
  components: {
    AvatarMenu,
    Members,
    Characters,
    Adv,
    Events,
    Messages,
    Profile,
    Settings,
    Tasks
  },
  created () {
    this.page = 'profile'
    this.leftPanel = true
  }
}
</script>
