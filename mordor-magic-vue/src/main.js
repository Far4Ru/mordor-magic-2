import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import ripple from 'vuetify/lib/directives/ripple'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(VueAxios, axios)
Vue.use(vuetify, {
  directives: {
    ripple
  }
})

new Vue({
  router,
  vuetify,
  axios,
  render: h => h(App)
}).$mount('#app')
