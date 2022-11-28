<template>
    <div class="info">
        <h2>Editar Liga</h2>
        <h5>Ingresa los campos para editar liga</h5>

        <div class="form">
            <b-form @submit.prevent="editLeague()">

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
                <b-button type="submit" variant="primary">Editar Liga</b-button>
                <b-button @click="deleteLeague()" variant="danger">Eliminar Liga</b-button>

            </b-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'EditLeague',

    data() {
        return {
            id: null,
            name: '',
            description: '',
            league: '',
        }
    },
    methods: {
        async getData () {
            this.id = this.$route.params.id
            let path = "http://127.0.0.1:8000/api/leagues/list/" + this.id
            await axios.get(path).then((response) => {
                this.league = response.data
            })
            .catch((error) => {
                console.log(error)
            })

            this.name = this.league.name
        },
        async editLeague() {
            this.id = this.$route.params.id
            const data = { name: this.name, description: this.description }
            const path = 'http://127.0.0.1:8000/api/leagues/edit/' + this.id
            await axios.put(path, data) 
            this.goToLeague()
        },
        async deleteLeague() {
            this.id = this.$route.params.id
            const path = 'http://127.0.0.1:8000/api/leagues/delete/' + this.id
            await axios.delete(path)
        },
        goToLeague() {
            alert("Liga actualizada correctamente")
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
    margin:  25px 50px 0 50px;
}
h2 {
    border-bottom: 1px solid black;
    text-align: left;
}
</style>