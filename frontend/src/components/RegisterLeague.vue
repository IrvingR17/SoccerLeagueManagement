<template>
    <div>
        <div class="containe">
            <div class="info">
                <h2>Registrar Liga</h2>
                <h5>Ingresa los campos para dar de alta una nueva liga</h5>
            <div class="form">
                <b-form @submit.prevent="addLeague()">

                    <b-form-group id="input-group-1" label="Nombre de la liga:" label-for="input-1">
                        <b-form-input
                        id="input-1"
                        v-model="name"
                        placeholder="Nombre"
                        required
                        ></b-form-input>
                    </b-form-group>
                    <b-form-group id="input-group-2" label="Descripcion de la liga:" label-for="input-2">
                        <b-form-input
                        id="input-2"
                        v-model="description"
                        placeholder="Descripcion"
                        required
                        ></b-form-input>
                    </b-form-group>
                    <b-button type="submit" variant="primary">Registrar Liga</b-button>

                </b-form>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'RegisterLeague',
    data() {
        return {
            name: '',
            description: '',
        }
    },
    methods: {
        async addLeague () {
            const data = { name: this.name, description: this.description };
            const response = await axios.post('http://127.0.0.1:8000/api/leagues/create/', data) 
            this.goToLeagues()
        },
        goToLeagues() {
            alert("Liga agregada correctamente")
            this.$router.push('/leagues')
        }
    }
}
</script>

<style scoped>

    .info {
        text-align: left;
        margin: 15px;
    }
    .form {
        margin: 25px 50px 0 50px;

    }
    h2 {
        border-bottom: 1px solid black;
        text-align: left;
    }
</style>