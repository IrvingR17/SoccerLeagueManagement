<template>
    <div>
        <div class="containe">
            <div class="info">
                <h2>Agregar equipo</h2>
                <h5>Ingresa los campos para dar de alta un nuevo equipo</h5>

                <b-form @submit.prevent="addTeam()">

                    <b-form-group id="input-group-1" label="Nombre del equipo:" label-for="input-1">
                        <b-form-input
                        id="input-1"
                        v-model="name"
                        placeholder="Equipo"
                        required
                        ></b-form-input>
                    </b-form-group>
                    <b-form-group id="input-group-1" label="Representante:" label-for="input-2">
                        <b-form-select
                        id="input-2"
                        v-model="manager"
                        :options="options"
                        required
                        >
                        <option v-for="option in options" :value="option">
                            {{ option.first_name + " " + option.last_name }}
                        </option>
                    </b-form-select>
                    </b-form-group>
                    <b-button type="submit" variant="primary">Enviar</b-button>

                </b-form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'AddTeam',
    data() {
        return {
            name: '',
            manager: '',
            league_name: '',
            options: '', 
        }
    },
    methods: {
        async addTeam () {
            const data = { name: this.name, manager_name: this.manager.id, league_name: this.league_name.id };
            const response = await axios.post('http://127.0.0.1:8000/api/teams/create/', data) 
        },
        async getData () {
            this.id = this.$route.params.id
            let path = "http://127.0.0.1:8000/api/leagues/list/" + this.id
            await axios.get(path).then((response) => {
                this.league_name = response.data
            })
            .catch((error) => {
                console.log(error)
            })

            
            path = "http://127.0.0.1:8000/api/managers/list/"
            await axios.get(path).then((response) => {
                this.options = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getData()
    }
}
</script>

<style scoped>

    .info {
        text-align: left;
        margin: 15px;
    }
    h2 {
        border-bottom: 1px solid black;
        text-align: left;
    }
</style>
