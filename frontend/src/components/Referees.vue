<template>
    <div>
        <div class="info">
            <h2>Arbitros</h2>
            <div class="content">

                <b-button @click="goToAddReferee()" variant="primary">Agregar Arbitro</b-button>

                <b-table selectable select-mode="single" hover @row-selected="" :items="referees" :fields="fields" caption-top>
                    <template #table-caption>Arbitros</template>
                </b-table>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Referees',

    data() {
        return {
            referees: [],
            fields: [
                {key: 'first_name', label: 'Nombre'},
                {key: 'email', label: 'Correo Electronico'},
                {key: 'phone_number', label: 'Numero de telefono'}
            ]
        }
    },
    methods: {
        async getData() {
            const path = "http://127.0.0.1:8000/api/referees/list/"
            await axios.get(path).then((response) => {
                this.referees = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        },
        goToAddReferee() {
            this.$router.push('/add_referee/')
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