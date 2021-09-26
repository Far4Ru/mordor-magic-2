<template>
  <v-app>
    <v-app-bar
      app
    >
      <div class="d-flex align-center">
        <h1 class="headline">Гильдия MORDOR (из игры Eternal Magic)</h1>
      </div>
    </v-app-bar>
    <v-main class="d-flex align-center text-center">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    //
  })
}
</script>
