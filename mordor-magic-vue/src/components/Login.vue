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
            v-on:click="$router.push('Home');"
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
    email: '',
    select: null,
    items: [
      'Item 1',
      'Item 2',
      'Item 3',
      'Item 4'
    ],
    checkbox: false,
    show1: false,
    rules: {
      required: value => !!value || 'Необходимо заполнить',
      min: v => v.length >= 8 || 'Не менее 8 символов'
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
    },
    clear () {
      this.$v.$reset()
      this.name = ''
      this.select = null
      this.checkbox = false
    },
    changeToRegistration () {
      // TODO - Переключение на регистрацию
    }
  }
}
</script>
