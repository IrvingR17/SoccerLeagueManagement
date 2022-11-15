<template>
    <div>
        <div class="info">
            <h2>Editar Equipo</h2>
            <h5>Ingresa los campos para actualizar equipo</h5>

                <b-form @submit.prevent="editTeam()">

                    <b-form-group id="input-group-1" label="Nombre del equipo:" label-for="input-1">
                        <b-form-input
                        id="input-1"
                        v-model="name"
                        placeholder="Nombre"
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
                    <b-button @click="deleteTeam()" variant="danger">Eliminar equipo</b-button>

                </b-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'EditTeam',    

    data() {
        return {
            id: null,
            name: '',
            manager: '',
            team: '',
            options: '',
        }
    },
    methods: {
        async editTeam() {
            this.id = this.$route.params.id
            const data = { name: this.name, manager_name: this.manager.id, league_name: this.team.league_name }
            const path = 'http://127.0.0.1:8000/api/teams/edit/' + this.id
            await axios.put(path, data) 
        },
        async getData () {
            this.id = this.$route.params.id
            let path = "http://127.0.0.1:8000/api/managers/list/"
            await axios.get(path).then((response) => {
                this.options = response.data
            })
            .catch((error) => {
                console.log(error)
            })

            path = "http://127.0.0.1:8000/api/teams/list2/" + this.id
            await axios.get(path).then((response) => {
                this.team = response.data
            })
            .catch((error) => {
                console.log(error)
            })

            this.name = this.team.name
        },
        async deleteTeam() {
            this.id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/teams/delete/' + this.id
            await axios.delete(path)
        }
    },
    created() {
        this.getData()
    },
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