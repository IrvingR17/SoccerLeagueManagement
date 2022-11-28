<template>
    <div>
        <div class="info">
            <h2>Editar Equipo</h2>
            <h5>Ingresa los campos para actualizar equipo</h5>
            <div class="form">
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
                    <b-button type="submit" variant="primary">Editar Equipo</b-button>
                    <b-button @click="deleteTeam()" variant="danger">Eliminar equipo</b-button>

                </b-form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'EditTeam',    

    data() {
        return {
            id: '',
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
            this.goToTeam()
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
            let text = "¿Seguro deseas eliminar este equipo?";
            if (confirm(text) == true) {
                this.id = this.$route.params.id
                const path = 'http://127.0.0.1:8000/api/teams/delete/' + this.id
                await axios.delete(path)
                this.goToLeague()
            } else {

            }
        },
        goToTeam() {
            alert("Equipo actualizado correctamente")
            this.$router.back() 
        },
        goToLeague() {
            alert("Equipo borrado correctamente")
            this.$router.push("/leagues")           
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
.form {
    margin: 25px 50px 0 50px;
}
h2 {
    border-bottom: 1px solid black;
    text-align: left;
}
</style>