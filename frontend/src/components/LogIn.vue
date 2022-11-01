<template>
    <form @submit.prevent="login()">
        <h1>Login</h1>
        <div>
          <input type="email" placeholder="Correo electronico" v-model="email">
        </div>
        <div>
          <input type="password" placeholder="Contraseña" v-model="password">
        </div>
        <div v-if="error">
          {{error}}
        </div>
        <div v-if="success" id="success">
          Logged in Successfully
        </div>
        <button type="submit">Ingresar</button>
    </form>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            email: '',
            password: '',
            error: null,
            success: false
        }
    },
    methods: {
      async login() {
        const data = { email: this.email, password: this.password };
        const response = await axios.post('http://127.0.0.1:8000/auth/token/login', data) 
      }
    }
}
</script>