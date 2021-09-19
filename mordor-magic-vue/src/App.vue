<template>
  <v-app id="inspire">
    <v-app-bar
      app
      color="white"
      flat
    >
      <v-container class="py-0 fill-height">
        <v-avatar color="grey">
          <v-icon>
            mdi-transmission-tower
          </v-icon>
        </v-avatar>
        <v-spacer></v-spacer>

        <v-btn
          v-for="link in links"
          :key="link"
          text
          v-on:click="$router.push('Nasa');"
        >
          {{ link }}
        </v-btn>

        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-text-field
            dense
            flat
            hide-details
            rounded
            solo-inverted
          ></v-text-field>
        </v-responsive>
        <v-spacer></v-spacer>
        <avatar-menu />
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
      <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
              <v-list color="transparent">
                <v-list-item
                  v-for="page in pages"
                  :key="page"
                  link
                >
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ page }}
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
              <router-view></router-view>
            </v-sheet>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import AvatarMenu from '@/components/AvatarMenu'
export default {
  name: 'App',
  data: () => ({
    links: [
      'Главная',
      'Объявления',
      'Участники',
      // 'Библиотека',
      'События'
    ],
    pages: [
      'Профиль',
      // 'Новости',
      'Сообщения',
      'Персонажи',
      'Мои задачи'
      // 'Закладки'
    ]
  }),
  components: {
    AvatarMenu
  }
}
</script>
