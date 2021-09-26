<template>
  <section>
    <form>
      <v-row>
        <v-col cols="3" class="mx-auto">
          <h2>Регистрация</h2>
          <v-text-field
            v-model="name"
            :error-messages="nameErrors"
            :counter="10"
            label="Имя"
            required
            @input="$v.name.$touch()"
            @blur="$v.name.$touch()"
          ></v-text-field>
          <v-text-field
            v-model="email"
            :error-messages="emailErrors"
            label="Эл. почта"
            required
            @input="$v.email.$touch()"
            @blur="$v.email.$touch()"
          ></v-text-field>
          <v-text-field
            v-model="password"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            label="Пароль"
            hint="От 8 символов"
            counter
            @click:append="show1 = !show1"
          ></v-text-field>

          <v-btn
            class="mr-4"
            @click="submit"
          >
            Зарегистрироваться
          </v-btn>
          <v-btn @click="changeToLogin">
            Назад
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
    name: { required, maxLength: maxLength(30) },
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
    email: '',
    password: '',
    select: null,
    checkbox: false,
    show1: false,
    rules: {
      required: value => !!value || 'Необходимо заполнить',
      min: v => (v && v.length >= 8) || 'Минимум 8 символов'
    }
  }),

  computed: {
    selectErrors () {
      const errors = []
      if (!this.$v.select.$dirty) return errors
      !this.$v.select.required && errors.push('Необходимо заполнить')
      return errors
    },
    nameErrors () {
      const errors = []
      if (!this.$v.name.$dirty) return errors
      !this.$v.name.required && errors.push('Необходимо заполнить')
      return errors
    },
    emailErrors () {
      const errors = []
      if (!this.$v.email.$dirty) return errors
      !this.$v.email.email && errors.push('Почта должна быть действительной')
      !this.$v.email.required && errors.push('Необходимо заполнить')
      return errors
    }
  },

  methods: {
    submit () {
      this.$v.$touch()
      this.register()
    },
    async register () {
      const data = new FormData()
      data.set('username', this.name)
      data.set('email', this.email)
      data.set('password', this.password)
      const config = {
        header: {
          'Content-Type': 'multipart/form-data'
        }
      }
      this.axios
        .post(server + 'auth/users/', data, config)
        .then(response => {
          this.info = response
          if (response.status === 201) {
            this.changeToLogin()
          }
        })
        .catch(e => {
          console.error('AN API ERROR', e)
        })
    },
    clear () {
      this.$v.$reset()
      this.name = ''
      this.email = ''
      this.select = null
      this.checkbox = false
    },
    changeToLogin () {
      this.$emit('changeLoginPage', true)
    }
  }
}
</script>
