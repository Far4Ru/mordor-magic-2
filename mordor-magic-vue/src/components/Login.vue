<template>
  <section>
    <form>
      <v-row>
        <v-col cols="3" class="mx-auto">
          <h2>Вход</h2>
          <v-text-field
            v-model="name"
            :error-messages="nameErrors"
            :counter="30"
            label="Имя"
            required
            @input="$v.name.$touch()"
            @blur="$v.name.$touch()"
          ></v-text-field>
          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Пароль"
            counter
            @click:append="show1 = !show1"
          ></v-text-field>
          <v-btn
            class="mr-4"
            @click="submit"
          >
            Войти
          </v-btn>
          <v-btn @click="changeToRegistration">
            Регистрация
          </v-btn>
        </v-col>
      </v-row>
    </form>
  </section>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, maxLength, email } from 'vuelidate/lib/validators'
import server from '@/server'

export default {
  mixins: [validationMixin],

  validations: {
    name: { required, maxLength: maxLength(10) },
    email: { required, email },
    select: { required },
    checkbox: {
      checked (val) {
        return val
      }
    }
  },

  data: () => ({
    name: '',
    password: '',
    show1: false,
    rules: {
      required: value => !!value || 'Необходимо заполнить',
      min: v => (v && v.length >= 8) || 'Не менее 8 символов'
    }
  }),

  computed: {
    selectErrors () {
      const errors = []
      if (!this.$v.select.$dirty) return errors
      !this.$v.select.required && errors.push('Item is required')
      return errors
    },
    nameErrors () {
      const errors = []
      if (!this.$v.name.$dirty) return errors
      !this.$v.name.required && errors.push('Необходимо заполнить.')
      return errors
    }
  },

  methods: {
    submit () {
      this.$v.$touch()
      this.login()
    },
    async login () {
      const data = new FormData()
      data.set('username', this.name)
      data.set('password', this.password)
      const config = {
        header: {
          'Content-Type': 'multipart/form-data'
        }
      }
      this.axios
        .post(server + 'auth/token/login/', data, config)
        .then(response => {
          this.info = response
          if (response.status === 200 && response.data.auth_token) {
            localStorage.setItem('user-token', response.data.auth_token)
            this.$router.push('Home')
          }
        })
        .catch(e => {
          console.error('AN API ERROR', e)
        })
    },
    clear () {
      this.$v.$reset()
      this.name = ''
      this.select = null
      this.checkbox = false
    },
    changeToRegistration () {
      this.$emit('changeLoginPage', false)
    }
  }
}
</script>
