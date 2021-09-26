<template>
  <v-menu
    bottom
    min-width="200px"
    rounded
    offset-y
  >
    <template v-slot:activator="{ on }">
      <v-btn
        icon
        x-large
        v-on="on"
      >
        <v-avatar
          color="blue"
          size="42"
        >
          <span class="white--text text-h5">{{ user.initials }}</span>
        </v-avatar>
      </v-btn>
    </template>
    <v-card>
      <v-list-item-content class="justify-center">
        <div class="mx-auto text-center">
          <v-container>
            <v-row>
              <v-col>
                <v-avatar
                  color="blue"
                >
                  <span class="white--text text-h5">{{ user.initials }}</span>
                </v-avatar>
              </v-col>
              <v-col>
                <h4>{{ user.fullName }}</h4>
                <p class="text-caption mt-1">
                  {{ user.email }}
                </p>
              </v-col>
            </v-row>
          </v-container>
          <v-divider class="my-3"></v-divider>
          <v-btn
            block
            text
          >
            Настройки
          </v-btn>
          <v-divider class="my-3"></v-divider>
          <v-btn
            block
            text
            v-on:click="$router.push('/');"
          >
            Выйти
          </v-btn>
        </div>
      </v-list-item-content>
    </v-card>
  </v-menu>
</template>
<script>
export default {
  name: 'AvatarMenu',
  data: () => ({
    user: {
      initials: 'S',
      fullName: 'Sasha',
      email: 'far4ru@gmail.com'
    }
  })
  // TODO: - http://127.0.0.1:8000/auth/token/logout/
  // Authorization Token ...
}
</script>
