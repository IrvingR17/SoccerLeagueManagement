<template>
    <div>
        <div class="info">
            <h2>Representantes de equipo</h2>
            <div class="content">

                <b-button @click="goToAddManager()" variant="primary">Agregar Representante de equipo</b-button>

                <b-table selectable select-mode="single" hover @row-selected="" :items="managers" :fields="fields" caption-top>
                    <template #table-caption>Representantes:</template>
                </b-table>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Managers',

    data() {
        return {
            managers: [],
            fields: [
                {key: 'manager_name.first_name', label: 'Nombre'},
                {key: 'manager_name.email', label: 'Correo Electronico'},
                {key: 'manager_name.phone_number', label: 'Numero de telefono'},
                {key: 'name', label: 'Equipo'}
            ]
        }
    },
    methods: {
        async getData() {
            let path = "http://127.0.0.1:8000/api/manager_team/list/"
            await axios.get(path).then((response) => {
                this.managers = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        goToAddManager() {
            this.$router.push('/add_manager/')
        },    
    },
    created() {
        this.getData()
    },
}
</script>

<style scoped>
.containe {
    display: flex;
}
.info {
    flex: 80%;
    margin: 15px;
}
h2 {
    border-bottom: 1px solid black;
    text-align: left;
}
</style>